first = [int(value) for value in input("Enter the first list of integers: ").split()]
second = [int(value) for value in input("Enter the second list of integers: ").split()]
common = []

for number in first:
    if number in second and number not in common:
        common.append(number)

print("Common elements:", common)
