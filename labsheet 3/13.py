text = input("Enter a string: ")
vowels = "aeiou"
result = ""

for character in text:
    if character.lower() in vowels:
        result += character.upper()
    else:
        result += character.lower()

print("Converted string:", result)
