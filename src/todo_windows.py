from PyQt6.QtWidgets import QHBoxLayout, QLineEdit, QListView, QMainWindow, QPushButton, QVBoxLayout, QWidget

from src.todo_model import TodoModel


class TodoWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Todo List")
        self.setGeometry(100, 100, 600, 400)

        self.model = TodoModel()

        self.setup_ui()

    def setup_ui(self) -> None:
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout_vertical = QVBoxLayout()
        central_widget.setLayout(layout_vertical)

        # Zone de saisie
        input_todo_layout = QHBoxLayout()
        self.todo_input = QLineEdit()
        self.todo_input.setPlaceholderText("Ajouter une tâche ...")
        self.add_todo_button = QPushButton("Ajouter")
        self.add_todo_button.clicked.connect(self.add_todo)

        input_todo_layout.addWidget(self.todo_input)
        input_todo_layout.addWidget(self.add_todo_button)
        layout_vertical.addLayout(input_todo_layout)

        # Zone de visualisation
        self.view = QListView()
        self.view.setModel(self.model)
        layout_vertical.addWidget(self.view)

        # Zone de boutons
        action_layout = QHBoxLayout()
        self.remove_todo_button = QPushButton("Supprimer")
        self.remove_todo_button.clicked.connect(self.remove_todo)
        self.toggle_todo_button = QPushButton("Toggle")
        self.toggle_todo_button.clicked.connect(self.toggle_todo)
        action_layout.addWidget(self.remove_todo_button)
        action_layout.addWidget(self.toggle_todo_button)
        layout_vertical.addLayout(action_layout)

    def add_todo(self) -> None:
        self.model.add_todo(self.todo_input.text())
        self.todo_input.clear()

    def remove_todo(self) -> None:
        indexes = self.view.selectedIndexes()
        for index in indexes:
            self.model.remove_todo(index.row())

    def toggle_todo(self) -> None:
        indexes = self.view.selectedIndexes()
        for index in indexes:
            self.model.toggle_todo(index.row())
