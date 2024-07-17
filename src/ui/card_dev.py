from PySide6.QtWidgets import QWidget, QLabel


class CardDeviceMB(QWidget):
    def __init__(self):
        super().__init__()
        # self.device = device
        self.type_lbl = QLabel()
        self.slave_lbl = QLabel()
        self.state_lbl = QLabel()
        self.serialnumber_lbl = QLabel()

        self.type_lbl.setText("type")
        self.slave_lbl.setText("slave")
        self.state_lbl.setText("state")
        self.serialnumber_lbl.setText("serialnumber")



