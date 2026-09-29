print("Vinit Sharma")

def roman_to_number(roman):
    values = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }

    roman = roman.upper()
    total = 0

    for i in range(len(roman)):
        if i + 1 < len(roman) and values[roman[i]] < values[roman[i + 1]]:
            total -= values[roman[i]]
        else:
            total += values[roman[i]]

    return total


roman = input("Enter a Roman number: ")
print("Ordinary number:", roman_to_number(roman))