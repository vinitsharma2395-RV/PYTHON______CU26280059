text = input("Enter a string: ")

unique_characters = ""
for character in text:
    if character not in unique_characters:
        unique_characters += character

print("String without duplicate characters:", unique_characters)
