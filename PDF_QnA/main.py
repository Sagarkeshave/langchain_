import streamlit as st
from helper_functions import get_qa_chain, create_vector

st.title("PDF data QnA 🌱")
btn = st.button("Create Knowledgebase")
# if btn:
#     create_vector()

question = st.text_input("Question: ")

if question:
    chain = get_qa_chain()
    response = chain(question)

    st.header("Answer")
    st.write(response["result"])




