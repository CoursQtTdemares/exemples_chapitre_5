import sys

from PyQt6.QtCore import QStringListModel
from PyQt6.QtWidgets import QApplication, QListView, QMainWindow


class SimpleListApp(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Simple List App")
        self.setGeometry(100, 100, 600, 400)

        fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

        self.model = QStringListModel(fruits)
        self.view = QListView()
        self.view.setModel(self.model)

        self.setCentralWidget(self.view)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = SimpleListApp()
    window.show()

    app.exec()
