import sqlite3

from db_helper import DB_PATH

# Connect to SQLite database and display success message
connection = None
try:
    connection = sqlite3.connect(DB_PATH)
    print("Database connected successfully.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection is not None:
        connection.close()
