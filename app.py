import streamlit as st
import os
from dotenv import load_dotenv
from langchain_groq import chatGroq
from langchain_core.tools import tools
from langchain.prebuild import create_react_agent
load_dotenv()
#1.Initialize Groq LLM
llm=ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY")
)
@tool
def add_numbers(a:int,b:int)->int:
    """Add two numbers."""
    return a+b
    agent=create_react_agent(
        llm,
        [add_numbers]
    )
    #4.Streamlit UI
    st.title ("My First AI Agent")
    question=st.chat_input("Ask something...")
    if question:
        st.write("You:",question)
        #5.Execute Agent
        result=agent.invoke({
            "message":[
                {"role":"user","content":question}
            ]
        })
        #6.Display response
        answer=result["message"][-1].content
        st.write("AI Agent:",answer)