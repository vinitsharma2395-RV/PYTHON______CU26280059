# Shared helper for Q11-Q20. Database file is created in this folder.
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).with_name("student_db.db")

def connect_db():
    connection = sqlite3.connect(DB_PATH)
    connection.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            marks REAL NOT NULL
        )
    """)
    connection.commit()
    return connection
