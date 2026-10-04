item_count = int(input("How many dictionary items? "))
dictionary = {}

for _ in range(item_count):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dictionary[key] = value

key_to_find = input("Enter the key to check: ")
if key_to_find in dictionary:
    print("The key exists in the dictionary.")
else:
    print("The key does not exist in the dictionary.")
