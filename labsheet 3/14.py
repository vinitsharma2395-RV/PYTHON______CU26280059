import string


text = input("Enter a string: ")
result = ""

for character in text:
    if character not in string.punctuation:
        result += character

print("String without punctuation:", result)
