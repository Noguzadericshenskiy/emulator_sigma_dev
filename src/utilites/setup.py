import os
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
FILE_SETUP_DB = "setup.json"
FILE_CONFIG = "config_dev.json"


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


class SNEmulatorValidator(QValidator):
    def validate(self, sn: str, index: int) -> object:
        if sn.isdigit():
            return QValidator.State.Acceptable, sn, index
        else:
            return QValidator.State.Invalid, sn, index


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
    """Проверка таблицы сетевое устройство-порт на повторы при объединении у СКАУ.
    """
    if net_dev[1] == "SKAU03Config":
        for record in ports_net_devs:
            if record[0] == port or record[1] == net_dev:
                return False
        return True
    else:
        return True


def check_file():
    if not os.path.exists(FILE_SETUP_DB):
        with open(FILE_SETUP_DB, "x") as file:
            json.dump(DEFAULT_CONNECT, file)


def save_conn_to_file(params):
    data = None
    with open(FILE_SETUP_DB, "r") as file:
        data = json.load(file)
        data["parameters_connect_db"] = params
    with open(FILE_SETUP_DB, "w") as file:
        json.dump(data, file)


def get_conn_from_file() -> dict:
    with open(FILE_SETUP_DB, "r") as file:
        data = json.load(file)
        return data["parameters_connect_db"]


def save_config_to_file(conf):
    with open(FILE_CONFIG, "w") as file:
        json.dump(conf, file)


def get_config_from_file() -> dict:
    with open(FILE_CONFIG, "r") as file:
        return json.load(file)
