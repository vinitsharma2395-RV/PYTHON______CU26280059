text = input("Enter a string: ")

# Ignore spaces and letter case when checking the palindrome.
normalized_text = ""
for character in text:
    if character != " ":
        normalized_text += character.lower()

reversed_text = ""
for character in normalized_text:
    reversed_text = character + reversed_text

if normalized_text == reversed_text:
    print("Palindrome")
else:
    print("Not a palindrome")
