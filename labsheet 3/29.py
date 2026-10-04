first = [int(value) for value in input("Enter the first list of integers: ").split()]
second = [int(value) for value in input("Enter the second list of integers: ").split()]
difference = []

for number in first:
    if number not in second and number not in difference:
        difference.append(number)

print("Elements in the first list but not the second:", difference)
