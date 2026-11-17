import sqlite3
from pathlib import Path
import pandas as pd

BASE_DIR =Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
DB_PATH = BASE_DIR / "database" / "pizza_sales.db"

def create_database(uploaded_files=None):

    connection=sqlite3.connect(DB_PATH)

    if uploaded_files is not None:
        csv_files=uploaded_files
    else :
        csv_files=list(DATA_DIR.glob("*.csv"))

    if not csv_files:
        raise ValueError("No Csv files found")

    for file in csv_files:

        if hasattr(file,"seek"):
            file.seek(0)

        df=pd.read_csv(file,encoding="cp1252")

        table_name =Path(file.name).stem if hasattr(file,"name") else file.stem

        df.to_sql(table_name,connection,if_exists="replace",index=False)

        print(f"Imported file name {table_name} and the length of rows is {len(df)}")

    connection.close()


if __name__ == "__main__":
    create_database()

    





