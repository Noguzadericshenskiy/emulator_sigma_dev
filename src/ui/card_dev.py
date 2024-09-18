from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout

from loguru import logger

class CardDeviceASH(QWidget):
    def __init__(self, sensor):
        super().__init__()
        self.setObjectName(u"card_device_ash")
        self.setContentsMargins(5, 5, 5, 5)
        self._create_card(sensor)

    def _create_card(self, sensor):
        self.v_layout = QVBoxLayout()
        self.h1_layout = QHBoxLayout()
        self.h2_layout = QHBoxLayout()
        self.h3_layout = QHBoxLayout()
        self.h4_layout = QHBoxLayout()
        self.h5_layout = QHBoxLayout()
        self.h6_layout = QHBoxLayout()

        self.v_layout.setContentsMargins(0, 0, 0, 0)
        self.v_layout.setSpacing(0)

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

        self.h1_layout.addWidget(card_type_lbl)
        self.h1_layout.addWidget(self.card_info_type_lbl)
        self.h2_layout.addWidget(card_slave_lbl)
        self.h2_layout.addWidget(self.card_info_slave_lbl)
        self.h3_layout.addWidget(card_sn_lbl)
        self.h3_layout.addWidget(self.card_info_sn_lbl)
        self.h4_layout.addWidget(card_state_lbl)
        self.h4_layout.addWidget(self.card_info_state_lbl)
        self.h5_layout.addWidget(card_state_in_lbl)
        self.h5_layout.addWidget(self.card_info_state_in_lbl)

        self.v_layout.addLayout(self.h1_layout)
        self.v_layout.addLayout(self.h2_layout)
        self.v_layout.addLayout(self.h3_layout)
        self.v_layout.addLayout(self.h4_layout)
        self.v_layout.addLayout(self.h5_layout)

        if sensor["type"] in ["ИСМ-5", "ИСМ-220.4"]:
            self.rele_1_stete = QLabel("Реле 1")
            self.rele_1_stete.setContentsMargins(3, 1, 0, 1)
            self.rele_1_stete.setStyleSheet("background-color: rgb(0, 0, 221); color: rgb(185, 189, 189);")
            self.rele_2_stete = QLabel("Реле 2")
            self.rele_2_stete.setContentsMargins(3, 1, 0, 1)
            self.rele_2_stete.setStyleSheet("background-color: rgb(0, 0, 221); color: rgb(185, 189, 189);")
            self.h6_layout.addWidget(self.rele_1_stete)
            self.h6_layout.addWidget(self.rele_2_stete)
            self.v_layout.addLayout(self.h6_layout)

        self.setLayout(self.v_layout)

    def set_text_lbl(self, params):
        self.card_info_type_lbl.setText(params["type"])
        self.card_info_slave_lbl.setText(str(params["slave"]))
        self.card_info_sn_lbl.setText(str(params["serialnumber"]))
        self.card_info_state_lbl.setText(params["state"])
        # self.card_info_state_in_lbl.setText(params["state_in"])
        self.set_state_in(params)
        self.change_color(params)

    "TODO  сделать инверсию битов реле исм5 для вывода и самих реле"
    def set_state_in(self, sensor):
        if sensor["state_in"] != "None":
            state = int(sensor["state_in"], 16).to_bytes(4, "big").hex(sep=" ")
            self.card_info_state_in_lbl.setText(state)

            if sensor["type"] in ["ИСМ-5", "ИСМ-220.4"] and sensor["state_in"] != "None":
                self.set_state_rele(sensor)
        else:
            self.card_info_state_in_lbl.setText("None")

    def set_state_rele(self, sensor):
        try:
            if sensor["state_in"] != "None":
                mask_r1 = 0b1
                mask_r2 = 0b10
                state_rele = int(bin(int(sensor["state_in"][4:6], 16)), 2)

                if state_rele & mask_r1:
                    self.rele_1_stete.setStyleSheet("background-color: rgb(0, 0, 221); color: rgb(185, 189, 189);")
                else:
                    self.rele_1_stete.setStyleSheet("background-color: rgb(0, 238, 0); color: rgb(0, 0, 221);")
                if state_rele & mask_r2:
                    self.rele_2_stete.setStyleSheet("background-color: rgb(0, 0, 221); color: rgb(185, 189, 189);")
                else:
                    self.rele_2_stete.setStyleSheet("background-color: rgb(0, 238, 0); color: rgb(0, 0, 221);")
        except Exception as err:
            logger.error(err)



    def get_params(self):
        type_sens = self.card_info_type_lbl.text()
        slave = self.card_info_slave_lbl.text()
        sn = self.card_info_sn_lbl.text()
        state = self.card_info_state_lbl.text()
        state_in = self.card_info_state_in_lbl.text().replace(" ", "")
        params = {"type": type_sens,
                  "slave": int(slave),
                  "serialnumber": int(sn),
                  "state": state,
                  "state_in": state_in}
        return params

    def change_color(self, params):
        if self.card_info_state_lbl.text() == "Норма":
            self.setStyleSheet("background-color: rgb(0, 130, 0);")
        elif self.card_info_state_lbl.text() == "Сработал":
            self.setStyleSheet("background-color: rgb(173, 0, 0);")
        elif self.card_info_state_lbl.text() == "Неисправность":
            self.setStyleSheet("background-color: rgb(255, 140, 0); color: rgb(0, 0, 0);")
        else:
            self.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 255, 255);")


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

        v_layout.setContentsMargins(0, 0, 0, 0)
        v_layout.setSpacing(0)

        card_type_lbl = QLabel("Тип")
        card_type_lbl.setContentsMargins(3, 3, 0, 1)
        card_slave_lbl = QLabel("Адрес")
        card_slave_lbl.setContentsMargins(3, 1, 0, 1)
        card_state_lbl = QLabel("Состояние")
        card_state_lbl.setContentsMargins(3, 1, 0, 1)

        self.card_info_type_lbl = QLabel()
        self.card_info_slave_lbl = QLabel()
        self.card_info_state_lbl = QLabel()

        h1_layout.addWidget(card_type_lbl)
        h1_layout.addWidget(self.card_info_type_lbl)
        h2_layout.addWidget(card_slave_lbl)
        h2_layout.addWidget(self.card_info_slave_lbl)
        h3_layout.addWidget(card_state_lbl)
        h3_layout.addWidget(self.card_info_state_lbl)

        v_layout.addLayout(h1_layout)
        v_layout.addLayout(h2_layout)
        v_layout.addLayout(h3_layout)

        self.setLayout(v_layout)

        self.change_color()

    def set_text_lbl(self, params):
        self.card_info_type_lbl.setText(params["type"])
        self.card_info_slave_lbl.setText(str(params["slave"]))
        self.card_info_state_lbl.setText(params["state"])
        self.change_color()

    def get_params(self):
        type_sens = self.card_info_type_lbl.text()
        slave = self.card_info_slave_lbl.text()
        state = self.card_info_state_lbl.text()
        params = {"type": type_sens,  "slave": int(slave), "state": state, }
        return params

    def change_color(self):
        if self.card_info_state_lbl.text() == "Норма":
            self.setStyleSheet("background-color: rgb(0, 130, 0);")
        elif self.card_info_state_lbl.text() == "Сработал":
            self.setStyleSheet("background-color: rgb(173, 0, 0);")
        elif self.card_info_state_lbl.text() == "Неисправность":
            self.setStyleSheet("background-color: rgb(255, 140, 0); color: rgb(0, 0, 0);")
        else:
            self.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 255, 255);")


def get_bit(value: int, n: int) -> int:
    return (value >> n & 1) != 0


def set_bit(value: int, n: int) -> int:
    return value | (1 << n)


def clear_bit(value: int, n: int) -> int:
    return value & ~(1 << n)