from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PySide6.QtCore import QSize

class CardDeviceASH(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName(u"card_device_ash")

        v_layout = QVBoxLayout()
        h1_layout = QHBoxLayout()
        h2_layout = QHBoxLayout()
        h3_layout = QHBoxLayout()
        h4_layout = QHBoxLayout()
        h5_layout = QHBoxLayout()

        v_layout.setContentsMargins(0, 0, 0, 0)
        v_layout.setSpacing(0)

        self.card_info_type_lbl = QLabel()
        self.card_info_slave_lbl = QLabel()
        self.card_info_sn_lbl = QLabel()
        self.card_info_state_lbl = QLabel()
        self.card_info_state_in_lbl = QLabel()

        h1_layout.addWidget(QLabel("Тип"))
        h1_layout.addWidget(self.card_info_type_lbl)
        h2_layout.addWidget(QLabel("Адрес"))
        h2_layout.addWidget(self.card_info_slave_lbl)
        h3_layout.addWidget(QLabel("Сер.№"))
        h3_layout.addWidget(self.card_info_sn_lbl)
        h4_layout.addWidget(QLabel("Состояние"))
        h4_layout.addWidget(self.card_info_state_lbl)
        h5_layout.addWidget(QLabel("Сост. in"))
        h5_layout.addWidget(self.card_info_state_in_lbl)

        v_layout.addLayout(h1_layout)
        v_layout.addLayout(h2_layout)
        v_layout.addLayout(h3_layout)
        v_layout.addLayout(h4_layout)
        v_layout.addLayout(h5_layout)

        self.setLayout(v_layout)

    def set_text_lbl(self, params):
        self.card_info_type_lbl.setText(params["type"])
        self.card_info_slave_lbl.setText(str(params["slave"]))
        self.card_info_sn_lbl.setText(params["serialnumber"])
        self.card_info_state_lbl.setText(params["state"])
        self.card_info_state_in_lbl.setText("None")

    def get_params(self):
        type_sens = self.card_info_type_lbl.text()
        slave = self.card_info_slave_lbl.text()
        sn = self.card_info_sn_lbl.text()
        state = self.card_info_state_lbl.text()
        params = {"type": type_sens,  "slave": slave, "serialnumber": sn, "state": state}
        return params

    def set_color(self):
        ...

