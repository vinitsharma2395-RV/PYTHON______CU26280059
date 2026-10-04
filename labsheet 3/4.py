text = input("Enter a string: ")

uppercase_characters = ""
for character in text:
    if character.isupper():
        uppercase_characters += character

print("Uppercase characters:", uppercase_characters)
