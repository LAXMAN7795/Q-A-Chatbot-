from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

# Langsmith Tracking
os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')
os.environ["LANGCHAIN_TRACING_V2"] = "true" 
os.environ['LANGCHAIN_PROJECT']="Q&A_Chatbot"

# Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the questions."),
        ("user","question:{question}")
    ]
)

def generate_response(question,llm,temperature,max_token):
    llm = Ollama(model=llm)
    output_parser = StrOutputParser()
    chain = prompt|llm|output_parser
    answer = chain.invoke({"question":question})
    return answer

# Title of the app
st.title("Q & A chatbot with Ollama")

# sidebar for settings
st.sidebar.title("Settings")

#drop down to select verious models
llm = st.sidebar.selectbox("select an model",["gemma:2b"])

# adjust response parameter
temperature = st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens = st.sidebar.slider("Max Tokens",min_value=50,max_value=300,value=150)

# main interface
st.write("ask any questions")
user_input = st.text_input("You:")

if user_input:
    response = generate_response(user_input,llm,temperature,max_tokens)
    st.write(response)
else:
    st.write("plase provide the query")