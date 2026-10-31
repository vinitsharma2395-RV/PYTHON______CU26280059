from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent

# Write multiple lines entered by the user; enter END to finish
lines = []
print("Enter lines (type END to finish):")
while True:
    line = input()
    if line.upper() == "END":
        break
    lines.append(line)
with open(DATA_DIR / "user_lines.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(lines))
print("Saved", len(lines), "line(s) in user_lines.txt")
