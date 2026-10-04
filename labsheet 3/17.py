text = input("Enter a string: ")

print("Substrings:")
for start in range(len(text)):
    for end in range(start + 1, len(text) + 1):
        print(text[start:end])
