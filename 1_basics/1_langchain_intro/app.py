from langchain import PromptTemplate, LLMChain
from langchain_community.llms import Ollama

template = """You are an assistant. Answer briefly:
Question: {q}
"""
prompt = PromptTemplate.from_template(template)

def run_ollama(q):
    llm = Ollama(model="llama3")
    chain = LLMChain(llm=llm, prompt=prompt)
    print(chain.run(q))

if __name__ == '__main__':
    run_ollama('What is RAG in one sentence?')
