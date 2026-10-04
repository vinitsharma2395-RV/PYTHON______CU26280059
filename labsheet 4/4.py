numbers = [int(value) for value in input("Enter numbers separated by spaces: ").split()]
product = 1

for number in numbers:
    product *= number

print("Product:", product)
