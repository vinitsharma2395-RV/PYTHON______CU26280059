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

if first_dictionary == second_dictionary:
    print("The dictionaries are equal.")
else:
    print("The dictionaries are not equal.")
