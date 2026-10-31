"""Shared SQLite helpers for the Lab Sheet 8 exercises."""

import sqlite3
from pathlib import Path


DB_PATH = Path(__file__).resolve().with_name("student_db.db")
DATA_DIR = Path(__file__).resolve().parent


def connect_db():
    """Return a connection to the database stored beside this file."""
    return sqlite3.connect(DB_PATH)


def setup_students():
    """Create the students table and add examples when it is empty."""
    with connect_db() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                marks REAL NOT NULL
            )
            """
        )
        total = connection.execute("SELECT COUNT(*) FROM students").fetchone()[0]
        if total == 0:
            connection.executemany(
                "INSERT INTO students (name, age, marks) VALUES (?, ?, ?)",
                [
                    ("Aman", 20, 85),
                    ("Riya", 21, 92),
                    ("Karan", 19, 78),
                    ("Neha", 20, 35),
                ],
            )


if __name__ == "__main__":
    setup_students()
    print(f"Database ready: {DB_PATH.name}")
