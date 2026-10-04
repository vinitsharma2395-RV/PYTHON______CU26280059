text = input("Enter a string: ")

words = text.split()
longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

if longest_word:
    print("Longest word:", longest_word)
else:
    print("No words found")
