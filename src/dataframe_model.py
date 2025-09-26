from typing import Any, override

import pandas as pd
from PyQt6.QtCore import QAbstractTableModel, QModelIndex, Qt


class DataFrameModel(QAbstractTableModel):
    def __init__(self, table_data: pd.DataFrame):
        super().__init__()
        self.table_data = table_data

    @override
    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:
        return self.table_data.shape[0]

    @override
    def columnCount(self, parent: QModelIndex = QModelIndex()) -> int:
        return self.table_data.shape[1]

    @override
    def data(self, index: QModelIndex, role: int = Qt.ItemDataRole.DisplayRole) -> Any:
        if not index.isValid():
            return None

        if index.row() >= self.table_data.shape[0] or index.column() >= self.table_data.shape[1]:
            return None

        if role == Qt.ItemDataRole.DisplayRole:
            return f"{self.table_data.iloc[index.row(), index.column()]:.2f}"
        return None
