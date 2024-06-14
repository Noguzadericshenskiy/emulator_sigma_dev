# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_win_v5.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1291, 824)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QSize(1271, 800))
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.main_tab = QWidget()
        self.main_tab.setObjectName(u"main_tab")
        sizePolicy.setHeightForWidth(self.main_tab.sizePolicy().hasHeightForWidth())
        self.main_tab.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.main_tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(self.main_tab)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.groupBox.setMinimumSize(QSize(371, 71))
        self.groupBox.setStyleSheet(u"")
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 30, 344, 22))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.normal_btn = QPushButton(self.layoutWidget)
        self.normal_btn.setObjectName(u"normal_btn")
        sizePolicy1.setHeightForWidth(self.normal_btn.sizePolicy().hasHeightForWidth())
        self.normal_btn.setSizePolicy(sizePolicy1)
        self.normal_btn.setMinimumSize(QSize(110, 20))
        self.normal_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(157, 242, 160);\n"
"	border: none;\n"
"\n"
"	font: 75 10pt \"Georgia\";\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(152, 234, 154);\n"
"	border-left: 2px solid rgb(0, 160, 0);\n"
"	border-top: 2px solid rgb(0, 160, 0);\n"
"	border-right: 2px solid rgb(0, 160, 0);	\n"
"	border-bottom: 2px solid rgb(0, 160, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(157, 242, 160);\n"
"	background-color: rgb(143, 220, 146);\n"
"	border-left: 2px solid rgb(0, 130, 0);\n"
"	border-top: 2px solid rgb(0, 130, 0);\n"
"	border-right: 2px solid rgb(0, 130, 0);	\n"
"	border-bottom: 2px solid rgb(0, 130, 0);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.normal_btn)

        self.fire_btn = QPushButton(self.layoutWidget)
        self.fire_btn.setObjectName(u"fire_btn")
        sizePolicy1.setHeightForWidth(self.fire_btn.sizePolicy().hasHeightForWidth())
        self.fire_btn.setSizePolicy(sizePolicy1)
        self.fire_btn.setMinimumSize(QSize(110, 20))
        self.fire_btn.setBaseSize(QSize(100, 0))
        self.fire_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(173, 0, 0);\n"
"	font: 75 10pt \"Georgia\";\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(173, 0, 0);;\n"
"	border-left: 2px solid rgb(0, 160, 0);\n"
"	border-top: 2px solid rgb(0, 160, 0);\n"
"	border-right: 2px solid rgb(0, 160, 0);	\n"
"	border-bottom: 2px solid rgb(0, 160, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(173, 0, 0);\n"
"	border-left: 2px solid rgb(0, 130, 0);\n"
"	border-top: 2px solid rgb(0, 130, 0);\n"
"	border-right: 2px solid rgb(0, 130, 0);	\n"
"	border-bottom: 2px solid rgb(0, 130, 0);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.fire_btn)

        self.failure_btn = QPushButton(self.layoutWidget)
        self.failure_btn.setObjectName(u"failure_btn")
        sizePolicy1.setHeightForWidth(self.failure_btn.sizePolicy().hasHeightForWidth())
        self.failure_btn.setSizePolicy(sizePolicy1)
        self.failure_btn.setMinimumSize(QSize(110, 20))
        self.failure_btn.setMaximumSize(QSize(100, 16777215))
        self.failure_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 140, 0);\n"
"	font: 75 10pt \"Georgia\";\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 140, 0);\n"
"	border-left: 2px solid rgb(0, 160, 0);\n"
"	border-top: 2px solid rgb(0, 160, 0);\n"
"	border-right: 2px solid rgb(0, 160, 0);	\n"
"	border-bottom: 2px solid rgb(0, 160, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 140, 0);\n"
"	border-left: 2px solid rgb(0, 130, 0);\n"
"	border-top: 2px solid rgb(0, 130, 0);\n"
"	border-right: 2px solid rgb(0, 130, 0);	\n"
"	border-bottom: 2px solid rgb(0, 130, 0);\n"
"}")

        self.horizontalLayout.addWidget(self.failure_btn)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.kz_r_btn = QRadioButton(self.main_tab)
        self.kz_r_btn.setObjectName(u"kz_r_btn")

        self.horizontalLayout_3.addWidget(self.kz_r_btn)

        self.break_r_btn = QRadioButton(self.main_tab)
        self.break_r_btn.setObjectName(u"break_r_btn")

        self.horizontalLayout_3.addWidget(self.break_r_btn)

        self.option_r_btn = QRadioButton(self.main_tab)
        self.option_r_btn.setObjectName(u"option_r_btn")

        self.horizontalLayout_3.addWidget(self.option_r_btn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.sensor58_lbl = QLabel(self.main_tab)
        self.sensor58_lbl.setObjectName(u"sensor58_lbl")
        self.sensor58_lbl.setStyleSheet(u"")
        self.sensor58_lbl.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.sensor58_lbl.setMargin(5)
        self.sensor58_lbl.setIndent(0)

        self.gridLayout.addWidget(self.sensor58_lbl, 1, 7, 1, 1)

        self.sensor57_lbl = QLabel(self.main_tab)
        self.sensor57_lbl.setObjectName(u"sensor57_lbl")
        self.sensor57_lbl.setStyleSheet(u"")
        self.sensor57_lbl.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.sensor57_lbl.setMargin(5)
        self.sensor57_lbl.setIndent(0)

        self.gridLayout.addWidget(self.sensor57_lbl, 1, 6, 1, 1)

        self.sensor6_lbl = QLabel(self.main_tab)
        self.sensor6_lbl.setObjectName(u"sensor6_lbl")
        self.sensor6_lbl.setStyleSheet(u"")
        self.sensor6_lbl.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.sensor6_lbl.setMargin(5)
        self.sensor6_lbl.setIndent(0)

        self.gridLayout.addWidget(self.sensor6_lbl, 0, 5, 1, 1)

        self.sensor7_lbl = QLabel(self.main_tab)
        self.sensor7_lbl.setObjectName(u"sensor7_lbl")
        self.sensor7_lbl.setStyleSheet(u"")
        self.sensor7_lbl.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.sensor7_lbl.setMargin(5)
        self.sensor7_lbl.setIndent(0)

        self.gridLayout.addWidget(self.sensor7_lbl, 0, 6, 1, 1)

        self.sensor1_lbl = QLabel(self.main_tab)
        self.sensor1_lbl.setObjectName(u"sensor1_lbl")
        self.sensor1_lbl.setStyleSheet(u"")
        self.sensor1_lbl.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.sensor1_lbl.setMargin(5)
        self.sensor1_lbl.setIndent(0)

        self.gridLayout.addWidget(self.sensor1_lbl, 0, 0, 1, 1)

        self.sensor67_lbl = QLabel(self.main_tab)
        self.sensor67_lbl.setObjectName(u"sensor67_lbl")
        self.sensor67_lbl.setStyleSheet(u"")
        self.sensor67_lbl.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.sensor67_lbl.setMargin(5)
        self.sensor67_lbl.setIndent(0)

        self.gridLayout.addWidget(self.sensor67_lbl, 1, 16, 1, 1)

        self.sensor8_lbl = QLabel(self.main_tab)
        self.sensor8_lbl.setObjectName(u"sensor8_lbl")
        self.sensor8_lbl.setStyleSheet(u"")
        self.sensor8_lbl.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.sensor8_lbl.setMargin(5)
        self.sensor8_lbl.setIndent(0)

        self.gridLayout.addWidget(self.sensor8_lbl, 0, 7, 1, 1)

        self.sensor62_lbl = QLabel(self.main_tab)
        self.sensor62_lbl.setObjectName(u"sensor62_lbl")
        self.sensor62_lbl.setStyleSheet(u"")
        self.sensor62_lbl.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.sensor62_lbl.setMargin(5)
        self.sensor62_lbl.setIndent(0)

        self.gridLayout.addWidget(self.sensor62_lbl, 1, 11, 1, 1)

        self.sensor54_lbl = QLabel(self.main_tab)
        self.sensor54_lbl.setObjectName(u"sensor54_lbl")
        self.sensor54_lbl.setStyleSheet(u"")
        self.sensor54_lbl.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.sensor54_lbl.setMargin(5)
        self.sensor54_lbl.setIndent(0)

        self.gridLayout.addWidget(self.sensor54_lbl, 1, 3, 1, 1)

        self.sensor66_lbl = QLabel(self.main_tab)
        self.sensor66_lbl.setObjectName(u"sensor66_lbl")
        self.sensor66_lbl.setStyleSheet(u"")
        self.sensor66_lbl.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.sensor66_lbl.setMargin(5)
        self.sensor66_lbl.setIndent(0)

        self.gridLayout.addWidget(self.sensor66_lbl, 1, 15, 1, 1)

        self.sensor59_lbl = QLabel(self.main_tab)
        self.sensor59_lbl.setObjectName(u"sensor59_lbl")
        self.sensor59_lbl.setStyleSheet(u"")
        self.sensor59_lbl.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.sensor59_lbl.setMargin(5)
        self.sensor59_lbl.setIndent(0)

        self.gridLayout.addWidget(self.sensor59_lbl, 1, 8, 1, 1)

        self.sensor65_lbl = QLabel(self.main_tab)
        self.sensor65_lbl.setObjectName(u"sensor65_lbl")
        self.sensor65_lbl.setStyleSheet(u"")
        self.sensor65_lbl.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.sensor65_lbl.setMargin(5)
        self.sensor65_lbl.setIndent(0)

        self.gridLayout.addWidget(self.sensor65_lbl, 1, 14, 1, 1)

        self.sensor53_lbl = QLabel(self.main_tab)
        self.sensor53_lbl.setObjectName(u"sensor53_lbl")
        self.sensor53_lbl.setStyleSheet(u"")
        self.sensor53_lbl.setFrameShape(QFrame.NoFrame)
        self.sensor53_lbl.setFrameShadow(QFrame.Plain)
        self.sensor53_lbl.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.sensor53_lbl.setMargin(5)
        self.sensor53_lbl.setIndent(0)

        self.gridLayout.addWidget(self.sensor53_lbl, 1, 2, 1, 1)

        self.sensor61_lbl = QLabel(self.main_tab)
        self.sensor61_lbl.setObjectName(u"sensor61_lbl")
        self.sensor61_lbl.setStyleSheet(u"")
        self.sensor61_lbl.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.sensor61_lbl.setMargin(5)
        self.sensor61_lbl.setIndent(0)

        self.gridLayout.addWidget(self.sensor61_lbl, 1, 10, 1, 1)

        self.sensor64_lbl = QLabel(self.main_tab)
        self.sensor64_lbl.setObjectName(u"sensor64_lbl")
        self.sensor64_lbl.setStyleSheet(u"")
        self.sensor64_lbl.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.sensor64_lbl.setMargin(5)
        self.sensor64_lbl.setIndent(0)

        self.gridLayout.addWidget(self.sensor64_lbl, 1, 13, 1, 1)

        self.sensor60_lbl = QLabel(self.main_tab)
        self.sensor60_lbl.setObjectName(u"sensor60_lbl")
        self.sensor60_lbl.setStyleSheet(u"")
        self.sensor60_lbl.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.sensor60_lbl.setMargin(5)
        self.sensor60_lbl.setIndent(0)

        self.gridLayout.addWidget(self.sensor60_lbl, 1, 9, 1, 1)

        self.sensor56_lbl = QLabel(self.main_tab)
        self.sensor56_lbl.setObjectName(u"sensor56_lbl")
        self.sensor56_lbl.setStyleSheet(u"")
        self.sensor56_lbl.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.sensor56_lbl.setMargin(5)
        self.sensor56_lbl.setIndent(0)

        self.gridLayout.addWidget(self.sensor56_lbl, 1, 5, 1, 1)

        self.sensor63_lbl = QLabel(self.main_tab)
        self.sensor63_lbl.setObjectName(u"sensor63_lbl")
        self.sensor63_lbl.setStyleSheet(u"")
        self.sensor63_lbl.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.sensor63_lbl.setMargin(5)
        self.sensor63_lbl.setIndent(0)

        self.gridLayout.addWidget(self.sensor63_lbl, 1, 12, 1, 1)

        self.sensor3_lbl = QLabel(self.main_tab)
        self.sensor3_lbl.setObjectName(u"sensor3_lbl")
        self.sensor3_lbl.setStyleSheet(u"")
        self.sensor3_lbl.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.sensor3_lbl.setMargin(5)
        self.sensor3_lbl.setIndent(0)

        self.gridLayout.addWidget(self.sensor3_lbl, 0, 2, 1, 1)

        self.sensor55_lbl = QLabel(self.main_tab)
        self.sensor55_lbl.setObjectName(u"sensor55_lbl")
        self.sensor55_lbl.setStyleSheet(u"")
        self.sensor55_lbl.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.sensor55_lbl.setMargin(5)
        self.sensor55_lbl.setIndent(0)

        self.gridLayout.addWidget(self.sensor55_lbl, 1, 4, 1, 1)

        self.sensor5_lbl = QLabel(self.main_tab)
        self.sensor5_lbl.setObjectName(u"sensor5_lbl")
        self.sensor5_lbl.setStyleSheet(u"")
        self.sensor5_lbl.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.sensor5_lbl.setMargin(5)
        self.sensor5_lbl.setIndent(0)

        self.gridLayout.addWidget(self.sensor5_lbl, 0, 4, 1, 1)

        self.sensor2_lbl = QLabel(self.main_tab)
        self.sensor2_lbl.setObjectName(u"sensor2_lbl")
        self.sensor2_lbl.setStyleSheet(u"")
        self.sensor2_lbl.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.sensor2_lbl.setMargin(5)
        self.sensor2_lbl.setIndent(0)

        self.gridLayout.addWidget(self.sensor2_lbl, 0, 1, 1, 1)

        self.sensor52_lbl = QLabel(self.main_tab)
        self.sensor52_lbl.setObjectName(u"sensor52_lbl")
        self.sensor52_lbl.setStyleSheet(u"")
        self.sensor52_lbl.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.sensor52_lbl.setMargin(5)
        self.sensor52_lbl.setIndent(0)

        self.gridLayout.addWidget(self.sensor52_lbl, 1, 1, 1, 1)

        self.sensor9_lbl = QLabel(self.main_tab)
        self.sensor9_lbl.setObjectName(u"sensor9_lbl")
        self.sensor9_lbl.setStyleSheet(u"")
        self.sensor9_lbl.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.sensor9_lbl.setMargin(5)
        self.sensor9_lbl.setIndent(0)

        self.gridLayout.addWidget(self.sensor9_lbl, 0, 8, 1, 1)

        self.sensor4_lbl = QLabel(self.main_tab)
        self.sensor4_lbl.setObjectName(u"sensor4_lbl")
        self.sensor4_lbl.setStyleSheet(u"")
        self.sensor4_lbl.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.sensor4_lbl.setMargin(5)
        self.sensor4_lbl.setIndent(0)

        self.gridLayout.addWidget(self.sensor4_lbl, 0, 3, 1, 1)

        self.sensor51_lbl = QLabel(self.main_tab)
        self.sensor51_lbl.setObjectName(u"sensor51_lbl")
        self.sensor51_lbl.setStyleSheet(u"")
        self.sensor51_lbl.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.sensor51_lbl.setMargin(5)
        self.sensor51_lbl.setIndent(0)

        self.gridLayout.addWidget(self.sensor51_lbl, 1, 0, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.output_table = QTableWidget(self.main_tab)
        self.output_table.setObjectName(u"output_table")
        self.output_table.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.output_table)

        self.tabWidget.addTab(self.main_tab, "")
        self.settings_tab = QWidget()
        self.settings_tab.setObjectName(u"settings_tab")
        self.port_and_ne_dev_groupBox = QGroupBox(self.settings_tab)
        self.port_and_ne_dev_groupBox.setObjectName(u"port_and_ne_dev_groupBox")
        self.port_and_ne_dev_groupBox.setGeometry(QRect(20, 370, 301, 401))
        sizePolicy1.setHeightForWidth(self.port_and_ne_dev_groupBox.sizePolicy().hasHeightForWidth())
        self.port_and_ne_dev_groupBox.setSizePolicy(sizePolicy1)
        self.port_and_ne_dev_groupBox.setStyleSheet(u"")
        self.port_and_net_dev_tableWidget = QTableWidget(self.port_and_ne_dev_groupBox)
        self.port_and_net_dev_tableWidget.setObjectName(u"port_and_net_dev_tableWidget")
        self.port_and_net_dev_tableWidget.setGeometry(QRect(20, 70, 261, 321))
        self.port_and_net_dev_tableWidget.setStyleSheet(u"QHeaderView::section:horizontal {\n"
"    color: #fff;\n"
"    background-color: rgb(0, 85, 127);\n"
" }\n"
"QTableWidget {\n"
"	background-color: rgb(0, 0, 127);\n"
"	color: rgb(85, 255, 0);\n"
"	font: 63 8pt \"Yu Gothic UI Semibold\";\n"
"}\n"
"")
        self.send_table_btn = QPushButton(self.port_and_ne_dev_groupBox)
        self.send_table_btn.setObjectName(u"send_table_btn")
        self.send_table_btn.setGeometry(QRect(20, 30, 151, 23))
        self.send_table_btn.setStyleSheet(u"")
        self.delete_line_btn = QPushButton(self.port_and_ne_dev_groupBox)
        self.delete_line_btn.setObjectName(u"delete_line_btn")
        self.delete_line_btn.setGeometry(QRect(184, 30, 101, 23))
        self.delete_line_btn.setStyleSheet(u"")
        self.ports_groupBox = QGroupBox(self.settings_tab)
        self.ports_groupBox.setObjectName(u"ports_groupBox")
        self.ports_groupBox.setGeometry(QRect(340, 370, 311, 401))
        sizePolicy1.setHeightForWidth(self.ports_groupBox.sizePolicy().hasHeightForWidth())
        self.ports_groupBox.setSizePolicy(sizePolicy1)
        self.ports_groupBox.setStyleSheet(u"")
        self.ports_listWidget = QListWidget(self.ports_groupBox)
        self.ports_listWidget.setObjectName(u"ports_listWidget")
        self.ports_listWidget.setGeometry(QRect(10, 60, 281, 331))
        self.ports_listWidget.setStyleSheet(u"")
        self.get_ports_btn = QPushButton(self.ports_groupBox)
        self.get_ports_btn.setObjectName(u"get_ports_btn")
        self.get_ports_btn.setGeometry(QRect(10, 20, 211, 23))
        self.get_ports_btn.setStyleSheet(u"")
        self.net_dev_groupBox = QGroupBox(self.settings_tab)
        self.net_dev_groupBox.setObjectName(u"net_dev_groupBox")
        self.net_dev_groupBox.setGeometry(QRect(670, 370, 251, 401))
        sizePolicy1.setHeightForWidth(self.net_dev_groupBox.sizePolicy().hasHeightForWidth())
        self.net_dev_groupBox.setSizePolicy(sizePolicy1)
        self.net_dev_groupBox.setStyleSheet(u"")
        self.net_dev_listWidget = QListWidget(self.net_dev_groupBox)
        self.net_dev_listWidget.setObjectName(u"net_dev_listWidget")
        self.net_dev_listWidget.setGeometry(QRect(10, 60, 231, 331))
        self.net_dev_listWidget.setStyleSheet(u"")
        self.get_net_dev_btn = QPushButton(self.net_dev_groupBox)
        self.get_net_dev_btn.setObjectName(u"get_net_dev_btn")
        self.get_net_dev_btn.setGeometry(QRect(10, 20, 221, 23))
        self.get_net_dev_btn.setStyleSheet(u"")
        self.groupBox_2 = QGroupBox(self.settings_tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(20, 10, 261, 311))
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.groupBox_2.setMinimumSize(QSize(261, 311))
        self.groupBox_2.setStyleSheet(u"")
        self.port_db_lbl = QLabel(self.groupBox_2)
        self.port_db_lbl.setObjectName(u"port_db_lbl")
        self.port_db_lbl.setGeometry(QRect(10, 60, 47, 16))
        self.port_db_lbl.setStyleSheet(u"")
        self.host_db_lbl = QLabel(self.groupBox_2)
        self.host_db_lbl.setObjectName(u"host_db_lbl")
        self.host_db_lbl.setGeometry(QRect(10, 30, 47, 14))
        self.host_db_lbl.setStyleSheet(u"")
        self.user_db_lbl = QLabel(self.groupBox_2)
        self.user_db_lbl.setObjectName(u"user_db_lbl")
        self.user_db_lbl.setGeometry(QRect(10, 90, 51, 16))
        self.user_db_lbl.setStyleSheet(u"")
        self.pass_db_lbl = QLabel(self.groupBox_2)
        self.pass_db_lbl.setObjectName(u"pass_db_lbl")
        self.pass_db_lbl.setGeometry(QRect(10, 120, 61, 16))
        self.pass_db_lbl.setStyleSheet(u"")
        self.name_db_lbl = QLabel(self.groupBox_2)
        self.name_db_lbl.setObjectName(u"name_db_lbl")
        self.name_db_lbl.setGeometry(QRect(10, 150, 61, 16))
        self.name_db_lbl.setStyleSheet(u"")
        self.host_db_lineEdit = QLineEdit(self.groupBox_2)
        self.host_db_lineEdit.setObjectName(u"host_db_lineEdit")
        self.host_db_lineEdit.setGeometry(QRect(110, 30, 141, 20))
        self.host_db_lineEdit.setStyleSheet(u"")
        self.port_db_lineEdit = QLineEdit(self.groupBox_2)
        self.port_db_lineEdit.setObjectName(u"port_db_lineEdit")
        self.port_db_lineEdit.setGeometry(QRect(110, 60, 141, 20))
        self.port_db_lineEdit.setStyleSheet(u"")
        self.user_db_lineEdit = QLineEdit(self.groupBox_2)
        self.user_db_lineEdit.setObjectName(u"user_db_lineEdit")
        self.user_db_lineEdit.setGeometry(QRect(110, 90, 141, 20))
        self.user_db_lineEdit.setStyleSheet(u"")
        self.pass_db_lineEdit = QLineEdit(self.groupBox_2)
        self.pass_db_lineEdit.setObjectName(u"pass_db_lineEdit")
        self.pass_db_lineEdit.setGeometry(QRect(110, 120, 141, 20))
        self.pass_db_lineEdit.setStyleSheet(u"")
        self.name_db_lineEdit = QLineEdit(self.groupBox_2)
        self.name_db_lineEdit.setObjectName(u"name_db_lineEdit")
        self.name_db_lineEdit.setGeometry(QRect(110, 150, 141, 20))
        self.name_db_lineEdit.setStyleSheet(u"")
        self.save_db_btn = QPushButton(self.groupBox_2)
        self.save_db_btn.setObjectName(u"save_db_btn")
        self.save_db_btn.setGeometry(QRect(10, 260, 75, 23))
        self.save_db_btn.setStyleSheet(u"")
        self.check_db_btn = QPushButton(self.groupBox_2)
        self.check_db_btn.setObjectName(u"check_db_btn")
        self.check_db_btn.setGeometry(QRect(10, 200, 241, 31))
        self.check_db_btn.setStyleSheet(u"")
        self.join_btn = QPushButton(self.settings_tab)
        self.join_btn.setObjectName(u"join_btn")
        self.join_btn.setGeometry(QRect(590, 320, 151, 23))
        self.join_btn.setStyleSheet(u"")
        self.tabWidget.addTab(self.settings_tab, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(whatsthis)
        self.groupBox.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0414\u043b\u044f \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u044f \u0434\u0430\u0442\u0447\u0438\u043a\u0430 \u043d\u0443\u0436\u043d\u043e \u0432\u044b\u0431\u0440\u0430\u0442\u044c \u0434\u0430\u0442\u0447\u0438\u043a \u0432 \u0442\u0430\u0431\u043b\u0438\u0446\u0435 \u0438 \u043d\u0430\u0436\u0430\u0442\u044c \u043d\u0430 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u044e\u0449\u0443\u044e \u043a\u043d\u043e\u043f\u043a\u0443 \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u044f.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u044f \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0433\u043e \u0434\u0430\u0442\u0447\u0438\u043a\u0430.", None))
        self.normal_btn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0440\u043c\u0430", None))
        self.fire_btn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0436\u0430\u0440", None))
        self.failure_btn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0438\u0441\u043f\u0440\u0430\u0432\u043d\u043e\u0441\u0442\u044c", None))
        self.kz_r_btn.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0417", None))
        self.break_r_btn.setText(QCoreApplication.translate("MainWindow", u"\u043e\u0431\u0440\u044b\u0432", None))
#if QT_CONFIG(tooltip)
        self.option_r_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041f\u043e\u043a\u0430 \u0442\u043e\u043b\u044c\u043a\u043e \u0434\u043b\u044f  \u0410\u04201 \u041e\u043f\u0446\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u0430\u044f \u043d\u0435\u0438\u0441\u043f\u0440\u0430\u0432\u043d\u043e\u0441\u0442\u044c \u0434\u0430\u0442\u0447\u0438\u043a\u0430.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.option_r_btn.setText(QCoreApplication.translate("MainWindow", u"\u043e\u043f\u0446\u0438\u044f", None))
        self.sensor58_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0410\u041e\u041f\u0418\n"
"\n"
"58", None))
        self.sensor57_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0422\u0418\n"
"\n"
"57", None))
        self.sensor6_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0418\u041f\u042d\u0421\n"
"\n"
"6", None))
        self.sensor7_lbl.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0418\u041f\n"
"\n"
"7", None))
        self.sensor1_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0418\u041f-535\n"
"\n"
"1", None))
        self.sensor67_lbl.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0421\u04179\n"
"\n"
"67", None))
        self.sensor8_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0418\u041f\u0410\n"
"\n"
"8", None))
        self.sensor62_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0421\u041c-22-1\n"
"\n"
"62", None))
        self.sensor54_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0420-1\n"
"\n"
"54", None))
        self.sensor66_lbl.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0421\u0417\n"
"\n"
"66", None))
        self.sensor59_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0420\u0421\n"
"\n"
"59", None))
        self.sensor65_lbl.setText(QCoreApplication.translate("MainWindow", u"\u041c\u041a\u0417\n"
"\n"
"65", None))
        self.sensor53_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0410\u041c\u041a\n"
"\n"
"53", None))
        self.sensor61_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0421\u041c-5\n"
"\n"
"61", None))
        self.sensor64_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0421\u041c-220\n"
"\n"
"64", None))
        self.sensor60_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0420-\u041f\n"
"\n"
"60", None))
        self.sensor56_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0420\u041c\u0438\u043d\u0438\n"
"\n"
"56", None))
        self.sensor63_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0421\u041c-22-2\n"
"\n"
"63", None))
        self.sensor3_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0418\u041f-101\n"
"\n"
"3", None))
        self.sensor55_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0420-5\n"
"\n"
"55", None))
        self.sensor5_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0418\u041f-329\n"
"\u0424\u0435\u043d\u0438\u043a\u0441\n"
"5", None))
        self.sensor2_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0418\u041f\u041f\n"
"\u0413\u0435\u043b\u0438\u043e\u0441\n"
"2", None))
        self.sensor52_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0412\u0418\n"
"\n"
"52", None))
        self.sensor9_lbl.setText(QCoreApplication.translate("MainWindow", u"NLS\n"
"\n"
"9", None))
        self.sensor4_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0418\u041f-330\n"
"\u041a\u0440\u0435\u0447\u0435\u0442\n"
"4", None))
        self.sensor51_lbl.setText(QCoreApplication.translate("MainWindow", u"\u04102\u0414\u041f\u0418\n"
"\n"
"51", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.main_tab), QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430 \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432", None))
        self.port_and_ne_dev_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Port -> Net Device", None))
        self.send_table_btn.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u044d\u043c\u0443\u043b\u044f\u0442\u043e\u0440", None))
        self.delete_line_btn.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.ports_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0440\u0442\u044b", None))
        self.get_ports_btn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0441\u043f\u0438\u0441\u043e\u043a \u043f\u043e\u0440\u0442\u043e\u0432", None))
        self.net_dev_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0442\u0435\u0432\u044b\u0435 \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u0430", None))
        self.get_net_dev_btn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0441\u043f\u0438\u0441\u043e\u043a \u0441\u0435\u0442\u0435\u0432\u044b\u0445 \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f \u043a \u0431\u0430\u0437\u0435 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.port_db_lbl.setText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.host_db_lbl.setText(QCoreApplication.translate("MainWindow", u"Host", None))
        self.user_db_lbl.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.pass_db_lbl.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.name_db_lbl.setText(QCoreApplication.translate("MainWindow", u"Name DB", None))
#if QT_CONFIG(tooltip)
        self.host_db_lineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0410\u0434\u0440\u0435\u0441 (IP4) \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f \u043a \u0411\u0414</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.host_db_lineEdit.setInputMask(QCoreApplication.translate("MainWindow", u"000\\.000\\.000\\.000", None))
        self.host_db_lineEdit.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.port_db_lineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041d\u043e\u043c\u0435\u0440 \u043f\u043e\u0440\u0442\u0430 \u0434\u043e\u043b\u0436\u0435\u043d \u0431\u044b\u0442\u044c \u0432 \u0434\u0438\u0430\u043f\u0430\u0437\u043e\u043d\u0435 <span style=\" font-family:'JetBrains Mono','monospace'; font-size:10pt; font-weight:600; font-style:italic; color:#ff0000;\">1024-49151</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.port_db_lineEdit.setInputMask(QCoreApplication.translate("MainWindow", u"00009", None))
        self.port_db_lineEdit.setText("")
#if QT_CONFIG(tooltip)
        self.user_db_lineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041b\u043e\u0433\u0438\u043d \u0431\u0430\u0437\u044b \u0434\u0430\u043d\u043d\u044b\u0445</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.user_db_lineEdit.setText("")
#if QT_CONFIG(tooltip)
        self.pass_db_lineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041f\u0430\u0440\u043e\u043b\u044c \u0431\u0430\u0437\u044b \u0434\u0430\u043d\u043d\u044b\u0445</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pass_db_lineEdit.setText("")
#if QT_CONFIG(tooltip)
        self.name_db_lineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0418\u043c\u044f \u0431\u0430\u0437\u044b \u0434\u0430\u043d\u043d\u044b\u0445</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.name_db_lineEdit.setText("")
#if QT_CONFIG(tooltip)
        self.save_db_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0421\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u0435 \u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043a \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.save_db_btn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(tooltip)
        self.check_db_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041f\u0440\u043e\u0432\u0435\u0440\u043a\u0430 \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f \u043a \u0431\u0430\u0437\u0435 \u0434\u0430\u043d\u043d\u044b\u0445</p><p>\u041d\u0435 \u0440\u0430\u0431\u043e\u0442\u0430\u0435\u0442</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.check_db_btn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f", None))
        self.join_btn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u044a\u0435\u0434\u0438\u043d\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings_tab), QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
    # retranslateUi

