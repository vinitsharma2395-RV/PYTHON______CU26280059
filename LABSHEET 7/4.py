from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent

# Count words in a text file
(DATA_DIR / "sample.txt").write_text("Python is simple and Python is useful.", encoding="utf-8")
words = (DATA_DIR / "sample.txt").read_text(encoding="utf-8").split()
print("Total words:", len(words))
