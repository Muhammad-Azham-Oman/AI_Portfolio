from pathlib import Path
import pandas as pd
import chromadb
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from chromadb.utils import embedding_functions
from langchain_core.prompts import PromptTemplate

ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

load_dotenv()

llm = None

client = chromadb.Client()

faq_path = Path(__file__).parent/"resources"/"ecommerce_faq.csv"

empty_list = []

collection_name = "ecommerce_faq"

def ingest_data(path):
    global collection_name
    df = pd.read_csv(path)

    if collection_name not in [c.name for c in client.list_collections()]:
        print("Injecting the data.")
        collection = client.get_or_create_collection(
            name=collection_name,
            embedding_function=ef)
        collection.add(
            documents=df["question"].tolist(),
            metadatas=[{"answer": ans} for ans in df["answer"].tolist()],
            ids=df["id"].astype(str).tolist()
        )

    else:
        print("Collection already exsists.")


def main(text):
    collection = client.get_collection(name="ecommerce_faq")
    print([c.name for c in client.list_collections()])
    results = collection.query(
    query_texts=[text],
    n_results=5
    )

    for i in range(len(results['ids'][0])):
        empty_list.append((results["metadatas"][0][i]).get('answer'))

    global llm
    if llm is None:
        llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=1.2)

    prompt = '''
    You are an E_commerce Chatbot.
    
    Your personal name is FlipKart chatbot.
    
    you are not llm not robot but a chatbot.
    
    I am providing you the data of answers.

    According to the bellow question which is the most probable answer.

    No preambles and you can do changes to provide good answer but only change
    wording not logic.Also don't make a very long answer give complete and to the point
    answer with reasonable explanation.
    
    If the question is related to your job return a short answer like Not related,etc...
    
    Don't afraid on the questions that user provides you don't have information about it.
    Just used your common sense and answer the question appropriate.
    
    Only In serious conditions give the customer support contact information with answer.
    The contacts of customer support are Phone Number:03020140713 , Email:azhamoman10@gmail.com

    data
    =====
    {data}
    =====

    question
    ======
    {question}
    ======'''

    pt = PromptTemplate.from_template(prompt)

    chain = pt | llm

    output = chain.invoke({
        "data" : list,
        "question" : text
    }
    )

    return output.content

if __name__ == "__main__":
    ingest_data(faq_path)
    user_text = ("what if I found my product broken?")
    main(user_text)