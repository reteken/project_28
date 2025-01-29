import sqlite3
from datetime import datetime


def init_db():
    """Инициализация базы данных и обновление структуры таблицы."""
    conn = sqlite3.connect("mushrooms.db")
    cursor = conn.cursor()

    # Создаём таблицу, если её нет
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS mushroom_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            image_path TEXT NOT NULL,
            scan_date TEXT NOT NULL
        )
    """
    )

    # Проверяем, есть ли столбец `image_path`
    cursor.execute("PRAGMA table_info(mushroom_history)")
    columns = [column[1] for column in cursor.fetchall()]
    if "image_path" not in columns:
        # Если столбца нет, добавляем его
        cursor.execute(
            "ALTER TABLE mushroom_history ADD COLUMN image_path TEXT NOT NULL DEFAULT ''"
        )

    conn.commit()
    conn.close()


def save_mushroom(name, image_path):
    """Сохраняет информацию о грибе в базу данных."""
    conn = sqlite3.connect("mushrooms.db")
    cursor = conn.cursor()

    # Сохраняем данные в таблицу
    cursor.execute(
        """
        INSERT INTO mushroom_history (name, image_path, scan_date)
        VALUES (?, ?, ?)
    """,
        (name, image_path, datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
    )

    conn.commit()
    conn.close()


def get_saved_mushrooms():
    """Получает список сохранённых грибов из базы данных."""
    conn = sqlite3.connect("mushrooms.db")
    cursor = conn.cursor()

    cursor.execute("SELECT name, image_path, scan_date FROM mushroom_history")
    rows = cursor.fetchall()

    conn.close()

    # Преобразуем данные в список словарей
    return [{"name": row[0], "image_path": row[1], "scan_date": row[2]} for row in rows]


def delete_mushroom(mushroom_id):
    conn = sqlite3.connect("mushrooms.db")
    c = conn.cursor()
    c.execute("DELETE FROM mushrooms WHERE id = ?", (mushroom_id,))
    conn.commit()
    conn.close()
