item_count = int(input("How many dictionary items? "))
dictionary = {}

for _ in range(item_count):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dictionary[key] = value

key_to_update = input("Enter the key to update: ")
if key_to_update in dictionary:
    dictionary[key_to_update] = input("Enter the new value: ")
    print("Updated dictionary:", dictionary)
else:
    print("Key not found.")
