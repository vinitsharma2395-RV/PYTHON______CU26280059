from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent

# Count occurrences of a word (case-insensitive)
(DATA_DIR / "sample.txt").write_text("Python python PYTHON is popular.", encoding="utf-8")
word = input("Enter word: ").strip().lower()
words = (DATA_DIR / "sample.txt").read_text(encoding="utf-8").lower().split()
count = sum(item.strip(".,!?;:") == word for item in words)
print("Occurrences:", count)
