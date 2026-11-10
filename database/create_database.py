import sqlite3
from pathlib import Path
import pandas as pd

BASE_DIR =Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
DB_PATH = BASE_DIR / "database" / "pizza_sales.db"

connection=sqlite3.connect(DB_PATH)

csv_files=DATA_DIR.glob('*.csv')
for file in csv_files:
    
    df=pd.read_csv(file,encoding="cp1252")

    table_name=file.stem

    df.to_sql(
        table_name,
        connection,
        if_exists="replace",
        index=False
    )
    print(f"Imported file {table_name} : {len(df)} rows.")

connection.close()

print("Database created successfully..")








