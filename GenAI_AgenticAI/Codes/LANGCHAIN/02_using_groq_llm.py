from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(model='deepseek-r1-distill-llama-70b')
output = llm.invoke("Write theme of thristy crow for me as human being ")
print(output)