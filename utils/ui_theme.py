import streamlit as st

def load_css():

    st.markdown("""
    <style>

    body {
        background: linear-gradient(135deg,#1f1c2c,#928dab);
    }

    .main-title{
        font-size:40px;
        font-weight:700;
        color:white;
        text-align:center;
        margin-bottom:20px;
    }

    .chat-user{
        background:#4e8cff;
        color:white;
        padding:12px;
        border-radius:10px;
        margin-bottom:10px;
    }

    .chat-ai{
        background:#2d2d2d;
        color:white;
        padding:12px;
        border-radius:10px;
        margin-bottom:10px;
    }

    .sql-box{
        background:#111;
        color:#00ff9c;
        padding:10px;
        border-radius:8px;
        font-family:monospace;
    }

    </style>
    """, unsafe_allow_html=True)