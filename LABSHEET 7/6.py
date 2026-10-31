from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent

# Display even-numbered lines (2, 4, 6, ...)
(DATA_DIR / "sample.txt").write_text("One\nTwo\nThree\nFour\nFive\nSix", encoding="utf-8")
with open(DATA_DIR / "sample.txt", encoding="utf-8") as file:
    for number, line in enumerate(file, start=1):
        if number % 2 == 0:
            print(f"Line {number}: {line.rstrip()}")
