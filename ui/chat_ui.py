import streamlit as st

def chat_ui():

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:

        if msg["role"] == "user":

            st.markdown(
                f"<div class='chat-user'>👤 {msg['content']}</div>",
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                f"<div class='chat-ai'>🤖 {msg['content']}</div>",
                unsafe_allow_html=True
            )

    question = st.chat_input("Ask your database...")

    return question