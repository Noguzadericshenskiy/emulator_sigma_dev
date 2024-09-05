import sys
import os

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from src.root_window import MainWindow


basedir = os.path.dirname(__file__)


def include_style(app):
    with open(os.path.join(basedir, "ui/style.qss"), "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)


if __name__ == "__main__":
    app = QApplication([])
    app.setWindowIcon(QIcon(os.path.join(basedir, "icons", "logo.ico")))
    widget = MainWindow()
    include_style(app)
    widget.show()
    sys.exit(app.exec())
