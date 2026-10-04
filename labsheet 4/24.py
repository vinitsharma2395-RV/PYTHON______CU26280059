item_count = int(input("How many dictionary items? "))
dictionary = {}

for _ in range(item_count):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dictionary[key] = value

inverted_dictionary = {}
for key, value in dictionary.items():
    inverted_dictionary[value] = key

print("Inverted dictionary:", inverted_dictionary)
