from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

pt = PromptTemplate.from_template("Write a two line poem on {topic1} and {topic2}")

llm = ChatGroq(
    model='deepseek-r1-distill-llama-70b',
    temperature=1.8
)

chain = pt | llm
output = chain.invoke({'topic1' : 'dog','topic2' : 'cat'})

print(output.content)