numbers = [int(value) for value in input("Enter integers separated by spaces: ").split()]
unique_numbers = sorted(set(numbers))

if len(unique_numbers) >= 2:
    print("Second largest number:", unique_numbers[-2])
else:
    print("At least two distinct numbers are required.")
