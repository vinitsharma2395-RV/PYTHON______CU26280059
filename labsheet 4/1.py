numbers = [int(value) for value in input("Enter numbers separated by spaces: ").split()]

total = sum(numbers)
average = total / len(numbers) if numbers else 0

print("Sum:", total)
print("Average:", average)
