import re


text = input("Enter a sentence: ")
words = re.findall(r"\b\w+\b", text.casefold())
frequencies = {}

for word in words:
    frequencies[word] = frequencies.get(word, 0) + 1

if frequencies:
    most_common = max(frequencies, key=frequencies.get)
    print("Most repeated word:", most_common)
    print("Frequency:", frequencies[most_common])
else:
    print("No words found.")
