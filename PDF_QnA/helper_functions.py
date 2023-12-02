from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import GooglePalmEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import GooglePalm
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
import os
from dotenv import load_dotenv


load_dotenv()

google_api_key = os.environ["GOOGLE_API_KEY"]

# create model instance
llm = GooglePalm(google_api_key=google_api_key, temperature=0.1)

# create embedding
google_palm_embeddings = GooglePalmEmbeddings(google_api_key= google_api_key)

# we will create vector database and store it locally and use again (to avoid databasing multiple times)
file_path = "Constitution India ENG.pdf"
vectordb_file_path = "faiss_index_main"


def create_vector():
    reader = PdfReader(file_path)

    text = ""
    for page in reader.pages:
        text += page.extract_text()

    text_splitter = CharacterTextSplitter(

        chunk_size=1000,  # 1000 chars 1 section
        separator="\n",  # each new line a separator
        chunk_overlap=200,  # includes 200 previous chars to next section
        length_function=len  # calc chars
    )

    chunks = text_splitter.split_text(text)

    knowledge_base = FAISS.from_texts(chunks, google_palm_embeddings)

    ## save index
    knowledge_base.save_local(vectordb_file_path)


def get_qa_chain():

    knowledge_base = FAISS.load_local("faiss_index", google_palm_embeddings)

    # create retriever for performing the query
    retriever = knowledge_base.as_retriever(score_threshold=0.7)


    # prompt template to prevent model hallucination
    prompt_template = """ Given the following context and a question, generate an answer based on this
        context only. In the answer try to provide as much text as possible from "response" section in the source
        document context without making much changes. If the answer is not found in the context, kindly state "I dont know".
        Dont try to make up an answer.

        CONTEXT : {context}
        QUESTION : {question} """

    PROMPT = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "question"]
    )

    chain = RetrievalQA.from_chain_type(llm=llm,
                                        chain_type="stuff",
                                        retriever=retriever,
                                        input_key="query",
                                        return_source_documents=True,
                                        chain_type_kwargs={"prompt": PROMPT})

    return chain


if __name__ == "__main__":
    # create_vector_db()

    query = "How many members are their in the Parliament ?"
    query_2 = "Who is the best cricketor in the world"
    chain = get_qa_chain()

    print(chain(query_2)["result"])
