import sqlite3
from models import LiteraryFormat


class LiteraryFormatManager:
    def __init__(self):
        # створюємо один раз підключеня к БД під час створеня
        self._connection = sqlite3.connect("library_db.db3")
        # щоб не міняти багато де назву якщо буде зміна імя
        self.table_name = "literary_formats"

    def create(self, format_: str):
        self._connection.execute(
            f"INSERT INTO {self.table_name} (format) VALUES (?)",
            (format_,)
        )
        # підтвердити зміни
        self._connection.commit()

    def delete(self, id_to_delete: int):
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = ?",
            (id_to_delete,)
        )
        self._connection.commit()

    def all(self) -> None:
        literary_formats_cursor = self._connection.execute(
            f"SELECT id, format  FROM {self.table_name}"
        )
        print(literary_formats_cursor)  # <sqlite3.Cursor object at 0x0000019C49A5E9C0>
        for row in literary_formats_cursor:
            print(LiteraryFormat(*row))
            # LiteraryFormat(id='lyrics', format=1)
            # LiteraryFormat(id='poema', format=3)

    def update(self, id_to_update: int, new_format: str):
        self._connection.execute(
            f"UPDATE {self.table_name} "
            "SET format = ? "
            "WHERE id = ?",
            (new_format, id_to_update)
        )
        self._connection.commit()


# Тут все взаємодіє з LF а не з LFM, потрібно змінити
# зробимо через main, якщо створювати LFM в LF то буде циклічний імпорт
# перенесли логіку в main
# P.S: в django ця проблема вирішується магією

# if __name__ == '__main__':
#     manager = LiteraryFormatManager()
#     manager.create("drama")  # +
#     manager.update(7, "kek")  # +
#     manager.delete(10)
#     manager.all()

