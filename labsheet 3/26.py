first = [int(value) for value in input("Enter the first list of integers: ").split()]
second = [int(value) for value in input("Enter the second list of integers: ").split()]

merged = first + second
print("Merged list:", merged)
