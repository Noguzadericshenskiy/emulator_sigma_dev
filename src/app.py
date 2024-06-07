import sys

from PySide6.QtWidgets import QApplication

from src.root_window import MainWindow


def include_style(app):
    with open("ui/style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)


if __name__ == "__main__":
    app = QApplication([])
    widget = MainWindow()
    include_style(app)
    widget.show()
    sys.exit(app.exec())
