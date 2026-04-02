import streamlit as st
from streamlit_option_menu import option_menu

def sidebar():

    with st.sidebar:

        selected = option_menu(
            "AI SQL Agent",
            ["Chat","Database","Upload CSV"],
            icons=["chat","database","upload"],
            menu_icon="robot",
            default_index=0
        )

    return selected