item_count = int(input("How many dictionary items? "))
dictionary = {}

for _ in range(item_count):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dictionary[key] = value

key_to_remove = input("Enter the key to remove: ")
if key_to_remove in dictionary:
    del dictionary[key_to_remove]
    print("Updated dictionary:", dictionary)
else:
    print("Key not found.")
