item_count = int(input("How many dictionary items? "))
dictionary = {}

for _ in range(item_count):
    key = input("Enter key: ")
    value = float(input("Enter numeric value: "))
    dictionary[key] = value

if dictionary:
    maximum_key = max(dictionary, key=dictionary.get)
    print("Key with the maximum value:", maximum_key)
    print("Maximum value:", dictionary[maximum_key])
else:
    print("The dictionary is empty.")
