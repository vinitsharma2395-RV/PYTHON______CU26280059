# Q11: Connect to SQLite and create students table
import sqlite3
from db_helper import connect_db

try:
    connection = connect_db()
    print("Connected to database successfully.")
    print("Students table created or already exists.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if "connection" in locals():
        connection.close()
