from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent

# Read content and display it in uppercase
(DATA_DIR / "sample.txt").write_text("Python File Handling", encoding="utf-8")
content = (DATA_DIR / "sample.txt").read_text(encoding="utf-8")
print(content.upper())
