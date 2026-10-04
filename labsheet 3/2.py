text = input("Enter a string: ")

vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for character in text:
    if character.isalpha():
        if character.lower() in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
