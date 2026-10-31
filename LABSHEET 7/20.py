from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent

# Merge two text files into a third file
(DATA_DIR / "first.txt").write_text(
    "Content of first file.\n", encoding="utf-8"
)
(DATA_DIR / "second.txt").write_text(
    "Content of second file.\n", encoding="utf-8"
)
first_content = (DATA_DIR / "first.txt").read_text(encoding="utf-8")
second_content = (DATA_DIR / "second.txt").read_text(encoding="utf-8")
merged = first_content + second_content
(DATA_DIR / "merged.txt").write_text(merged, encoding="utf-8")
print((DATA_DIR / "merged.txt").read_text(encoding="utf-8"))
