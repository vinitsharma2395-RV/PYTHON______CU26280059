item_count = int(input("How many dictionary items? "))
dictionary = {}

for _ in range(item_count):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dictionary[key] = value

sorted_dictionary = dict(sorted(dictionary.items()))
print("Dictionary sorted by keys:", sorted_dictionary)
