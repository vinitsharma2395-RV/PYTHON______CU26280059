text = input("Enter a string: ")
frequencies = {}

for character in text:
    frequencies[character] = frequencies.get(character, 0) + 1

for character in text:
    if frequencies[character] == 1:
        print("First non-repeated character:", character)
        break
else:
    print("There is no non-repeated character.")
