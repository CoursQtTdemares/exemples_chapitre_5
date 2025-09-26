import sys

from PyQt6.QtWidgets import QApplication

from src.dataframe_window import DataFrameWindow


def main() -> int:
    app = QApplication(sys.argv)
    window = DataFrameWindow()
    window.show()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
