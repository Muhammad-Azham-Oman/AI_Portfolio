from dotenv import load_dotenv
from langchain_groq import ChatGroq
from chromadb.utils import embedding_functions
from langchain_core.prompts import PromptTemplate

ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

load_dotenv()

llm=None

print("Starting...")

def router(question):
    global llm
    if llm is None:
        llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=1.2)

    print("Making prompt...")
    faq =  ["Do you have a mobile app",
            "Do you offer gift wrapping",
            "Are there membership benefits",
            "How do I know if a product is in stock",
            "Is cash on delivery available",
            "How do I apply a discount coupon",
            "Can I use multiple coupons in one order",
            "Do you sell refurbished products",
            "How do I create an account",
            "How can I track my order"
        ]

    sql =  ["What is the price of Nike Air shoes?",
            "Show me shoes under 30 dollars",
            "Do you have jackets between 50 and 100 dollars?",
            "List smartphones cheaper than 200 dollars",
            "Find me a laptop under 500 dollars",
            "Are there any Adidas sneakers under 60 dollars?",
            "Show me the best headphones in the 40 to 80 dollar range",
            "What is the cheapest smartwatch you sell?",
            "Do you have t-shirts priced below 20 dollars?",
            "Give me all products under 10 dollars"
        ]

    prompt = '''
    You are an E_commerce Chatbot semantic router.
    
    I am providing you the data of two routes faq and sql you have to give me the best
    route from these two according to the question but if the question doesn't match 
    the logic of these two routes and all the irrelevant questions than simply return faq.
    
    Means all the information of Frequently asked questions that i get and train llm will
    go in faq and other which i get from webscraping and train llm go in sql.
    
    According to the bellow question which is the most probable answer.
    
    No preambles and only print faq or sql.
        
    faq
    =====
    {faq}
    =====
    
    sql
    ======
    {sql}
    ======
    
    question
    ======
    {question}
    ======'''

    print("Prompt Template....")
    pt = PromptTemplate.from_template(prompt)

    chain = pt | llm

    output = chain.invoke({
        "faq": faq,
        "sql": sql,
        "question": question
    }
    )

    print("output done....")
    return output.content

if __name__ == "__main__":

    query = ("hello")
    router(query)