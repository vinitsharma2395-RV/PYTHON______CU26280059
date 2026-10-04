item_count = int(input("How many dictionary items? "))
dictionary = {}

for _ in range(item_count):
    key = input("Enter key: ")
    value = float(input("Enter numeric value: "))
    dictionary[key] = value

print("Sum of values:", sum(dictionary.values()))
