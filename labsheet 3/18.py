text = input("Enter a string: ")
sorted_text = "".join(sorted(text, key=str.casefold))

print("Characters in alphabetical order:", sorted_text)
