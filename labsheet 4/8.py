numbers = [int(value) for value in input("Enter numbers separated by spaces: ").split()]
target_sum = int(input("Enter the target sum: "))
pairs = []

for first_index in range(len(numbers)):
    for second_index in range(first_index + 1, len(numbers)):
        if numbers[first_index] + numbers[second_index] == target_sum:
            pairs.append((numbers[first_index], numbers[second_index]))

print("Pairs:", pairs)
