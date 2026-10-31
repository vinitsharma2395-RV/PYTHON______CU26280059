# Q5: Delete a student record by roll number from a list
students = [
    {"roll": 101, "name": "Rahul", "marks": 85},
    {"roll": 102, "name": "Aman", "marks": 90},
    {"roll": 103, "name": "Vinit", "marks": 95}
]

print("Before deletion:")
for student in students:
    print(student)

try:
    roll_no = int(input("\nEnter roll number to delete: "))
    for student in students:
        if student["roll"] == roll_no:
            students.remove(student)
            print("Student record deleted successfully.")
            break
    else:
        print("Student not found.")

    print("\nAfter deletion:")
    for student in students:
        print(student)
except ValueError:
    print("Please enter a valid roll number.")
