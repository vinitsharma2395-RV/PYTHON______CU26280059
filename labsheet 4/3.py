numbers = [int(value) for value in input("Enter numbers separated by spaces: ").split()]
non_negative_numbers = []

for number in numbers:
    if number >= 0:
        non_negative_numbers.append(number)

print("List without negative numbers:", non_negative_numbers)
