# Q8: Store and manage product details using CRUD operations
products = [
    {"id": 1, "name": "Notebook", "price": 50.0, "quantity": 20},
    {"id": 2, "name": "Pen", "price": 10.0, "quantity": 100}
]

while True:
    print("\n1. Add  2. View  3. Update  4. Delete  5. Exit")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        try:
            product_id = int(input("Product ID: "))
            if any(p["id"] == product_id for p in products):
                print("Product ID already exists.")
                continue
            name = input("Product name: ").strip()
            price = float(input("Price: "))
            quantity = int(input("Quantity: "))
            products.append({"id": product_id, "name": name, "price": price, "quantity": quantity})
            print("Product added.")
        except ValueError:
            print("Enter valid numeric values.")
    elif choice == "2":
        for product in products:
            print(product)
        if not products:
            print("No products available.")
    elif choice == "3":
        try:
            product_id = int(input("Product ID to update: "))
            for product in products:
                if product["id"] == product_id:
                    product["name"] = input("New name: ").strip()
                    product["price"] = float(input("New price: "))
                    product["quantity"] = int(input("New quantity: "))
                    print("Product updated.")
                    break
            else:
                print("Product not found.")
        except ValueError:
            print("Enter valid numeric values.")
    elif choice == "4":
        try:
            product_id = int(input("Product ID to delete: "))
            for product in products:
                if product["id"] == product_id:
                    products.remove(product)
                    print("Product deleted.")
                    break
            else:
                print("Product not found.")
        except ValueError:
            print("Product ID must be a number.")
    elif choice == "5":
        break
    else:
        print("Invalid choice.")
