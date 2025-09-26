import pandas as pd
from PyQt6.QtWidgets import QMainWindow, QPushButton, QTableView, QVBoxLayout, QWidget

from src.dataframe_model import DataFrameModel


class DataFrameWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Load pandas DataFrame as a model")
        self.setGeometry(100, 100, 800, 600)

        self.table_data = pd.read_csv("data.csv")

        self.model = DataFrameModel(self.table_data)

        self.setup_ui()

    def setup_ui(self) -> None:
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout_vertical = QVBoxLayout()
        central_widget.setLayout(layout_vertical)

        self.filter_button = QPushButton("Filter")
        self.filter_button.clicked.connect(self.model.filter_data)

        layout_vertical.addWidget(self.filter_button)

        self.table_view = QTableView()
        self.table_view.setModel(self.model)
        layout_vertical.addWidget(self.table_view)
