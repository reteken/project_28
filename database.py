import sqlite3
from datetime import datetime


def init_db():
    conn = sqlite3.connect("mushrooms.db")
    c = conn.cursor()
    c.execute(
        """CREATE TABLE IF NOT EXISTS mushrooms
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT,
                  image_path TEXT,
                  date TEXT)"""
    )
    conn.commit()
    conn.close()


def save_mushroom(name, image_path):
    conn = sqlite3.connect("mushrooms.db")
    c = conn.cursor()
    c.execute(
        "INSERT INTO mushrooms (name, image_path, date) VALUES (?, ?, ?)",
        (name, image_path, datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
    )
    conn.commit()
    conn.close()


def get_mushrooms():
    conn = sqlite3.connect("mushrooms.db")
    c = conn.cursor()
    c.execute("SELECT * FROM mushrooms")
    rows = c.fetchall()
    conn.close()
    return rows


def delete_mushroom(mushroom_id):
    conn = sqlite3.connect("mushrooms.db")
    c = conn.cursor()
    c.execute("DELETE FROM mushrooms WHERE id = ?", (mushroom_id,))
    conn.commit()
    conn.close()
