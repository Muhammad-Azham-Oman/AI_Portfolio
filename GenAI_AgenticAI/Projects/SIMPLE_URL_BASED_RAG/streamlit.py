import streamlit as st
from RAG import*

st.title("Real Websites Research Tool")

try:
    url_num = st.sidebar.number_input("How many URLs do you want to provide?", min_value=0, max_value=4, step=1)

    urls = []

    if 1 <= url_num <= 4:
        for i in range(int(url_num)):
            url = st.sidebar.text_input(f"URL {i+1}")
            urls.append(url)

    print(urls)
    ind = []
    for index, url in enumerate(urls, start=1):
        if url.strip() == "":
            ind.append(index)

    if len(ind) != 0:
       st.sidebar.text(f"{len(ind)} URL's not provided.")

    elif len(ind) == 0 and len(urls) != 0:
        process_url_button = st.sidebar.button("Process")
        if process_url_button:
            process_urls(urls)
            st.session_state["processed"] = True
        if st.session_state.get("processed", False):
            process_urls(urls)
            question = st.text_area("Enter your question:")
            question_button = st.button("Get Answer")
            if question_button:
                st.text("Processing your question")
                answer, sources = generate_answer(question)
                st.text_area("Answer:", answer)
                st.text_area("Sources:", sources)

except:
    st.error("Something went wrong.")