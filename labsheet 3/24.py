numbers = [int(value) for value in input("Enter integers separated by spaces: ").split()]
left = 0
right = len(numbers) - 1

while left < right:
    numbers[left], numbers[right] = numbers[right], numbers[left]
    left += 1
    right -= 1

print("Reversed list:", numbers)
