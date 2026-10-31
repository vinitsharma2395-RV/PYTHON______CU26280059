# Q7: Menu-driven CRUD operations on a list of books
books = [
    {"id": 1, "title": "Python Basics", "author": "A. Kumar"},
    {"id": 2, "title": "Database Systems", "author": "R. Sharma"}
]

while True:
    print("\n1. Add  2. View  3. Update  4. Delete  5. Exit")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        try:
            book_id = int(input("Book ID: "))
            if any(book["id"] == book_id for book in books):
                print("Book ID already exists.")
                continue
            title = input("Book title: ").strip()
            author = input("Author: ").strip()
            books.append({"id": book_id, "title": title, "author": author})
            print("Book added.")
        except ValueError:
            print("Book ID must be a number.")
    elif choice == "2":
        for book in books:
            print(book)
        if not books:
            print("No books available.")
    elif choice == "3":
        try:
            book_id = int(input("Book ID to update: "))
            for book in books:
                if book["id"] == book_id:
                    book["title"] = input("New title: ").strip()
                    book["author"] = input("New author: ").strip()
                    print("Book updated.")
                    break
            else:
                print("Book not found.")
        except ValueError:
            print("Book ID must be a number.")
    elif choice == "4":
        try:
            book_id = int(input("Book ID to delete: "))
            for book in books:
                if book["id"] == book_id:
                    books.remove(book)
                    print("Book deleted.")
                    break
            else:
                print("Book not found.")
        except ValueError:
            print("Book ID must be a number.")
    elif choice == "5":
        break
    else:
        print("Invalid choice.")
