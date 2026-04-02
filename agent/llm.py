from langchain_groq import ChatGroq
from config.settings import GROQ_API_KEY


llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=GROQ_API_KEY,
    temperature=0
)