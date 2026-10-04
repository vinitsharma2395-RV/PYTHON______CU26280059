numbers = [int(value) for value in input("Enter numbers separated by spaces: ").split()]
positions = int(input("Rotate right by how many positions? "))

if numbers:
    positions %= len(numbers)
    if positions:
        numbers = numbers[-positions:] + numbers[:-positions]

print("Rotated list:", numbers)
