import sys

from PyQt6.QtWidgets import QApplication

from src.todo_windows import TodoWindow


def main() -> int:
    """Entry point for exemples_chapitre_5."""
    app = QApplication(sys.argv)
    window = TodoWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
