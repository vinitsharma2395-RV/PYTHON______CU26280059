item_count = int(input("How many dictionary items? "))
dictionary = {}

for _ in range(item_count):
    key = input("Enter key: ")
    value = float(input("Enter numeric value: "))
    dictionary[key] = value

sorted_dictionary = dict(sorted(dictionary.items(), key=lambda item: item[1]))
print("Dictionary sorted by values:", sorted_dictionary)
