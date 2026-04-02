import pandas as pd
from database.connection import engine

def load_csv(file):

    df = pd.read_csv(file)

    table_name = file.name.replace(".csv","")

    df.to_sql(table_name, engine, if_exists="replace", index=False)

    return table_name