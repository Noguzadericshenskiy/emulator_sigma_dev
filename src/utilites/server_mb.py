import asyncio

from threading import Thread
from pymodbus.datastore import ModbusServerContext
from pymodbus.framer import ModbusRtuFramer
from pymodbus.server import StartAsyncSerialServer
from PySide6.QtCore import Signal, QThread

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
        :param sensors: [{'type': 1, 'state': 'N', 'slave': '4', 'row': 0, 'column': 2},{}]
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

    def changing_state(self, params: dict) -> None:
        """
        :param pqrams: dict параметры датчика
        """
        type_sensor = params["type"]
        status = params["state"]
        slave = params["slave"]

        match type_sensor:
            case 1:
                self.slaves[slave] = states_ip_535_07ea_rs(status, 100, slave)
            case 2:
                self.slaves[slave] = states_ipp_helios(status, 100, slave)
            case 3:
                self.slaves[slave] = states_ip_101(status, 100, slave)
            case 4:
                self.slaves[slave] = states_ip_330_zik_krechet(status, 100, slave)
            case 5:
                self.slaves[slave] = state_ip_329_330_phoenix(status, 100, slave)
            case 6:
                self.slaves[slave] = state_ipes_ik_uf(status, 100, slave)
            case 7:
                self.slaves[slave] = states_mip(status, 100, slave)
            case 8:
                self.slaves[slave] = state_ipa(status, 100, slave)
            case 9:
                self.slaves[slave] = states_nls(status, 100, slave)
            case 10:
                ...
            case 11:
                ...

    async def _run_server(self):
        server = await StartAsyncSerialServer(
            context=self.context,
            port=self.name,
            stopbits=1,
            parity="N",
            baudrate=9600,
            framer=ModbusRtuFramer,
        )
        return server

    def _create_slaves(self):
        slaves = {}
        count_num = 1
        store = None
        for sensor in self.sensors:
            match sensor["type"]:
                case 1:
                    store = states_ip_535_07ea_rs(sensor["state"], count_num, sensor["slave"],)
                case 2:
                    store = states_ipp_helios(sensor["state"], count_num, sensor["slave"])
                case 3:
                    store = states_ip_101(sensor["state"], count_num, sensor["slave"])
                case 4:
                    store = states_ip_330_zik_krechet(sensor["state"], count_num, sensor["slave"])
                case 5:
                    store = state_ip_329_330_phoenix(sensor["state"], count_num, sensor["slave"])
                case 6:
                    store = state_ipes_ik_uf(sensor["state"], count_num, sensor["slave"])
                case 7:
                    store = states_mip(sensor["state"], count_num, sensor["slave"])
                case 8:
                    store = state_ipa(sensor["state"], count_num, sensor["slave"])
                case 9:
                    store = states_nls(sensor["state"], count_num, sensor["slave"])
                case 11:
                    ...
                case 12:
                    ...


            slaves[sensor["slave"]] = store
            count_num += 1
        return slaves





