from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent

# Read numeric values and calculate sum and average
(DATA_DIR / "numbers.txt").write_text("10\n20\n30\n40", encoding="utf-8")
try:
    numbers = [
        float(value)
        for value in (DATA_DIR / "numbers.txt").read_text(encoding="utf-8").split()
    ]
    print("Numbers:", numbers)
    print("Sum:", sum(numbers))
    print("Average:", sum(numbers) / len(numbers) if numbers else 0)
except ValueError:
    print("The file contains an invalid number.")
