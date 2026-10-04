first_count = int(input("How many items in the first dictionary? "))
first_dictionary = {}

for _ in range(first_count):
    key = input("Enter key: ")
    value = input("Enter value: ")
    first_dictionary[key] = value

second_count = int(input("How many items in the second dictionary? "))
second_dictionary = {}

for _ in range(second_count):
    key = input("Enter key: ")
    value = input("Enter value: ")
    second_dictionary[key] = value

common_keys = []
for key in first_dictionary:
    if key in second_dictionary:
        common_keys.append(key)

print("Common keys:", common_keys)
