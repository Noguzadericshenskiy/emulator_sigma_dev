import os
import re
import json

from PySide6.QtGui import QValidator
from serial.tools import list_ports_windows
from typing import Any

DEFAULT_CONNECT = {
    "parameters_connect_db": {
        "user": "postgres",
        "password": "postgres",
        "name": "idspoconfig",
        "host": "127.0.0.1",
        "port": "5432"
    },
    "config_devices": []
}
PATH = "setup.json"

class NumbersIPValidator(QValidator):
    """Проверка введенного IP
    значение должно соответствовать 255.255.255.255
    """
    def validate(self, string: str, index: int) -> object:
        # try:
            nums_arr = string.split(".")
            if 0 <= int(nums_arr[0]) <= 255 and 0 <= int(nums_arr[1]) <= 255 and \
                    0 <= int(nums_arr[2]) <= 255 and 0 <= int(nums_arr[3]) <= 255:
                return QValidator.State.Acceptable, string, index
            else:
                return QValidator.State.Invalid, string, index


class PortValidator(QValidator):
    """Проверка номера порта
        Значение должно быть в пределе 1024-49151
        или макс. 65535?
    """
    def validate(self, string: str, index: int) -> object:
        if 1024 < int(string) <= 49151:
            return QValidator.State.Acceptable, string, index
        else:
            return QValidator.State.Invalid, string, index


def get_ports_info() -> list[Any]:
    "Получить список портов"
    ports = []
    usb_port = list_ports_windows.comports()
    for i_port in usb_port:
        ports.append((i_port.device, i_port.description))
    return ports


def get_net_devices() -> list[Any]:
    """Получить список сетевых контроллеров"""
    return ["KA2", "CKAU03D"]


def check_join_table_output(port: str, net_dev: str, ports_net_devs: list[tuple]) -> bool:
    """Проверка объединенной таблицы на задвоенные параметры (ранее используемые)
    """
    for record in ports_net_devs:
        if record[0] == port or record[1] == net_dev:
            return False
    return True


def check_file():
    if not os.path.exists(PATH):
        with open(PATH, "x") as file:
            json.dump(DEFAULT_CONNECT, file)


def save_conn_to_file(params):
    data = None
    with open(PATH, "r") as file:
        data = json.load(file)
        data["parameters_connect_db"] = params
    with open(PATH, "w") as file:
        json.dump(data, file)


def get_conn_from_file() -> dict:
    with open(PATH, "r") as file:
        data = json.load(file)
        return data["parameters_connect_db"]

