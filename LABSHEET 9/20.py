# Q20: Menu-driven student management application using SQLite
import sqlite3
from db_helper import connect_db

def add_student(connection):
    try:
        student_id = int(input("Roll number/ID: "))
        name = input("Name: ").strip()
        age = int(input("Age: "))
        marks = float(input("Marks: "))
        connection.execute(
            "INSERT INTO students (id, name, age, marks) VALUES (?, ?, ?, ?)",
            (student_id, name, age, marks)
        )
        connection.commit()
        print("Student added.")
    except ValueError:
        print("Enter valid numeric values.")
    except sqlite3.IntegrityError:
        print("This roll number/ID already exists.")

def view_students(connection):
    rows = connection.execute(
        "SELECT id, name, age, marks FROM students ORDER BY id"
    ).fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No student records found.")

def update_student(connection):
    try:
        student_id = int(input("Roll number/ID to update: "))
        marks = float(input("New marks: "))
        cursor = connection.execute(
            "UPDATE students SET marks = ? WHERE id = ?", (marks, student_id)
        )
        connection.commit()
        print("Student updated." if cursor.rowcount else "Student not found.")
    except ValueError:
        print("Enter valid numeric values.")

def delete_student(connection):
    try:
        student_id = int(input("Roll number/ID to delete: "))
        cursor = connection.execute("DELETE FROM students WHERE id = ?", (student_id,))
        connection.commit()
        print("Student deleted." if cursor.rowcount else "Student not found.")
    except ValueError:
        print("Roll number/ID must be numeric.")

connection = None
try:
    connection = connect_db()
    while True:
        print("\n--- STUDENT MANAGEMENT ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student Marks")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_student(connection)
        elif choice == "2":
            view_students(connection)
        elif choice == "3":
            update_student(connection)
        elif choice == "4":
            delete_student(connection)
        elif choice == "5":
            print("Thank you. Program ended.")
            break
        else:
            print("Invalid choice.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection:
        connection.close()
