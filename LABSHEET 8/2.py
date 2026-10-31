import sqlite3

from db_helper import DB_PATH

# SQLite creates a database file automatically when connected
connection = None
try:
    connection = sqlite3.connect(DB_PATH)
    print(f"Database created/opened successfully: {DB_PATH.name}")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection is not None:
        connection.close()
