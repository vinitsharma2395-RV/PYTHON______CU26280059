text = input("Enter a string: ")
digits = 0
alphabets = 0
special_characters = 0

for character in text:
    if character.isdigit():
        digits += 1
    elif character.isalpha():
        alphabets += 1
    elif not character.isspace():
        special_characters += 1

print("Digits:", digits)
print("Alphabets:", alphabets)
print("Special characters:", special_characters)
