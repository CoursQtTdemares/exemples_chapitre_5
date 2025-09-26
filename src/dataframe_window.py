import pandas as pd
from PyQt6.QtWidgets import QMainWindow, QTableView

from src.dataframe_model import DataFrameModel


class DataFrameWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Load pandas DataFrame as a model")
        self.setGeometry(100, 100, 800, 600)

        self.table_data = pd.read_csv("data.csv")

        self.model = DataFrameModel(self.table_data)
        self.table_view = QTableView()
        self.table_view.setModel(self.model)

        self.setCentralWidget(self.table_view)
