numbers = [int(value) for value in input("Enter numbers separated by spaces: ").split()]
middle = len(numbers) // 2

first_half = numbers[:middle]
second_half = numbers[middle:]

print("First half:", first_half)
print("Second half:", second_half)
