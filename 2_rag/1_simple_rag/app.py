"""Simple RAG: ingest a PDF, store embeddings in Chroma, and expose a /ask endpoint.
This example uses Ollama for embeddings & LLM locally, and Chroma as vectorstore.
"""
from flask import Flask, request, jsonify
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama

app = Flask(__name__)
CHROMA_DIR = './chroma_store'

@app.route('/ingest', methods=['POST'])
def ingest():
    data = request.get_json() or {}
    file_path = data.get('file_path')
    if not file_path or not os.path.exists(file_path):
        return jsonify({'error':'file not found'}), 400
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    embeddings = OllamaEmbeddings(model='llama3')
    vectordb = Chroma.from_documents(docs, embedding_function=embeddings, persist_directory=CHROMA_DIR)
    vectordb.persist()
    return jsonify({'status':'ingested'})

@app.route('/ask', methods=['POST'])
def ask():
    q = (request.get_json() or {}).get('question','')
    if not q:
        return jsonify({'error':'no question'}),400
    embeddings = OllamaEmbeddings(model='llama3')
    vectordb = Chroma(persist_directory=CHROMA_DIR, embedding_function=embeddings)
    llm = Ollama(model='llama3')
    qa = RetrievalQA.from_chain_type(llm, retriever=vectordb.as_retriever())
    res = qa.run(q)
    return jsonify({'answer':res})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
