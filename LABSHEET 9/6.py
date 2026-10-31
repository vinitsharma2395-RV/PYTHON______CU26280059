# Q6: CRUD operations on a dictionary of employee data
employees = {
    1: {"name": "Ravi", "department": "IT", "salary": 30000},
    2: {"name": "Neha", "department": "HR", "salary": 35000}
}

while True:
    print("\n1. Add  2. View  3. Update  4. Delete  5. Exit")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        try:
            emp_id = int(input("Employee ID: "))
            if emp_id in employees:
                print("Employee ID already exists.")
                continue
            name = input("Name: ").strip()
            department = input("Department: ").strip()
            salary = float(input("Salary: "))
            employees[emp_id] = {"name": name, "department": department, "salary": salary}
            print("Employee added.")
        except ValueError:
            print("Enter a valid ID and salary.")
    elif choice == "2":
        if employees:
            for emp_id, details in employees.items():
                print(emp_id, details)
        else:
            print("No employee records.")
    elif choice == "3":
        try:
            emp_id = int(input("Employee ID to update: "))
            if emp_id in employees:
                employees[emp_id]["name"] = input("New name: ").strip()
                employees[emp_id]["department"] = input("New department: ").strip()
                employees[emp_id]["salary"] = float(input("New salary: "))
                print("Employee updated.")
            else:
                print("Employee not found.")
        except ValueError:
            print("Enter a valid ID and salary.")
    elif choice == "4":
        try:
            emp_id = int(input("Employee ID to delete: "))
            if employees.pop(emp_id, None) is not None:
                print("Employee deleted.")
            else:
                print("Employee not found.")
        except ValueError:
            print("Enter a valid employee ID.")
    elif choice == "5":
        print("Program ended.")
        break
    else:
        print("Invalid choice.")
