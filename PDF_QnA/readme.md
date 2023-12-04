# PDF chat Q&A: Question and Answer System Based on Google Palm LLM and Langchain for LargePDFs  

This is an end to end LLM project based on Google Palm and Langchain. We are building a Q&A system for large PDFs (Indian constituion).This system will provide a streamlit based user interface for students where they can ask questions and get answers. 


## Project Highlights

- We will build an LLM based question and answer system that can reduce the workload of their human staff.
- Students should be able to use this system to ask questions directly and get answers within seconds

## You will learn following,
  - Langchain + Google Palm: LLM based Q&A
  - Streamlit: UI
  - Google Palm: Text embeddings
  - FAISS: Vector databse

## Installation

1.Clone this repository to your local machine using:

```bash
  git clone https://github.com/Sagarkeshave/langchain_.git
```
2.Navigate to the project directory:

```bash
  cd PDF_QnA
```
3. Install the required dependencies using pip:

```bash
  pip install -r requirements.txt
```
4.Acquire an api key through makersuite.google.com and put it in .env file

```bash
  GOOGLE_API_KEY="your_api_key_here"
```
## Usage

1. Run the Streamlit app by executing:
```bash
streamlit run main.py

```

2.The web app will open in your browser.

- To create a knowledebase of FAQs, click on Create Knolwedge Base button. It will take some time before knowledgebase is created so please wait.

- Once knowledge base is created you will see a directory called faiss_index in your current folder

- Now you are ready to ask questions. Type your question in Question box and hit Enter

## Sample Questions
  - "How many members are their in the Parliament ?"
  - "What is the legal age for voting in India"
  - How many states are there?


## Project Structure

- main.py: The main Streamlit application script.
- langchain_helper.py: This has all the langchain code
- requirements.txt: A list of required Python packages for the project.
- .env: Configuration file for storing your Google API key.
