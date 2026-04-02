from sqlalchemy import inspect
from database.connection import engine

def get_schema():

    inspector = inspect(engine)

    tables = inspector.get_table_names()

    schema = ""

    for table in tables:

        columns = inspector.get_columns(table)

        schema += f"\nTable: {table}\n"

        for col in columns:
            schema += f"{col['name']} ({col['type']})\n"

    return schema