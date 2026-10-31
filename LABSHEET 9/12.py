# Q12: Insert a new student record (Create operation)
import sqlite3
from db_helper import connect_db

connection = None
try:
    connection = connect_db()
    student_id = int(input("Enter roll number/ID: "))
    name = input("Enter student name: ").strip()
    age = int(input("Enter age: "))
    marks = float(input("Enter marks: "))

    connection.execute(
        "INSERT INTO students (id, name, age, marks) VALUES (?, ?, ?, ?)",
        (student_id, name, age, marks)
    )
    connection.commit()
    print("Student record inserted successfully.")
except ValueError:
    print("Please enter valid numeric values for ID, age and marks.")
except sqlite3.IntegrityError:
    print("This roll number/ID already exists.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection:
        connection.close()
