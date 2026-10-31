# Q2: Display all student records from a list
students = [
    {"roll": 101, "name": "Rahul", "marks": 85},
    {"roll": 102, "name": "Aman", "marks": 90},
    {"roll": 103, "name": "Vinit", "marks": 95}
]

print("All Student Records")
for student in students:
    print(f"Roll: {student['roll']}, Name: {student['name']}, Marks: {student['marks']}")
