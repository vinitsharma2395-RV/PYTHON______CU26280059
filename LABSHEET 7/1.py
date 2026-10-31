from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent

# Create a text file and write content
(DATA_DIR / "sample.txt").write_text(
    "Welcome to Python File Handling!\nThis is Lab Sheet 07.", encoding="utf-8"
)
print("File created and content written successfully.")
print((DATA_DIR / "sample.txt").read_text(encoding="utf-8"))
