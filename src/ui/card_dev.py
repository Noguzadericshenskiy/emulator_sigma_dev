from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PySide6.QtCore import QSize


class CardDeviceASH(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName(u"card_device_ash")
        self.setContentsMargins(5, 5, 5, 5)

        v_layout = QVBoxLayout()
        h1_layout = QHBoxLayout()
        h2_layout = QHBoxLayout()
        h3_layout = QHBoxLayout()
        h4_layout = QHBoxLayout()
        h5_layout = QHBoxLayout()

        v_layout.setContentsMargins(0, 0, 0, 0)
        v_layout.setSpacing(0)

        card_type_lbl = QLabel("Тип")
        card_type_lbl.setContentsMargins(3, 3, 0, 1)
        card_slave_lbl = QLabel("Адрес")
        card_slave_lbl.setContentsMargins(3, 1, 0, 1)
        card_sn_lbl = QLabel("Сер.№")
        card_sn_lbl.setContentsMargins(3, 1, 0, 1)
        card_state_lbl = QLabel("Состояние")
        card_state_lbl.setContentsMargins(3, 1, 0, 1)
        card_state_in_lbl = QLabel("Сост. in")
        card_state_in_lbl.setContentsMargins(3, 1, 0, 3)

        self.card_info_type_lbl = QLabel()
        self.card_info_slave_lbl = QLabel()
        self.card_info_sn_lbl = QLabel()
        self.card_info_state_lbl = QLabel()
        self.card_info_state_in_lbl = QLabel()

        h1_layout.addWidget(card_type_lbl)
        h1_layout.addWidget(self.card_info_type_lbl)
        h2_layout.addWidget(card_slave_lbl)
        h2_layout.addWidget(self.card_info_slave_lbl)
        h3_layout.addWidget(card_sn_lbl)
        h3_layout.addWidget(self.card_info_sn_lbl)
        h4_layout.addWidget(card_state_lbl)
        h4_layout.addWidget(self.card_info_state_lbl)
        h5_layout.addWidget(card_state_in_lbl)
        h5_layout.addWidget(self.card_info_state_in_lbl)

        v_layout.addLayout(h1_layout)
        v_layout.addLayout(h2_layout)
        v_layout.addLayout(h3_layout)
        v_layout.addLayout(h4_layout)
        v_layout.addLayout(h5_layout)

        self.setLayout(v_layout)

        self.change_color()

    def set_text_lbl(self, params):
        self.card_info_type_lbl.setText(params["type"])
        self.card_info_slave_lbl.setText(str(params["slave"]))
        self.card_info_sn_lbl.setText(str(params["serialnumber"]))
        self.card_info_state_lbl.setText(params["state"])
        self.card_info_state_in_lbl.setText("None")
        self.change_color()

    def get_params(self):
        type_sens = self.card_info_type_lbl.text()
        slave = self.card_info_slave_lbl.text()
        sn = self.card_info_sn_lbl.text()
        state = self.card_info_state_lbl.text()
        params = {"type": type_sens,  "slave": int(slave), "serialnumber": int(sn), "state": state}
        return params

    def change_color(self):
        if self.card_info_state_lbl.text() == "Норма":
            self.setStyleSheet("background-color: rgb(0, 130, 0);")
        elif self.card_info_state_lbl.text() == "Сработал":
            self.setStyleSheet("background-color: rgb(173, 0, 0);")
        elif self.card_info_state_lbl.text() == "Неисправность":
            self.setStyleSheet("background-color: rgb(255, 140, 0); color: rgb(0, 0, 0);")
        else:
            self.setStyleSheet("background-color: rgb(255, 140, 0); color: rgb(255, 255, 255);")


class CardDeviceMB(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName(u"card_device_ash")
        self.setContentsMargins(5, 5, 5, 5)

        v_layout = QVBoxLayout()
        h1_layout = QHBoxLayout()
        h2_layout = QHBoxLayout()
        h3_layout = QHBoxLayout()
        h4_layout = QHBoxLayout()
        h5_layout = QHBoxLayout()

        v_layout.setContentsMargins(0, 0, 0, 0)
        v_layout.setSpacing(0)

        card_type_lbl = QLabel("Тип")
        card_type_lbl.setContentsMargins(3, 3, 0, 1)
        card_slave_lbl = QLabel("Адрес")
        card_slave_lbl.setContentsMargins(3, 1, 0, 1)
        card_sn_lbl = QLabel("Сер.№")
        card_sn_lbl.setContentsMargins(3, 1, 0, 1)
        card_state_lbl = QLabel("Состояние")
        card_state_lbl.setContentsMargins(3, 1, 0, 1)
        card_state_in_lbl = QLabel("Сост. in")
        card_state_in_lbl.setContentsMargins(3, 1, 0, 3)

        self.card_info_type_lbl = QLabel()
        self.card_info_slave_lbl = QLabel()
        self.card_info_sn_lbl = QLabel()
        self.card_info_state_lbl = QLabel()
        self.card_info_state_in_lbl = QLabel()

        h1_layout.addWidget(card_type_lbl)
        h1_layout.addWidget(self.card_info_type_lbl)
        h2_layout.addWidget(card_slave_lbl)
        h2_layout.addWidget(self.card_info_slave_lbl)
        h3_layout.addWidget(card_sn_lbl)
        h3_layout.addWidget(self.card_info_sn_lbl)
        h4_layout.addWidget(card_state_lbl)
        h4_layout.addWidget(self.card_info_state_lbl)
        h5_layout.addWidget(card_state_in_lbl)
        h5_layout.addWidget(self.card_info_state_in_lbl)

        v_layout.addLayout(h1_layout)
        v_layout.addLayout(h2_layout)
        v_layout.addLayout(h3_layout)
        v_layout.addLayout(h4_layout)
        v_layout.addLayout(h5_layout)

        self.setLayout(v_layout)

        self.change_color()

    def set_text_lbl(self, params):
        self.card_info_type_lbl.setText(params["type"])
        self.card_info_slave_lbl.setText(str(params["slave"]))
        self.card_info_sn_lbl.setText(str(params["serialnumber"]))
        self.card_info_state_lbl.setText(params["state"])
        self.card_info_state_in_lbl.setText("None")
        self.change_color()

    def get_params(self):
        type_sens = self.card_info_type_lbl.text()
        slave = self.card_info_slave_lbl.text()
        sn = self.card_info_sn_lbl.text()
        state = self.card_info_state_lbl.text()
        params = {"type": type_sens,  "slave": int(slave), "serialnumber": int(sn), "state": state}
        return params

    def change_color(self):
        if self.card_info_state_lbl.text() == "Норма":
            self.setStyleSheet("background-color: rgb(0, 130, 0);")
        elif self.card_info_state_lbl.text() == "Сработал":
            self.setStyleSheet("background-color: rgb(173, 0, 0);")
        elif self.card_info_state_lbl.text() == "Неисправность":
            self.setStyleSheet("background-color: rgb(255, 140, 0); color: rgb(0, 0, 0);")
        else:
            self.setStyleSheet("background-color: rgb(255, 140, 0); color: rgb(255, 255, 255);")
