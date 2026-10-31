# Q9: Save student data into a text file and read it back
from pathlib import Path

file_path = Path(__file__).with_name("students.txt")

try:
    name = input("Enter student name: ").strip().replace(",", " ")
    roll = input("Enter roll number: ").strip()
    marks = input("Enter marks: ").strip()

    with file_path.open("a", encoding="utf-8") as file:
        file.write(f"{roll},{name},{marks}\n")

    print("\nStudent data saved. File contents:")
    with file_path.open("r", encoding="utf-8") as file:
        print(file.read())
except OSError as error:
    print("File error:", error)
