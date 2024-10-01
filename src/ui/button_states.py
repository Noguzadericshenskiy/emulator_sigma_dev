from PySide6.QtCore import QRect
from PySide6.QtWidgets import QPushButton


class StatesBtn:

    def btn_norma(self, parent):
        norma = QPushButton(parent)
        norma.setObjectName(u"norma_btn")
        norma.setGeometry(QRect(20, 30, 151, 23))
        norma.setText("Норма")
        return norma

    def btn_error_mb(self, parent, num=0):
        error = QPushButton(parent)
        error.setGeometry(QRect(20, 30, 151, 23))
        if num == 0:
            error.setText("Неисправность")
            error.setObjectName(u"btn_error_mb")
        elif num == 121:
            error.setText("Неисправность ШС1")
            error.setObjectName(u"btn_error_1_mb")
        elif num == 122:
            error.setText("Неисправность ШС2")
            error.setObjectName(u"btn_error_2_mb")
        elif num == 123:
            error.setText("Неисправность ШС3")
            error.setObjectName(u"btn_error_3_mb")
        return error

    def activation_fire(self, parent, num=0):
        fire = QPushButton(parent)

        fire.setGeometry(QRect(20, 30, 151, 23))
        if num == 0:
            fire.setText("Сработал")
            fire.setObjectName(u"fire_btn")
        elif num == 101:
            fire.setText("Сработал ШС1")
            fire.setObjectName(u"fire_1_btn")
        elif num == 102:
            fire.setText("Сработал ШС2")
            fire.setObjectName(u"fire_2_btn")
        elif num == 103:
            fire.setText("Сработал ШС3")
            fire.setObjectName(u"fire_3_btn")
        return fire

    def btn_alarm(self, parent):
        alarm = QPushButton(parent)
        alarm.setObjectName(u"alarm_btn")
        alarm.setGeometry(QRect(20, 30, 151, 23))
        alarm.setText("Тревога")
        return alarm

    def btn_alarm_in1(self, parent):
        alarm = QPushButton(parent)
        alarm.setObjectName(u"alarm_in1_btn")
        alarm.setGeometry(QRect(20, 30, 151, 23))
        alarm.setText("Сработал S1.1")
        return alarm

    def btn_alarm_in1_2(self, parent):
        alarm = QPushButton(parent)
        alarm.setObjectName(u"alarm_in1_2_btn")
        alarm.setGeometry(QRect(20, 30, 151, 23))
        alarm.setText("Сработал S1.2")
        return alarm

    def btn_alarm_in2(self, parent):
        alarm = QPushButton(parent)
        alarm.setObjectName(u"alarm_in2_btn")
        alarm.setGeometry(QRect(20, 30, 151, 23))
        alarm.setText("Сработал S2.1")
        return alarm

    def btn_alarm_in2_2(self, parent):
        alarm = QPushButton(parent)
        alarm.setObjectName(u"alarm_in2_2_btn")
        alarm.setGeometry(QRect(20, 30, 151, 23))
        alarm.setText("Сработал S2.2")
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

    def btn_break_in1(self, parent):
        break_btn = QPushButton(parent)
        break_btn.setObjectName(u"break_in1_btn")
        break_btn.setGeometry(QRect(20, 30, 151, 23))
        break_btn.setText("Обрыв ШС S1")
        return break_btn

    def btn_break_in2(self, parent):
        break_btn = QPushButton(parent)
        break_btn.setObjectName(u"break_in2_btn")
        break_btn.setGeometry(QRect(20, 30, 151, 23))
        break_btn.setText("Обрыв ШС S2")
        return break_btn

    def btn_break_out1(self, parent):
        break_btn = QPushButton(parent)
        break_btn.setObjectName(u"break_out1_btn")
        break_btn.setGeometry(QRect(20, 30, 151, 23))
        break_btn.setText("Обрыв NO out1")
        return break_btn

    def btn_break_out2(self, parent):
        break_btn = QPushButton(parent)
        break_btn.setObjectName(u"break_out2_btn")
        break_btn.setGeometry(QRect(20, 30, 151, 23))
        break_btn.setText("Обрыв NO out2")
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

    def btn_kz_in1(self, parent):
        kz = QPushButton(parent)
        kz.setObjectName(u"kz_in1_btn")
        kz.setGeometry(QRect(20, 30, 151, 23))
        kz.setText("КЗ ШС S1")
        return kz

    def btn_kz_in2(self, parent):
        kz = QPushButton(parent)
        kz.setObjectName(u"kz_in2_btn")
        kz.setGeometry(QRect(20, 30, 151, 23))
        kz.setText("КЗ ШС S2")
        return kz

    def btn_kz_out1(self, parent):
        kz = QPushButton(parent)
        kz.setObjectName(u"kz_out1_btn")
        kz.setGeometry(QRect(20, 30, 151, 23))
        kz.setText("Обрыв NC out1")
        return kz

    def btn_kz_out2(self, parent):
        kz = QPushButton(parent)
        kz.setObjectName(u"kz_out2_btn")
        kz.setGeometry(QRect(20, 30, 151, 23))
        kz.setText("Обрыв NC out2")
        return kz

    def btn_noise_s1(self, parent):
        noise = QPushButton(parent)
        noise.setObjectName(u"noise_s1_btn")
        noise.setGeometry(QRect(20, 30, 151, 23))
        noise.setText("Шум на S1")
        return noise

    def btn_noise_s2(self, parent):
        noise = QPushButton(parent)
        noise.setObjectName(u"noise_s2_btn")
        noise.setGeometry(QRect(20, 30, 151, 23))
        noise.setText("Шум на S2")
        return noise

    def btn_test(self, parent):
        noise = QPushButton(parent)
        noise.setObjectName(u"test")
        noise.setGeometry(QRect(20, 30, 151, 23))
        noise.setText("Тест")
        return noise

    def btn_pwr(self, parent):
        power = QPushButton(parent)
        power.setObjectName(u"power_btn")
        power.setGeometry(QRect(20, 30, 151, 23))
        power.setText("Ошибка питания")
        return power
