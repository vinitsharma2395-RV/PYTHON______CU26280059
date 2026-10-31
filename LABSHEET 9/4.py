# Q4: Update a student's marks in a list
students = [
    {"roll": 101, "name": "Rahul", "marks": 85},
    {"roll": 102, "name": "Aman", "marks": 90},
    {"roll": 103, "name": "Vinit", "marks": 95}
]

try:
    roll_no = int(input("Enter roll number: "))
    new_marks = float(input("Enter new marks: "))
    for student in students:
        if student["roll"] == roll_no:
            student["marks"] = new_marks
            print("Marks updated successfully.")
            print(student)
            break
    else:
        print("Student not found.")
except ValueError:
    print("Please enter a valid number.")
