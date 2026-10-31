# Q10: CRUD operations on student records stored in a text file
from pathlib import Path

file_path = Path(__file__).with_name("student_records.txt")

def read_records():
    records = []
    if file_path.exists():
        with file_path.open("r", encoding="utf-8") as file:
            for line in file:
                parts = line.rstrip("\r\n").split(",", 2)
                if len(parts) == 3:
                    records.append({"roll": parts[0], "name": parts[1], "marks": parts[2]})
    return records

def save_records(records):
    with file_path.open("w", encoding="utf-8") as file:
        for record in records:
            file.write(f"{record['roll']},{record['name']},{record['marks']}\n")

while True:
    print("\n1. Add  2. View  3. Modify  4. Delete  5. Exit")
    choice = input("Choose an option: ").strip()

    try:
        records = read_records()

        if choice == "1":
            roll = input("Roll number: ").strip()
            if any(r["roll"] == roll for r in records):
                print("Roll number already exists.")
                continue
            name = input("Name: ").strip().replace(",", " ")
            marks = input("Marks: ").strip()
            records.append({"roll": roll, "name": name, "marks": marks})
            save_records(records)
            print("Record added.")
        elif choice == "2":
            if records:
                for record in records:
                    print(record)
            else:
                print("No records found.")
        elif choice == "3":
            roll = input("Roll number to modify: ").strip()
            for record in records:
                if record["roll"] == roll:
                    record["name"] = input("New name: ").strip().replace(",", " ")
                    record["marks"] = input("New marks: ").strip()
                    save_records(records)
                    print("Record modified.")
                    break
            else:
                print("Record not found.")
        elif choice == "4":
            roll = input("Roll number to delete: ").strip()
            updated = [r for r in records if r["roll"] != roll]
            if len(updated) == len(records):
                print("Record not found.")
            else:
                save_records(updated)
                print("Record deleted.")
        elif choice == "5":
            print("Program ended.")
            break
        else:
            print("Invalid choice.")
    except OSError as error:
        print("File error:", error)
