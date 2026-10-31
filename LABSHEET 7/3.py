from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent

# Read a file one line at a time
(DATA_DIR / "sample.txt").write_text("First line\nSecond line\nThird line", encoding="utf-8")
with open(DATA_DIR / "sample.txt", "r", encoding="utf-8") as file:
    for line_no, line in enumerate(file, start=1):
        print(f"Line {line_no}: {line.rstrip()}")
