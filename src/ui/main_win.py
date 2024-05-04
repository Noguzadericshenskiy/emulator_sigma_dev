# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_win_v1.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1174, 835)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 85, 127);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(1291, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QTabWidget {\n"
"	\n"
"	border-color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-left: 1px solid rgb(0, 83, 122);\n"
"	border-top: 1px solid rgb(0, 83, 122);\n"
"	border-right: 1px solid rgb(0, 50, 74);	\n"
"	border-bottom: 1px solid rgb(0, 50, 74);\n"
"}\n"
"\n"
"QTabBar {\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTabBar::tab:selected  {\n"
"    background-color:rgb(0, 0, 127);\n"
"	color: rgb(85, 255, 0);\n"
"}\n"
"")
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.main_tab = QWidget()
        self.main_tab.setObjectName(u"main_tab")
        self.horizontalLayout_3 = QHBoxLayout(self.main_tab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.output_table = QTableWidget(self.main_tab)
        self.output_table.setObjectName(u"output_table")
        self.output_table.setStyleSheet(u"QHeaderView::section:horizontal {\n"
"    color: #fff;\n"
"    background-color: rgb(0, 85, 127);\n"
" }\n"
"QTableWidget {\n"
"	background-color: rgb(0, 0, 127);\n"
"	color: rgb(85, 255, 0);\n"
"	font: 63 8pt \"Yu Gothic UI Semibold\";\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.output_table, 2, 1, 1, 3)

        self.groupBox = QGroupBox(self.main_tab)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setStyleSheet(u"QGroupBox {\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"}\n"
"")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.normal_btn = QPushButton(self.groupBox)
        self.normal_btn.setObjectName(u"normal_btn")
        sizePolicy.setHeightForWidth(self.normal_btn.sizePolicy().hasHeightForWidth())
        self.normal_btn.setSizePolicy(sizePolicy)
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

        self.fire_btn = QPushButton(self.groupBox)
        self.fire_btn.setObjectName(u"fire_btn")
        sizePolicy.setHeightForWidth(self.fire_btn.sizePolicy().hasHeightForWidth())
        self.fire_btn.setSizePolicy(sizePolicy)
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

        self.failure_btn = QPushButton(self.groupBox)
        self.failure_btn.setObjectName(u"failure_btn")
        sizePolicy.setHeightForWidth(self.failure_btn.sizePolicy().hasHeightForWidth())
        self.failure_btn.setSizePolicy(sizePolicy)
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


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 1, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.radioButton = QRadioButton(self.main_tab)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout_4.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.main_tab)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_4.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.main_tab)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout_4.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.main_tab)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.horizontalLayout_4.addWidget(self.radioButton_4)

        self.radioButton_5 = QRadioButton(self.main_tab)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.horizontalLayout_4.addWidget(self.radioButton_5)

        self.radioButton_6 = QRadioButton(self.main_tab)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.horizontalLayout_4.addWidget(self.radioButton_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.ipr_label = QLabel(self.main_tab)
        self.ipr_label.setObjectName(u"ipr_label")
        self.ipr_label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.ipr_label)

        self.ip_101_lbl = QLabel(self.main_tab)
        self.ip_101_lbl.setObjectName(u"ip_101_lbl")
        self.ip_101_lbl.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.ip_101_lbl)

        self.label_12 = QLabel(self.main_tab)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.label_12)

        self.label_4 = QLabel(self.main_tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.label_10 = QLabel(self.main_tab)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.label_10)

        self.label_6 = QLabel(self.main_tab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.label_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 2, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout_2)

        self.tabWidget.addTab(self.main_tab, "")
        self.settings_tab = QWidget()
        self.settings_tab.setObjectName(u"settings_tab")
        self.groupBox_3 = QGroupBox(self.settings_tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(350, 10, 331, 91))
        self.groupBox_3.setStyleSheet(u"QGroupBox {\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_3 = QPushButton(self.groupBox_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(10, 20, 137, 18))
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color: rgb(255, 255, 127);\n"
"	border: none;\n"
"	border-left: 2px solid rgb(0, 83, 122);\n"
"	border-top: 2px solid rgb(0, 83, 122);\n"
"	border-right: 2px solid rgb(0, 50, 74);	\n"
"	border-bottom: 2px solid rgb(0, 50, 74);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color:rgb(0, 255, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color: rgb(0, 255, 0);\n"
"	border-left: 2px solid rgb(0, 64, 94);\n"
"	border-top: 2px solid rgb(0, 64, 94);\n"
"	border-right: 2px solid rgb(0, 83, 122);	\n"
"	border-bottom: 2px solid rgb(0, 83, 122);\n"
"}")
        self.pushButton_4 = QPushButton(self.groupBox_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(10, 50, 137, 18))
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color: rgb(255, 255, 127);\n"
"	border: none;\n"
"	border-left: 2px solid rgb(0, 83, 122);\n"
"	border-top: 2px solid rgb(0, 83, 122);\n"
"	border-right: 2px solid rgb(0, 50, 74);	\n"
"	border-bottom: 2px solid rgb(0, 50, 74);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color:rgb(0, 255, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color: rgb(0, 255, 0);\n"
"	border-left: 2px solid rgb(0, 64, 94);\n"
"	border-top: 2px solid rgb(0, 64, 94);\n"
"	border-right: 2px solid rgb(0, 83, 122);	\n"
"	border-bottom: 2px solid rgb(0, 83, 122);\n"
"}")
        self.port_and_ne_dev_groupBox = QGroupBox(self.settings_tab)
        self.port_and_ne_dev_groupBox.setObjectName(u"port_and_ne_dev_groupBox")
        self.port_and_ne_dev_groupBox.setGeometry(QRect(20, 370, 301, 401))
        self.port_and_ne_dev_groupBox.setStyleSheet(u"QGroupBox {\n"
"	color: rgb(255, 255, 255);\n"
"	font: 10pt \"Tahoma\";\n"
"}")
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
        self.send_table_btn.setGeometry(QRect(30, 30, 231, 23))
        self.send_table_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color: rgb(255, 255, 127);\n"
"	border: none;\n"
"	border-left: 2px solid rgb(0, 83, 122);\n"
"	border-top: 2px solid rgb(0, 83, 122);\n"
"	border-right: 2px solid rgb(0, 50, 74);	\n"
"	border-bottom: 2px solid rgb(0, 50, 74);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color:rgb(0, 255, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color: rgb(0, 255, 0);\n"
"	border-left: 2px solid rgb(0, 64, 94);\n"
"	border-top: 2px solid rgb(0, 64, 94);\n"
"	border-right: 2px solid rgb(0, 83, 122);	\n"
"	border-bottom: 2px solid rgb(0, 83, 122);\n"
"}")
        self.ports_groupBox = QGroupBox(self.settings_tab)
        self.ports_groupBox.setObjectName(u"ports_groupBox")
        self.ports_groupBox.setGeometry(QRect(360, 370, 241, 401))
        self.ports_groupBox.setStyleSheet(u"QGroupBox {\n"
"	color: rgb(255, 255, 255);\n"
"	font: 10pt \"Tahoma\";\n"
"}")
        self.ports_listWidget = QListWidget(self.ports_groupBox)
        self.ports_listWidget.setObjectName(u"ports_listWidget")
        self.ports_listWidget.setGeometry(QRect(10, 60, 211, 331))
        self.get_ports_btn = QPushButton(self.ports_groupBox)
        self.get_ports_btn.setObjectName(u"get_ports_btn")
        self.get_ports_btn.setGeometry(QRect(10, 20, 211, 23))
        self.get_ports_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color: rgb(255, 255, 127);\n"
"	border: none;\n"
"	border-left: 2px solid rgb(0, 83, 122);\n"
"	border-top: 2px solid rgb(0, 83, 122);\n"
"	border-right: 2px solid rgb(0, 50, 74);	\n"
"	border-bottom: 2px solid rgb(0, 50, 74);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color:rgb(0, 255, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color: rgb(0, 255, 0);\n"
"	border-left: 2px solid rgb(0, 64, 94);\n"
"	border-top: 2px solid rgb(0, 64, 94);\n"
"	border-right: 2px solid rgb(0, 83, 122);	\n"
"	border-bottom: 2px solid rgb(0, 83, 122);\n"
"}")
        self.net_dev_groupBox = QGroupBox(self.settings_tab)
        self.net_dev_groupBox.setObjectName(u"net_dev_groupBox")
        self.net_dev_groupBox.setGeometry(QRect(630, 370, 251, 401))
        self.net_dev_groupBox.setStyleSheet(u"QGroupBox {\n"
"	color: rgb(255, 255, 255);\n"
"	font: 10pt \"Tahoma\";\n"
"}")
        self.net_dev_listWidget = QListWidget(self.net_dev_groupBox)
        self.net_dev_listWidget.setObjectName(u"net_dev_listWidget")
        self.net_dev_listWidget.setGeometry(QRect(10, 60, 231, 331))
        self.get_net_dev_btn = QPushButton(self.net_dev_groupBox)
        self.get_net_dev_btn.setObjectName(u"get_net_dev_btn")
        self.get_net_dev_btn.setGeometry(QRect(10, 20, 221, 23))
        self.get_net_dev_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color: rgb(255, 255, 127);\n"
"	border: none;\n"
"	border-left: 2px solid rgb(0, 83, 122);\n"
"	border-top: 2px solid rgb(0, 83, 122);\n"
"	border-right: 2px solid rgb(0, 50, 74);	\n"
"	border-bottom: 2px solid rgb(0, 50, 74);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color:rgb(0, 255, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color: rgb(0, 255, 0);\n"
"	border-left: 2px solid rgb(0, 64, 94);\n"
"	border-top: 2px solid rgb(0, 64, 94);\n"
"	border-right: 2px solid rgb(0, 83, 122);	\n"
"	border-bottom: 2px solid rgb(0, 83, 122);\n"
"}")
        self.pushButton_2 = QPushButton(self.settings_tab)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(390, 140, 271, 18))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color: rgb(255, 255, 127);\n"
"	border: none;\n"
"	border-left: 2px solid rgb(0, 83, 122);\n"
"	border-top: 2px solid rgb(0, 83, 122);\n"
"	border-right: 2px solid rgb(0, 50, 74);	\n"
"	border-bottom: 2px solid rgb(0, 50, 74);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color:rgb(0, 255, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color: rgb(0, 255, 0);\n"
"	border-left: 2px solid rgb(0, 64, 94);\n"
"	border-top: 2px solid rgb(0, 64, 94);\n"
"	border-right: 2px solid rgb(0, 83, 122);	\n"
"	border-bottom: 2px solid rgb(0, 83, 122);\n"
"}")
        self.groupBox_2 = QGroupBox(self.settings_tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(20, 10, 311, 311))
        self.groupBox_2.setStyleSheet(u"QGroupBox {\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.port_db_lbl = QLabel(self.groupBox_2)
        self.port_db_lbl.setObjectName(u"port_db_lbl")
        self.port_db_lbl.setGeometry(QRect(10, 60, 47, 16))
        self.port_db_lbl.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.host_db_lbl = QLabel(self.groupBox_2)
        self.host_db_lbl.setObjectName(u"host_db_lbl")
        self.host_db_lbl.setGeometry(QRect(10, 30, 47, 14))
        self.host_db_lbl.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.user_db_lbl = QLabel(self.groupBox_2)
        self.user_db_lbl.setObjectName(u"user_db_lbl")
        self.user_db_lbl.setGeometry(QRect(10, 90, 47, 14))
        self.user_db_lbl.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.pass_db_lbl = QLabel(self.groupBox_2)
        self.pass_db_lbl.setObjectName(u"pass_db_lbl")
        self.pass_db_lbl.setGeometry(QRect(10, 120, 47, 14))
        self.pass_db_lbl.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.name_db_lbl = QLabel(self.groupBox_2)
        self.name_db_lbl.setObjectName(u"name_db_lbl")
        self.name_db_lbl.setGeometry(QRect(10, 150, 47, 14))
        self.name_db_lbl.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.host_db_lineEdit = QLineEdit(self.groupBox_2)
        self.host_db_lineEdit.setObjectName(u"host_db_lineEdit")
        self.host_db_lineEdit.setGeometry(QRect(110, 30, 141, 20))
        self.host_db_lineEdit.setStyleSheet(u"QLineEdit {\n"
"background-color: rgb(0, 74, 109);\n"
"color: rgb(4, 255, 0);\n"
"}\n"
"\n"
"QToolTip {\n"
"	color: rgb(0, 0, 127);\n"
"}")
        self.port_db_lineEdit = QLineEdit(self.groupBox_2)
        self.port_db_lineEdit.setObjectName(u"port_db_lineEdit")
        self.port_db_lineEdit.setGeometry(QRect(110, 60, 141, 20))
        self.port_db_lineEdit.setStyleSheet(u"QLineEdit {\n"
"background-color: rgb(0, 74, 109);\n"
"color: rgb(4, 255, 0);\n"
"}\n"
"\n"
"QToolTip {\n"
"	color: rgb(0, 0, 127);\n"
"}")
        self.user_db_lineEdit = QLineEdit(self.groupBox_2)
        self.user_db_lineEdit.setObjectName(u"user_db_lineEdit")
        self.user_db_lineEdit.setGeometry(QRect(110, 90, 141, 20))
        self.user_db_lineEdit.setStyleSheet(u"QLineEdit {\n"
"background-color: rgb(0, 74, 109);\n"
"color: rgb(4, 255, 0);\n"
"}\n"
"\n"
"QToolTip {\n"
"	color: rgb(0, 0, 127);\n"
"}")
        self.pass_db_lineEdit = QLineEdit(self.groupBox_2)
        self.pass_db_lineEdit.setObjectName(u"pass_db_lineEdit")
        self.pass_db_lineEdit.setGeometry(QRect(110, 120, 141, 20))
        self.pass_db_lineEdit.setStyleSheet(u"QLineEdit {\n"
"background-color: rgb(0, 74, 109);\n"
"color: rgb(4, 255, 0);\n"
"}\n"
"\n"
"QToolTip {\n"
"	color: rgb(0, 0, 127);\n"
"}")
        self.name_db_lineEdit = QLineEdit(self.groupBox_2)
        self.name_db_lineEdit.setObjectName(u"name_db_lineEdit")
        self.name_db_lineEdit.setGeometry(QRect(110, 150, 141, 20))
        self.name_db_lineEdit.setStyleSheet(u"QLineEdit {\n"
"background-color: rgb(0, 74, 109);\n"
"color: rgb(4, 255, 0);\n"
"}\n"
"\n"
"QToolTip {\n"
"	color: rgb(0, 0, 127);\n"
"}")
        self.save_db_btn = QPushButton(self.groupBox_2)
        self.save_db_btn.setObjectName(u"save_db_btn")
        self.save_db_btn.setGeometry(QRect(10, 260, 75, 23))
        self.save_db_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color: rgb(255, 255, 127);\n"
"	border: none;\n"
"	border-left: 2px solid rgb(0, 83, 122);\n"
"	border-top: 2px solid rgb(0, 83, 122);\n"
"	border-right: 2px solid rgb(0, 50, 74);	\n"
"	border-bottom: 2px solid rgb(0, 50, 74);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color:rgb(0, 255, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color: rgb(0, 255, 0);\n"
"	border-left: 2px solid rgb(0, 64, 94);\n"
"	border-top: 2px solid rgb(0, 64, 94);\n"
"	border-right: 2px solid rgb(0, 83, 122);	\n"
"	border-bottom: 2px solid rgb(0, 83, 122);\n"
"}")
        self.cancel_db_btn = QPushButton(self.groupBox_2)
        self.cancel_db_btn.setObjectName(u"cancel_db_btn")
        self.cancel_db_btn.setGeometry(QRect(110, 260, 75, 23))
        self.cancel_db_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color: rgb(255, 255, 127);\n"
"	border: none;\n"
"	border-left: 2px solid rgb(0, 83, 122);\n"
"	border-top: 2px solid rgb(0, 83, 122);\n"
"	border-right: 2px solid rgb(0, 50, 74);	\n"
"	border-bottom: 2px solid rgb(0, 50, 74);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color:rgb(0, 255, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color: rgb(0, 255, 0);\n"
"	border-left: 2px solid rgb(0, 64, 94);\n"
"	border-top: 2px solid rgb(0, 64, 94);\n"
"	border-right: 2px solid rgb(0, 83, 122);	\n"
"	border-bottom: 2px solid rgb(0, 83, 122);\n"
"}")
        self.check_db_btn = QPushButton(self.groupBox_2)
        self.check_db_btn.setObjectName(u"check_db_btn")
        self.check_db_btn.setGeometry(QRect(10, 200, 281, 31))
        self.check_db_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color: rgb(255, 255, 127);\n"
"	border: none;\n"
"	border-left: 2px solid rgb(0, 83, 122);\n"
"	border-top: 2px solid rgb(0, 83, 122);\n"
"	border-right: 2px solid rgb(0, 50, 74);	\n"
"	border-bottom: 2px solid rgb(0, 50, 74);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color:rgb(0, 255, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color: rgb(0, 255, 0);\n"
"	border-left: 2px solid rgb(0, 64, 94);\n"
"	border-top: 2px solid rgb(0, 64, 94);\n"
"	border-right: 2px solid rgb(0, 83, 122);	\n"
"	border-bottom: 2px solid rgb(0, 83, 122);\n"
"}")
        self.pushButton = QPushButton(self.settings_tab)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(390, 110, 271, 18))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color: rgb(255, 255, 127);\n"
"	border: none;\n"
"	border-left: 2px solid rgb(0, 83, 122);\n"
"	border-top: 2px solid rgb(0, 83, 122);\n"
"	border-right: 2px solid rgb(0, 50, 74);	\n"
"	border-bottom: 2px solid rgb(0, 50, 74);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color:rgb(0, 255, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color: rgb(0, 255, 0);\n"
"	border-left: 2px solid rgb(0, 64, 94);\n"
"	border-top: 2px solid rgb(0, 64, 94);\n"
"	border-right: 2px solid rgb(0, 83, 122);	\n"
"	border-bottom: 2px solid rgb(0, 83, 122);\n"
"}")
        self.join_btn = QPushButton(self.settings_tab)
        self.join_btn.setObjectName(u"join_btn")
        self.join_btn.setGeometry(QRect(570, 340, 91, 23))
        self.join_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color: rgb(255, 255, 127);\n"
"	border: none;\n"
"	border-left: 2px solid rgb(0, 83, 122);\n"
"	border-top: 2px solid rgb(0, 83, 122);\n"
"	border-right: 2px solid rgb(0, 50, 74);	\n"
"	border-bottom: 2px solid rgb(0, 50, 74);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color:rgb(0, 255, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 74, 109);\n"
"	color: rgb(0, 255, 0);\n"
"	border-left: 2px solid rgb(0, 64, 94);\n"
"	border-top: 2px solid rgb(0, 64, 94);\n"
"	border-right: 2px solid rgb(0, 83, 122);	\n"
"	border-bottom: 2px solid rgb(0, 83, 122);\n"
"}")
        self.tabWidget.addTab(self.settings_tab, "")

        self.verticalLayout_3.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u042d\u043c\u0443\u043b\u044f\u0442\u043e\u0440 \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432 ModBus & Sigma", None))
#if QT_CONFIG(whatsthis)
        self.groupBox.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0414\u043b\u044f \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u044f \u0434\u0430\u0442\u0447\u0438\u043a\u0430 \u043d\u0443\u0436\u043d\u043e \u0432\u044b\u0431\u0440\u0430\u0442\u044c \u0434\u0430\u0442\u0447\u0438\u043a \u0432 \u0442\u0430\u0431\u043b\u0438\u0446\u0435 \u0438 \u043d\u0430\u0436\u0430\u0442\u044c \u043d\u0430 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u044e\u0449\u0443\u044e \u043a\u043d\u043e\u043f\u043a\u0443 \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u044f.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u044f \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0433\u043e \u0434\u0430\u0442\u0447\u0438\u043a\u0430.", None))
        self.normal_btn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0440\u043c\u0430", None))
        self.fire_btn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0436\u0430\u0440", None))
        self.failure_btn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0438\u0441\u043f\u0440\u0430\u0432\u043d\u043e\u0441\u0442\u044c", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.ipr_label.setText(QCoreApplication.translate("MainWindow", u"\u0418\u041f\u0420", None))
        self.ip_101_lbl.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.main_tab), QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430 \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0444\u0438\u0433\u0443\u0440\u0430\u0446\u0438\u044f", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u043e\u043d\u0444\u0438\u0433\u0443\u0440\u0430\u0446\u0438\u044e", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u043a\u043e\u043d\u0444\u0438\u0433\u0443\u0440\u0430\u0446\u0438\u044e", None))
        self.port_and_ne_dev_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Port -> Net Device", None))
        self.send_table_btn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043b\u043e\u0436\u0438\u0442\u044c \u043f\u0440\u043e\u043a\u043b\u044f\u0442\u044c\u0435, \u0432\u044b\u0431\u0440\u0430\u0442\u044c \u0437\u0430\u043a\u043b\u0438\u043d\u0430\u043d\u0438\u0435", None))
        self.ports_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Ports", None))
        self.get_ports_btn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0441\u043f\u0438\u0441\u043e\u043a \u043f\u043e\u0440\u0442\u043e\u0432", None))
        self.net_dev_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Net devices", None))
        self.get_net_dev_btn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0441\u043f\u0438\u0441\u043e\u043a \u0441\u0435\u0442\u0435\u0432\u044b\u0445 \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043f\u043e\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043f\u043e\u0440\u0442\u043e\u0432 \u0438 \u0441\u0435\u0442\u0435\u0432\u044b\u0445 \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f \u043a \u0431\u0430\u0437\u0435 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.port_db_lbl.setText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.host_db_lbl.setText(QCoreApplication.translate("MainWindow", u"Host", None))
        self.user_db_lbl.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.pass_db_lbl.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.name_db_lbl.setText(QCoreApplication.translate("MainWindow", u"Name DB", None))
        self.save_db_btn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.cancel_db_btn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.check_db_btn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f \u043a \u0431\u0430\u0437\u0435 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.join_btn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0436\u0435\u043d\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings_tab), QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
    # retranslateUi

