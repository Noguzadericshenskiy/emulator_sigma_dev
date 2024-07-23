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


class ServerMB(QThread):
    """
    Эмулятор адресных устройств ModBus на один порт
        передается конфигурация устройств 1 ряда виджета .
    :param name: название потока = port name
    :param devices: адресные устройства ModBus
    """
    def __init__(self, sensors, name,):
        """
        :param sensors: [{'type': "NLS-16", 'state': 'N', 'slave': '4', 'row': 0, 'column': 2},{}]
        :param name: str "COM1"
        """
        super().__init__()
        self.slaves = {}
        self.context = None
        self.name = name
        self.sensors = sensors
        self.daemon = True

    def run(self) -> None:
        self.slaves = self._create_slaves()
        self.context = ModbusServerContext(slaves=self.slaves, single=False)
        asyncio.run(self._run_server())

    async def _run_server(self):
        server = await StartAsyncSerialServer(
            context=self.context,
            port=self.name,
            stopbits=1,
            parity="N",
            baudrate=9600,
            # framer=ModbusRtuFramer,
        )
        return server

    def _create_slaves(self):
        slaves = {}
        count_num = 1
        store = None
        logger.info(self.sensors)
        for sensor in self.sensors:
            match sensor["type"]:
                case "ИП-535 (Эридан)":
                    store = states_ip_535_07ea_rs(sensor["state_cod"], count_num, sensor["slave"],)
                case "ИП Гелиос 3ИК (Эридан)":
                    store = states_ipp_helios(sensor["state_cod"], count_num, sensor["slave"])
                case "ИП-101 (Эридан)":
                    store = states_ip_101(sensor["state_cod"], count_num, sensor["slave"])
                case "ИП Кречет":
                    store = states_ip_330_zik_krechet(sensor["state_cod"], count_num, sensor["slave"])
                case "ИП Феникс":
                    store = state_ip_329_330_phoenix(sensor["state_cod"], count_num, sensor["slave"])
                case "ИПЭС ИК-УФ":
                    store = state_ipes_ik_uf(sensor["state_cod"], count_num, sensor["slave"])
                case "МИП 3И":
                    store = states_mip(sensor["state_cod"], count_num, sensor["slave"])
                case "ИПА V5":
                    store = state_ipa(sensor["state_cod"], count_num, sensor["slave"])
                case "NLS-16":
                    store = states_nls(sensor["state_cod"], count_num, sensor["slave"])
                case _:
                    logger.info(sensor["type"])

            slaves[sensor["slave"]] = store
            count_num += 1
        return slaves

    def changing_state(self, params: dict) -> None:
        """
        :param pqrams: dict параметры датчика
        """
        type_sensor = params["type"]
        status = params["state_cod"]
        slave = params["slave"]

        match type_sensor:
            case "ИП-535 (Эридан)":
                self.slaves[slave] = states_ip_535_07ea_rs(status, 100, slave)
            case "ИП Гелиос 3ИК (Эридан)":
                self.slaves[slave] = states_ipp_helios(status, 100, slave)
            case "ИП-101 (Эридан)":
                self.slaves[slave] = states_ip_101(status, 100, slave)
            case "ИП Кречет":
                self.slaves[slave] = states_ip_330_zik_krechet(status, 100, slave)
            case "ИП Феникс":
                self.slaves[slave] = state_ip_329_330_phoenix(status, 100, slave)
            case "ИПЭС ИК-УФ":
                self.slaves[slave] = state_ipes_ik_uf(status, 100, slave)
            case "МИП 3И":
                self.slaves[slave] = states_mip(status, 100, slave)
            case "ИПА V5":
                self.slaves[slave] = state_ipa(status, 100, slave)
            case "NLS-16":
                self.slaves[slave] = states_nls(status, 100, slave)
            case _:
                logger.info(f"Нет сенсора {params}")




