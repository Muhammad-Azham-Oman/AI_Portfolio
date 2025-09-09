from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2:1b", temperature=1.3, num_predict=100)

output = llm.invoke("can you give me story of thirsty crow")
print(output)