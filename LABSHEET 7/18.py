from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent

# Store unique words in another file, preserving first appearance
(DATA_DIR / "source.txt").write_text("apple banana apple mango banana orange", encoding="utf-8")
words = (DATA_DIR / "source.txt").read_text(encoding="utf-8").split()
unique = list(dict.fromkeys(words))
(DATA_DIR / "unique_words.txt").write_text("\n".join(unique), encoding="utf-8")
print("Unique words:", unique)
print("Saved in unique_words.txt")
