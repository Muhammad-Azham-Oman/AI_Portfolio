from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader
from langchain.chains import RetrievalQAWithSourcesChain
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from uuid import uuid4

load_dotenv()

directory = Path(__file__).parent / "resources/storage"

llm = None
storage = None


def initialize():
    global llm, storage
    if llm is None:
        llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=1.1, max_tokens=1000)

    if storage is None:
        ef = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={"trust_remote_code": True}
        )

        storage = Chroma(
            collection_name="Real_Estate_RAG",
            persist_directory=str(directory),
            embedding_function=ef
        )


def process_urls(urls):
    print("initializing")
    initialize()

    try:
        storage.reset_collection()
    except Exception:
        print("No existing collection. Creating a new one...")

    print("load_data")
    loader = WebBaseLoader(web_paths=urls)
    data = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=60,
        separators=["\n\n", "\n", ".", " "],
    )
    docs = text_splitter.split_documents(data)
    print("final")
    uuids = [str(uuid4()) for _ in range(len(docs))]
    storage.add_documents(docs, ids=uuids)


def generate_answer(query: str):
    if storage is None:
        raise RuntimeError("No existing collection. Creating a new one...")

    chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=storage.as_retriever())
    result = chain.invoke({"question": query},return_only_outputs=True)

    sources = result.get("sources", "")
    return result["answer"], sources


if __name__ == '__main__':
    urls = [
        "https://www.cnbc.com/2025/07/31/apple-aapl-q3-earnings-report-2025.html",
        "https://www.cnbc.com/2025/06/18/fed-meeting-heres-what-changed-in-the-new-statement.html"
    ]

    process_urls(urls)
    answer, sources = generate_answer("Give me the eps of apple")

    print(f"answer: {answer}")
    print(f"sources: {sources}")