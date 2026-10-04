student_count = int(input("How many students? "))
students = {}

for _ in range(student_count):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    students[name] = marks

print("Student marks:", students)
