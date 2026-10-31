from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent

# Count lines and characters in a file
(DATA_DIR / "sample.txt").write_text("Hello Python\nFile Handling", encoding="utf-8")
content = (DATA_DIR / "sample.txt").read_text(encoding="utf-8")
print("Lines:", len(content.splitlines()))
print("Characters:", len(content))
