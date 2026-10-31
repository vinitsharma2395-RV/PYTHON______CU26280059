from db_helper import connect_db
# Use functions to insert and fetch student records
def insert_student(name, age, marks):
    with connect_db() as con:
        con.execute("INSERT INTO students(name, age, marks) VALUES (?, ?, ?)", (name, age, marks))
def fetch_students():
    with connect_db() as con:
        return con.execute("SELECT * FROM students ORDER BY id").fetchall()
insert_student("Sana", 20, 87)
print("Student records:")
for student in fetch_students(): print(student)
