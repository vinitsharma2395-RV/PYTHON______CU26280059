text = input("Enter a string: ")

# Convert ASCII letters manually without using the title() method.
title_case = ""
start_of_word = True

for character in text:
    if character == " ":
        title_case += character
        start_of_word = True
    elif "a" <= character <= "z":
        if start_of_word:
            title_case += chr(ord(character) - 32)
        else:
            title_case += character
        start_of_word = False
    elif "A" <= character <= "Z":
        if start_of_word:
            title_case += character
        else:
            title_case += chr(ord(character) + 32)
        start_of_word = False
    else:
        title_case += character
        start_of_word = False

print("Title case:", title_case)
