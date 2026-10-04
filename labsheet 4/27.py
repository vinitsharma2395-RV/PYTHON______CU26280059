item_count = int(input("How many dictionary items? "))
dictionary = {}

for _ in range(item_count):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dictionary[key] = value

unique_dictionary = {}
for key, value in dictionary.items():
    if value not in unique_dictionary.values():
        unique_dictionary[key] = value

print("Dictionary without duplicate values:", unique_dictionary)
