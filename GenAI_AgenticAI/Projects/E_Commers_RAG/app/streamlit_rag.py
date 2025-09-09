import streamlit as st
from router import router
from FAQ import ingest_data , main
from pathlib import Path
from sql import sql_chain

st.title("E_Commerce Chatbot")

query = st.chat_input("Please enter your query")

faq_path = Path(__file__).parent/"resources"/"ecommerce_faq.csv"

ingest_data(faq_path)

def ask(query):
    route = router(query)
    if route=="faq":
        return main(query)
    if route=="sql":
        return sql_chain(query)
    else:
        return f"{route} route is not implemented yet."


if "messages" not in st.session_state:
    st.session_state["messages"] = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
if query:
    with st.chat_message("human"):
        st.markdown(query)
    st.session_state.messages.append({"role":"human","content":query})

    response = ask(query)
    with st.chat_message("ai"):
        st.markdown(response)
    st.session_state.messages.append({"role": "ai", "content": response})