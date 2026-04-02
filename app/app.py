import streamlit as st

from utils.ui_theme import load_css
from ui.sidebar import sidebar
from ui.chat_ui import chat_ui

from database.schema import get_schema

from agent.sql_generator import generate_sql
from agent.sql_executor import execute_sql
from agent.sql_guard import validate_sql

from utils.charts import create_chart

# ================= UI =================

st.set_page_config(
    page_title="AI SQL Agent",
    page_icon="🤖",
    layout="wide"
)

load_css()

st.markdown(
    "<div class='main-title'>🤖 AI SQL Data Analyst</div>",
    unsafe_allow_html=True
)

page = sidebar()

schema = get_schema()

# ================= CHAT PAGE =================

if page == "Chat":

    question = chat_ui()

    if question:

        st.session_state.messages.append(
            {"role":"user","content":question}
        )

        sql = generate_sql(question, schema)

        st.markdown(
            f"<div class='sql-box'>{sql}</div>",
            unsafe_allow_html=True
        )

        if validate_sql(sql):

            try:

                df = execute_sql(sql)

                st.subheader("📊 Result")

                st.dataframe(df, use_container_width=True)

                chart = create_chart(df)

                if chart:
                    st.plotly_chart(chart, use_container_width=True)

            except Exception as e:

                st.error(e)

        else:

            st.error("Unsafe SQL blocked")

        st.session_state.messages.append(
            {"role":"assistant","content":sql}
        )

# ================= DATABASE PAGE =================

if page == "Database":

    st.subheader("Database Schema")

    st.code(schema)

# ================= CSV PAGE =================

if page == "Upload CSV":

    st.subheader("Upload CSV to Database")

    file = st.file_uploader("Upload CSV")

    if file:

        from database.csv_loader import load_csv

        table = load_csv(file)

        st.success(f"Table created: {table}")