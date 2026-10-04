numbers = [int(value) for value in input("Enter integers separated by spaces: ").split()]

if numbers:
    largest = numbers[0]
    smallest = numbers[0]

    for number in numbers[1:]:
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number

    print("Largest:", largest)
    print("Smallest:", smallest)
else:
    print("The list is empty.")
