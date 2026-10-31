import re
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent

# Search for a word in a text file
(DATA_DIR / "sample.txt").write_text("Python is easy. File handling is useful.", encoding="utf-8")
word = input("Enter word to search: ").strip()
content = (DATA_DIR / "sample.txt").read_text(encoding="utf-8")
if word and re.search(rf"\b{re.escape(word)}\b", content, re.IGNORECASE):
    print(f"'{word}' found in the file.")
else:
    print(f"'{word}' not found in the file.")
