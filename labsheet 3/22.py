numbers = [int(value) for value in input("Enter integers separated by spaces: ").split()]

print("Ascending:", sorted(numbers))
print("Descending:", sorted(numbers, reverse=True))
