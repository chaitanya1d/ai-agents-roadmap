"""Basic agent example using LangChain tools: RAG tool + Web search (DuckDuckGo).
Exposes /ask which runs an agent that can use tools.
"""
from flask import Flask, request, jsonify
from langchain.agents import initialize_agent, Tool
from langchain_community.llms import Ollama
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
import os

app = Flask(__name__)
CHROMA_DIR = './chroma_store'

def rag_tool():
    embeddings = OllamaEmbeddings(model='llama3')
    vectordb = Chroma(persist_directory=CHROMA_DIR, embedding_function=embeddings)
    llm = Ollama(model='llama3')
    return RetrievalQA.from_chain_type(llm, retriever=vectordb.as_retriever())

@app.route('/ask', methods=['POST'])
def ask():
    q = (request.get_json() or {}).get('question','')
    if not q:
        return jsonify({'error':'no question'}),400
    rag = rag_tool()
    web = DuckDuckGoSearchRun()
    tools = [
        Tool(name='RAG', func=rag.run, description='Answers from local docs'),
        Tool(name='WebSearch', func=web.run, description='Search the web')
    ]
    llm = Ollama(model='llama3')
    agent = initialize_agent(tools, llm, agent='zero-shot-react-description', verbose=False)
    out = agent.run(q)
    return jsonify({'answer': out})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
