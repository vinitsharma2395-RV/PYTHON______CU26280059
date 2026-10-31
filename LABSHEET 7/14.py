from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent

# Find the longest line in a text file
(DATA_DIR / "sample.txt").write_text(
    "Short line.\nThis is the longest line in this sample file.\nEnd.",
    encoding="utf-8",
)
lines = (DATA_DIR / "sample.txt").read_text(encoding="utf-8").splitlines()
if lines:
    longest = max(lines, key=len)
    print("Longest line:", longest)
    print("Length:", len(longest))
else:
    print("File is empty.")
