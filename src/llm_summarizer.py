from langchain.llms import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

def summarize_document(text):
    llm = OpenAI(openai_api_key=openai_api_key, temperature=0.4)
    prompt = f"Summarize the following document text clearly and concisely:\n\n{text[:3000]}"
    response = llm(prompt)
    return response
