from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent

# Sort words alphabetically and save them in a new file
(DATA_DIR / "source.txt").write_text("mango apple banana orange", encoding="utf-8")
words = (DATA_DIR / "source.txt").read_text(encoding="utf-8").split()
sorted_words = sorted(words, key=str.lower)
(DATA_DIR / "sorted_words.txt").write_text("\n".join(sorted_words), encoding="utf-8")
print("Sorted words:", sorted_words)
