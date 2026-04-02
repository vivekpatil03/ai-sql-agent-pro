import pandas as pd
from sqlalchemy import text
from database.connection import engine

def execute_sql(sql):

    with engine.connect() as conn:

        result = conn.execute(text(sql))

        df = pd.DataFrame(result.fetchall(), columns=result.keys())

    return df