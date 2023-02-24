# для взаимодействия с БД через классы в modules.py

import sqlite3
from models import LiteraryFormat


class LiteraryFormatManager:
    # в django_orm не будем подключаться для каждого менеджера отдельно, но в этом
    # примере для удобства сделаем

    def __init__(self):
        # "открытие" бд как файла
        # в sqllite не нужно вводить логин/пароль, работаем с db3 как с файлом
        # подключение к удаленной БД может занимать некоторое время
        self._connection = sqlite3.connect("library_db.db3")
        # без этого при смене имени приходилось бы много где менять
        self.table_name = "literary_formats"

    # CREATE
    def create(self, format_: str):
        # ставим ? вместо format_ чтобы избежать sqli
        self._connection.execute(
            f"INSERT INTO {self.table_name} (format) VALUES (?)",
            (format_,)
        )  # подготовили данные для добавления
        self._connection.commit()  # загрузили их в БД

    # READ
    def all(self):
        lf_cursor = self._connection.execute(
            # f"SELECT * FROM {self.table_name}"  # так будет путаться вывод id/format, но в БД сохр. корректно
            f"SELECT id, format FROM {self.table_name}"  # тут все ок
        )
        # print(lf_cursor)  # <sqlite3.Cursor object at 0x0000019BB58B4DC0>
        # for row in lf_cursor:
        #     print(row)  # ('lyrics', 1) ('poema', 2)

        return [LiteraryFormat(*row) for row in lf_cursor]

    # UPDATE
    def update(self, id_to_update: int, new_format: str):
        self._connection.execute(
            f"UPDATE {self.table_name} "
            "SET format = ? "
            "WHERE id = ? ",
            (new_format, id_to_update)
        )
        self._connection.commit()

    # DELETE
    def delete(self, id_to_delete: int):
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            "WHERE id = ?",
            f"{id_to_delete}"
        )
        self._connection.commit()
