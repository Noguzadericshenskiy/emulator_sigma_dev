import sys

from PySide6.QtWidgets import QApplication
from src.root_window import MainWindow

from PySide6.QtGui import QColor
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QMainWindow,
    QListWidgetItem,
    QTableWidgetItem,
    QAbstractItemView,
    )
from loguru import logger

from src.ui.main_win import Ui_MainWindow
from src.ui.card_dev import CardDeviceASH, CardDeviceMB
from src.utilites.setup import (
    NumbersIPValidator,
    PortValidator,
    SNEmulatorValidator,
    get_ports_info,
    check_join_table_output,
    save_conn_to_file,
    check_file,
    get_conn_from_file
)
from src.utilites.database import (
    get_net_devices_from_db,
    handler_devices,
    check_conn,
)
from src.utilites.boot_firmware import (
    get_data_from_file,
    boot_firmware,
    get_version,)
from src.utilites.server_mb import ServerMB
from src.utilites.server_ash import ServerAH
from src.utilites.dialogues import (
    err_selection,
    ok_connect,
    err_connect,
    err_selection_port_net_dev,
    open_file
)

from src.ui.button_states import StatesBtn

import time
from serial import Serial
from loguru import logger

from src.utilites.crc import add_crc, crc_ccitt_16_kermit_b
from src.utilites.ash_util import indicate_send_b6

import sqlalchemy
import psycopg2
import operator

from psycopg2 import OperationalError
from sqlalchemy import create_engine, select, Integer, Boolean
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase

from sqlalchemy.dialects.postgresql import BIGINT, VARCHAR
from loguru import logger

from PySide6.QtWidgets import QMessageBox, QFileDialog

import time

from serial import Serial
from PySide6.QtCore import Signal, QThread
from loguru import logger

from src.utilites.crc import crc_ccitt_16_kermit_b, add_crc

import asyncio

from pymodbus.datastore import ModbusServerContext
from pymodbus.framer import ModbusRtuFramer
from pymodbus.server import StartAsyncSerialServer
from PySide6.QtCore import QThread

from loguru import logger

from devices.registers_devises import (
    states_ipp_helios,
    states_ip_535_07ea_rs,
    states_ip_101,
    states_mip,
    states_nls,
    states_ip_330_zik_krechet,
    state_ipes_ik_uf,
    state_ip_329_330_phoenix,
    state_ipa,
)

import os
import json

from PySide6.QtGui import QValidator
from serial.tools import list_ports_windows
from typing import Any

from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PySide6.QtCore import QSize

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

from PySide6.QtCore import QRect
from PySide6.QtWidgets import QPushButton


def include_style(app):
    with open("_internal/src/ui/style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)


if __name__ == "__main__":
    app = QApplication([])
    widget = MainWindow()
    include_style(app)
    widget.show()
    sys.exit(app.exec())
