from typing import Any, override

from PyQt6.QtCore import QAbstractListModel, QModelIndex, Qt
from PyQt6.QtGui import QColor, QFont

type ToDo = tuple[str, bool]

TODO_DEFAULT_ITEMS: list[ToDo] = [
    ("Faire les courses", False),
    ("Aller au cinéma", False),
    ("Faire le menage", True),
    ("Faire le cuisine", False),
    ("Faire le lit", True),
    ("Faire le sport", False),
]


class TodoModel(QAbstractListModel):
    def __init__(self, todos: list[ToDo] | None = None) -> None:
        super().__init__()
        self.todos = todos or TODO_DEFAULT_ITEMS

    @override
    def rowCount(self, parent: QModelIndex | None = None) -> int:
        return len(self.todos)

    @override
    def columnCount(self, parent: QModelIndex | None = None) -> int:
        return 1

    @override
    def data(self, index: QModelIndex, role: int = Qt.ItemDataRole.DisplayRole) -> Any:
        if index.isValid() is False:
            return

        todo_text, is_done = self.todos[index.row()]

        if role == Qt.ItemDataRole.DisplayRole:
            done_status = "DONE" if is_done is True else "TODO"

            return f"{todo_text}  --  {done_status}"

        if role == Qt.ItemDataRole.ForegroundRole:
            return QColor(Qt.GlobalColor.darkGreen if is_done else Qt.GlobalColor.black)

        if role == Qt.ItemDataRole.FontRole:
            font = QFont()
            if is_done is False:
                font.setBold(True)
            return font

        return

    def add_todo(self, text: str) -> None:
        if (todo_text := text.strip()) == "":
            return

        row = len(self.todos)

        self.beginInsertRows(QModelIndex(), row, row)

        self.todos.append((todo_text, False))

        self.endInsertRows()

    def is_row_valid(self, row: int) -> bool:
        return 0 <= row < len(self.todos)

    def remove_todo(self, row: int) -> None:
        if self.is_row_valid(row) is False:
            return

        self.beginInsertRows(QModelIndex(), row, row)

        self.todos.pop(row)

        self.endInsertRows()

    def toggle_todo(self, row: int) -> None:
        if self.is_row_valid(row) is False:
            return

        todo_text, is_done = self.todos[row]
        self.todos[row] = (todo_text, not is_done)

        index = self.index(row, 0)
        self.dataChanged.emit(index, index)
