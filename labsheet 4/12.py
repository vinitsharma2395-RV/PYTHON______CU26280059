student_count = int(input("How many students? "))
students = {}

for _ in range(student_count):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    students[name] = marks

if students:
    print("Maximum marks:", max(students.values()))
    print("Minimum marks:", min(students.values()))
else:
    print("No student marks were entered.")
