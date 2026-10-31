from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent

# Append content without deleting existing content
path = (DATA_DIR / "notes.txt")
if not path.exists():
    path.write_text("Existing note.\n", encoding="utf-8")
new_text = input("Enter content to append: ")
with open(path, "a", encoding="utf-8") as file:
    file.write(new_text + "\n")
print("Updated file:\n", path.read_text(encoding="utf-8"))
