import sqlite3
from pathlib import Path

BASE_DIR =Path(__file__).resolve().parent.parent

DATABASE_LOC =BASE_DIR / "database" / "pizza_sales.db"

def inspect_schema():

    #connect to sqlite databse
    connection=sqlite3.connect(DATABASE_LOC)

    #cursor to execute the query
    cursor=connection.cursor()

    cursor.execute("""
SELECT name 
FROM sqlite_master
WHERE type = 'table'
and name NOT LIKE 'sqlite%'
""")
    tables =cursor.fetchall()

    #store database schema 
    schema={}

    for table in tables:

        table_name=table[0]

        cursor.execute(f"PRAGMA table_info('{table_name}')")

        columns=cursor.fetchall()

        columns_details=[]

        for column in columns:

            column_info={
                'column_name':column[1],
                'data_type':column[2],
                'not_null':bool(column[3]),
                'default_value':column[4],
                'primary_key':bool(column[5])
            }

            columns_details.append(column_info)

        schema[table_name]=columns_details
    connection.close()

    return schema

if __name__ == "__main__":
    database_schema =inspect_schema()

    for table_name,columns in database_schema.items():

        print(f'Table {table_name}')

        for column in columns:
            print(
                f"Column : {column['column_name']}"
                f" type : {column['data_type']}"
                f"Primary key {column['primary_key']}  "
            ) 




    




