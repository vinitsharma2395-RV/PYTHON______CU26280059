import sqlite3
from db_helper import connect_db
# Demonstrate database exception handling
try:
    with connect_db() as con:
        con.execute("SELECT * FROM table_that_does_not_exist")
except sqlite3.Error as error:
    print("Database error handled:", error)
else:
    print("Query completed successfully.")
