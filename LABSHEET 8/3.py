import sqlite3

from db_helper import connect_db

# Create students table with the required columns
try:
    with connect_db() as con:
        con.execute(
            """
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                marks REAL NOT NULL
            )
            """
        )
    print("Table students is ready.")
except sqlite3.Error as error:
    print("Database error:", error)
