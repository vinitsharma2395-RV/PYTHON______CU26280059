from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent

# Read the complete content of a text file
(DATA_DIR / "sample.txt").write_text(
    "Python makes file handling easy.\nWe are learning read operations.",
    encoding="utf-8",
)
try:
    print((DATA_DIR / "sample.txt").read_text(encoding="utf-8"))
except FileNotFoundError:
    print("File not found.")
