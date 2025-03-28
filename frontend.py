import streamlit as st
import requests

# FastAPI URL
API_URL = "http://127.0.0.1:8000/execute"

# Streamlit UI
st.set_page_config(page_title="LLM + RAG Automation", layout="centered")
st.title("🚀 LLM + RAG-Based Automation")

st.write("Enter a command, and the system will map it to the best-matching function.")

# User input
prompt = st.text_input("Enter your prompt:", placeholder="Example: Open Chrome")

if st.button("Execute"):
    if prompt:
        response = requests.post(API_URL, json={"prompt": prompt})
        result = response.json()
        
        if "error" in result:
            st.error(f"❌ {result['error']}")
        else:
            st.success(f"✅ Matched Function: `{result['function']}`")
    else:
        st.warning("⚠️ Please enter a prompt.")

st.markdown("---")
st.write("💡 This app uses **FastAPI + ChromaDB** for function retrieval.")

