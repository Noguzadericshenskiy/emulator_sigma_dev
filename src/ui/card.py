from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QGroupBox, QLabel,
    QSizePolicy, QWidget)

class Ui_CardSensor(QWidget):
    def setupUi(self, CardSensor):
        if not CardSensor.objectName():
            CardSensor.setObjectName(u"CardSensor")
        CardSensor.resize(480, 640)
        self.card_groupBox = QGroupBox(CardSensor)
        self.card_groupBox.setObjectName(u"card_groupBox")
        self.card_groupBox.setGeometry(QRect(50, 60, 161, 151))
        self.formLayoutWidget = QWidget(self.card_groupBox)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 20, 141, 84))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.card_type_lbl = QLabel(self.formLayoutWidget)
        self.card_type_lbl.setObjectName(u"card_type_lbl")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.card_type_lbl)

        self.card_info_type_lbl = QLabel(self.formLayoutWidget)
        self.card_info_type_lbl.setObjectName(u"card_info_type_lbl")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.card_info_type_lbl)

        self.card_slave_lbl = QLabel(self.formLayoutWidget)
        self.card_slave_lbl.setObjectName(u"card_slave_lbl")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.card_slave_lbl)

        self.card_info_slave_lbl = QLabel(self.formLayoutWidget)
        self.card_info_slave_lbl.setObjectName(u"card_info_slave_lbl")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.card_info_slave_lbl)

        self.card_sn_lbl = QLabel(self.formLayoutWidget)
        self.card_sn_lbl.setObjectName(u"card_sn_lbl")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.card_sn_lbl)

        self.card_info_sn_lbl = QLabel(self.formLayoutWidget)
        self.card_info_sn_lbl.setObjectName(u"card_info_sn_lbl")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.card_info_sn_lbl)

        self.card_state_lbl = QLabel(self.formLayoutWidget)
        self.card_state_lbl.setObjectName(u"card_state_lbl")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.card_state_lbl)

        self.card_info_state_lbl = QLabel(self.formLayoutWidget)
        self.card_info_state_lbl.setObjectName(u"card_info_state_lbl")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.card_info_state_lbl)

        self.label = QLabel(self.card_groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 110, 151, 16))
        self.label_2 = QLabel(self.card_groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 130, 141, 16))

        self.retranslateUi(CardSensor)

        QMetaObject.connectSlotsByName(CardSensor)
    # setupUi

    def retranslateUi(self, CardSensor):
        CardSensor.setWindowTitle(QCoreApplication.translate("CardSensor", u"Form", None))
        self.card_groupBox.setTitle(QCoreApplication.translate("CardSensor", u"GroupBox", None))
        self.card_type_lbl.setText(QCoreApplication.translate("CardSensor", u"\u0422\u0438\u043f", None))
        self.card_info_type_lbl.setText(QCoreApplication.translate("CardSensor", u"TextLabel", None))
        self.card_slave_lbl.setText(QCoreApplication.translate("CardSensor", u"\u0410\u0434\u0440\u0435\u0441", None))
        self.card_info_slave_lbl.setText(QCoreApplication.translate("CardSensor", u"TextLabel", None))
        self.card_sn_lbl.setText(QCoreApplication.translate("CardSensor", u"\u0421\u0435\u0440\u0438\u0439\u043d\u044b\u0439 N", None))
        self.card_info_sn_lbl.setText(QCoreApplication.translate("CardSensor", u"TextLabel", None))
        self.card_state_lbl.setText(QCoreApplication.translate("CardSensor", u"\u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435", None))
        self.card_info_state_lbl.setText(QCoreApplication.translate("CardSensor", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("CardSensor", u"\u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u0430 (HEX)", None))
        self.label_2.setText(QCoreApplication.translate("CardSensor", u"TextLabel", None))
    # retranslateUi

