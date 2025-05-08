
import streamlit as st
import os
from openai import AzureOpenAI

# Use Streamlit secrets instead of .env
endpoint = st.secrets["AZURE_OPENAI_ENDPOINT"]
api_key = st.secrets["AZURE_OPENAI_API_KEY"]
deployment = st.secrets["AZURE_OPENAI_DEPLOYMENT"]
api_version = st.secrets["AZURE_OPENAI_API_VERSION"]

# Azure OpenAI client
client = AzureOpenAI(
    api_key=api_key,
    azure_endpoint=endpoint,
    api_version=api_version
)

def genai_response(prompt):
    try:
        response = client.chat.completions.create(
            model=deployment,
            messages=[
                {"role": "system", "content": "You are a helpful Business Analyst assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[ERROR] {str(e)}"

st.set_page_config(page_title="GenAI BA Assistant", layout="centered")
st.title("🤖 GenAI BA Assistant")

task = st.selectbox("Choose your task", [
    "Generate User Stories",
    "Generate UAT Test Cases",
    "Summarize Requirements",
    "Generate Sprint Report"
])

input_text = st.text_area("Paste your input here", height=200)

if st.button("Generate"):
    if not input_text.strip():
        st.warning("Please enter some input to proceed.")
    else:
        prompt = input_text
        result = genai_response(prompt)
        st.subheader("📄 GenAI Output")
        st.code(result, language='markdown')
