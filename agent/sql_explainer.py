from agent.llm import llm

def explain_sql(sql):

    prompt = f"Explain this SQL query in simple terms:\n{sql}"

    response = llm.invoke(prompt)

    return response.content