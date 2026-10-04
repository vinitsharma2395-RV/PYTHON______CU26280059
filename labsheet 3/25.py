numbers = [int(value) for value in input("Enter integers separated by spaces: ").split()]
frequencies = {}

for number in numbers:
    frequencies[number] = frequencies.get(number, 0) + 1

print("Frequencies:", frequencies)
