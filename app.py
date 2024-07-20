from flask import Flask, render_template, request, jsonify
import os
import getpass
import warnings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import pickle
from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.runnables import RunnableParallel

warnings.filterwarnings('ignore', category=DeprecationWarning)

os.environ["GOOGLE_API_KEY"] = ""

app = Flask(__name__)

def get_answer(question):
    return rag_chain_with_source.invoke(question)['answer']

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def prepare():
    llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.7)
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    faiss_index = FAISS.load_local("sth", embeddings=embeddings, allow_dangerous_deserialization=True)
    with open("sth/index.pkl", "rb") as f:
        docstore = pickle.load(f)
        if isinstance(docstore, tuple):
            docstore, index_to_docstore_id = docstore
            faiss_index.docstore = docstore
            faiss_index.index_to_docstore_id = index_to_docstore_id
        else:
            faiss_index.docstore = docstore
    retriever = faiss_index.as_retriever()
    prompt=hub.pull("rlm/rag-prompt")
    rag_chain_from_docs = (
            RunnablePassthrough.assign(context=(lambda x: format_docs(x["context"])))
            | prompt
            | llm
            | StrOutputParser()
    )

    rag_chain_with_source = RunnableParallel(
        {"context": retriever, "question": RunnablePassthrough()}
    ).assign(answer=rag_chain_from_docs)
    return rag_chain_with_source

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response_message = get_answer(user_message)
    return jsonify({'response': response_message})

if __name__ == '__main__':
    rag_chain_with_source = prepare()
    app.run(debug=True)
