import pyodbc

def get_db_connection():

    conn = pyodbc.connect(
        "DRIVER={SQL Server};"
        "SERVER=DESKTOP-5OUD1G3;"
        "DATABASE=cafe_datab;"
        "Trusted_Connection=yes;"
    )

    return conn