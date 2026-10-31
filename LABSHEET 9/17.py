# Q17: Count total number of student records
import sqlite3
from db_helper import connect_db

connection = None
try:
    connection = connect_db()
    total = connection.execute("SELECT COUNT(*) FROM students").fetchone()[0]
    print("Total number of students:", total)
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection:
        connection.close()
