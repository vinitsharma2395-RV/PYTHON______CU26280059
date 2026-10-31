from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent

# Remove blank lines and save cleaned content
path = (DATA_DIR / "sample.txt")
path.write_text("First line\n\nSecond line\n   \nThird line", encoding="utf-8")
lines = path.read_text(encoding="utf-8").splitlines()
clean_lines = [line for line in lines if line.strip()]
path.write_text("\n".join(clean_lines), encoding="utf-8")
print(path.read_text(encoding="utf-8"))
