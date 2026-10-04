student_count = int(input("How many students? "))
students = {}

for number in range(1, student_count + 1):
    print("Enter details for student", number)
    name = input("Name: ")
    roll = input("Roll: ")
    marks = float(input("Marks: "))
    students[roll] = {"Name": name, "Roll": roll, "Marks": marks}

print("Student details:", students)
