text = input("Enter the main string: ")
substring = input("Enter the substring to find: ")

if substring in text:
    print("The substring exists in the string.")
else:
    print("The substring does not exist in the string.")
