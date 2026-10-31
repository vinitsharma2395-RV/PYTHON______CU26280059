from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent

# Replace one word with another and save the file
path = (DATA_DIR / "sample.txt")
path.write_text("I like Java. Java is popular.", encoding="utf-8")
old = input("Word to replace: ")
new = input("New word: ")
content = path.read_text(encoding="utf-8")
if old:
    path.write_text(content.replace(old, new), encoding="utf-8")
print("Updated content:", path.read_text(encoding="utf-8"))
