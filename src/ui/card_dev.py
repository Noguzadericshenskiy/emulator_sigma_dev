from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout


class CardDeviceMB(QWidget):
    def __init__(self):
        super().__init__()

        self.card_type_lbl = QLabel()
        self.card_type_lbl.setText("Тип")
        self.card_info_type_lbl = QLabel()
        self.card_slave_lbl = QLabel()
        self.card_slave_lbl.setText("Адрес")
        self.card_info_slave_lbl = QLabel()
        self.card_sn_lbl = QLabel()
        self.card_sn_lbl.setText("Номер")
        self.card_info_sn_lbl = QLabel()
        self.card_state_lbl = QLabel()
        self.card_state_lbl.setText("Состояние")
        self.card_info_state_lbl = QLabel()

        self.h1_layout = QHBoxLayout()
        self.h2_layout = QHBoxLayout()
        self.h3_layout = QHBoxLayout()
        self.h4_layout = QHBoxLayout()
        self.h5_layout = QHBoxLayout()

        self.h1_layout.addWidget(self.card_type_lbl)
        self.h1_layout.addWidget(self.card_info_type_lbl)
        self.h2_layout.addWidget(self.card_slave_lbl)
        self.h2_layout.addWidget(self.card_info_slave_lbl)







