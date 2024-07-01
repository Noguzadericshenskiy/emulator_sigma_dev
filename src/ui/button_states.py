from PySide6.QtCore import QRect
from PySide6.QtWidgets import QPushButton


class StatesBtn:
    def btn_norma(self, parent):
        norma = QPushButton(parent)
        norma.setObjectName(u"norma_btn")
        norma.setGeometry(QRect(20, 30, 151, 23))
        norma.setText("Норма")
        return norma

    def btn_fire(self, parent):
        fire = QPushButton(parent)
        fire.setObjectName(u"fire_btn")
        fire.setGeometry(QRect(20, 30, 151, 23))
        fire.setText("Пожар")
        return fire

    def btn_alarm(self, parent):
        alarm = QPushButton(parent)
        alarm.setObjectName(u"alarm_btn")
        alarm.setGeometry(QRect(20, 30, 151, 23))
        alarm.setText("Тревога")
        return alarm

    def btn_diff_fire(self, parent):
        diff_fire = QPushButton(parent)
        diff_fire.setObjectName(u"diff_fire_btn")
        diff_fire.setGeometry(QRect(20, 30, 151, 23))
        diff_fire.setText("Дифф пожар")
        return diff_fire

    def btn_dirt(self, parent):
        dirt = QPushButton(parent)
        dirt.setObjectName(u"dirt_btn")
        dirt.setGeometry(QRect(20, 30, 151, 23))
        dirt.setText("Пыль")
        return dirt

    def btn_noise(self, parent):
        noise = QPushButton(parent)
        noise.setObjectName(u"noise_btn")
        noise.setGeometry(QRect(20, 30, 151, 23))
        noise.setText("Шум")
        return noise

    def btn_break(self, parent):
        break_btn = QPushButton(parent)
        break_btn.setObjectName(u"break_btn")
        break_btn.setGeometry(QRect(20, 30, 151, 23))
        break_btn.setText("Обрыв")
        return break_btn

    def btn_swich(self, parent):
        switch = QPushButton(parent)
        switch.setObjectName(u"switch_btn")
        switch.setGeometry(QRect(20, 30, 151, 23))
        switch.setText("Тампер")
        switch.setToolTip("Норма (default) - замкнут")
        return switch

    def btn_sensitivity(self, parent):
        sensitivity = QPushButton(parent)
        sensitivity.setObjectName(u"sensitivity_btn")
        sensitivity.setGeometry(QRect(20, 30, 151, 23))
        sensitivity.setText("Чувствительность")
        sensitivity.setToolTip("Потеря чувствительности")
        return sensitivity

    def btn_kz(self, parent):
        kz = QPushButton(parent)
        kz.setObjectName(u"kz_btn")
        kz.setGeometry(QRect(20, 30, 151, 23))
        kz.setText("Сработал МКЗ")
        return kz
