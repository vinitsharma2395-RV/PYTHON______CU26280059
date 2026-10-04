text = input("Enter a string: ")
frequencies = {}

for character in text:
    frequencies[character] = frequencies.get(character, 0) + 1

print("Character frequencies:", frequencies)
