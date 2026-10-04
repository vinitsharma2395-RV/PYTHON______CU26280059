first = input("Enter the first string: ")
second = input("Enter the second string: ")

first_normalized = "".join(first.lower().split())
second_normalized = "".join(second.lower().split())

if sorted(first_normalized) == sorted(second_normalized):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
