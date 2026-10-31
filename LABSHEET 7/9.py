from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent

# Copy content from source file to destination file
(DATA_DIR / "source.txt").write_text(
    "This content will be copied.\nCopy operation in Python.", encoding="utf-8"
)
content = (DATA_DIR / "source.txt").read_text(encoding="utf-8")
(DATA_DIR / "copy.txt").write_text(content, encoding="utf-8")
print("Copied successfully. Destination content:")
print((DATA_DIR / "copy.txt").read_text(encoding="utf-8"))
