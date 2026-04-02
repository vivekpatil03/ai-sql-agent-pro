from langchain_core.prompts import PromptTemplate
from agent.llm import llm
import re


def clean_sql(response):

    sql = response.strip()

    sql = re.sub(r"```sql", "", sql, flags=re.IGNORECASE)
    sql = re.sub(r"```", "", sql)

    sql = re.sub(r"^sql\s+", "", sql, flags=re.IGNORECASE)

    return sql.strip()


def generate_sql(question, schema):

    prompt = PromptTemplate.from_template("""
You are an expert MySQL data analyst.

Database schema:
{schema}

IMPORTANT RULES:
1. Always use table aliases
2. Always qualify columns with aliases
3. Avoid ambiguous columns
4. Return ONLY SQL query                                         

Example:
SELECT e.name, SUM(s.amount)
FROM employees e
JOIN sales s ON e.emp_id = s.emp_id
GROUP BY e.name;

Question:
{question}

SQL:
""")

    chain = prompt | llm

    response = chain.invoke({
        "question": question,
        "schema": schema
    })

    sql = clean_sql(response.content)

    return sql