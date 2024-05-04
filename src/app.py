import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from src.ui.main_win import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Эмулятор датчиков Modbus")
        self.ui = Ui_MainWindow()


if __name__ == "__main__":
    app = QApplication([])
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
