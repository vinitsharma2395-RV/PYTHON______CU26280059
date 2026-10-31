from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent

# Display first and last lines
(DATA_DIR / "sample.txt").write_text("First line\nMiddle line\nLast line", encoding="utf-8")
lines = (DATA_DIR / "sample.txt").read_text(encoding="utf-8").splitlines()
if lines:
    print("First line:", lines[0])
    print("Last line:", lines[-1])
else:
    print("File is empty.")
