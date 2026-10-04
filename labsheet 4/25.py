import re


paragraph = input("Enter a paragraph: ")
words = re.findall(r"\b\w+\b", paragraph.casefold())
frequencies = {}

for word in words:
    frequencies[word] = frequencies.get(word, 0) + 1

print("Word frequencies:", frequencies)
