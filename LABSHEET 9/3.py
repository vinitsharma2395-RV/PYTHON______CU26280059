# Q3: Search for a student by name in a list
students = [
    {"roll": 101, "name": "Rahul", "marks": 85},
    {"roll": 102, "name": "Aman", "marks": 90},
    {"roll": 103, "name": "Vinit", "marks": 95}
]

search_name = input("Enter student name to search: ").strip()
matches = [s for s in students if s["name"].lower() == search_name.lower()]

if matches:
    for student in matches:
        print("Student found:", student)
else:
    print("Student not found.")
