import asyncio

from threading import Thread
from pymodbus.datastore import ModbusServerContext, ModbusSlaveContext, ModbusSparseDataBlock
from pymodbus.framer import ModbusRtuFramer
from pymodbus.server import StartAsyncSerialServer

from devices.registers_devises import (
    states_ipp_helios,
    states_ip_535_07ea_rs,
    states_ip_101,
    states_mip,
    states_nls,
    states_ip_330_zik_krechet,
    state_ipes_ik_uf,
    state_ip_329_330_phenix,
    state_ipa,
    a2dpi_sigma,
    ir_sigma,
    mkz_sigma
)


class ServerAH(Thread):
    """Эмулятор адресных устройств АШ Сигма
        передается конфигурация 1 ряда согласно порта из списка.
    :param name: название сетевого контроллера
    :param devices: адресные устройства
    """
    def __init__(self, devices, name, ):
        super().__init__()
        self.slaves = {}
        self.context = None
        self.name = name
        self.devices = devices
        self.daemon = True

    def run(self) -> None:
        ...


class ServerMB(Thread):
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

        if type_sensor == 1:
            # num = self.slaves[slave].
            self.slaves[slave] = states_ip_535_07ea_rs(status, 100, slave)
        elif type_sensor == 2:
            self.slaves[slave] = states_ipp_helios(status, 100, slave)
        elif type_sensor == 3:
            self.slaves[slave] = states_ip_101(status, 100, slave)
        elif type_sensor == 4:
            self.slaves[slave] = states_ip_330_zik_krechet(status, 100, slave)


        elif type_sensor == 7:
            self.slaves[slave] = states_mip(status, 100, slave)



        # if status == "N":
        #     self.slaves[slave] = ModbusSlaveContext(hr=ModbusSparseDataBlock(
        #             {0: [4, 4, 1, 1, 3, 3, 2, 5, 2, 100+slave, 0, 3, 0, 0], 50: [0, 13]},
        #             mutable=True))
        # elif status == "F":
        #     self.slaves[slave] = ModbusSlaveContext(
        #         hr=ModbusSparseDataBlock(
        #             {0: [4, 4, 1, 1, 3, 3, 2, 5, 2, 100+slave, 0, 5, 256, 8, 0], 50: [0, 13]},
        #             mutable=True))
        # elif status == "E":
        #     self.slaves[slave] = ModbusSlaveContext(
        #         hr=ModbusSparseDataBlock(
        #             {0: [4, 4, 1, 1, 3, 3, 2, 5, 2, 100+slave, 0, 6, 0, 0], 50: [0, 13]},
        #             mutable=True))


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

    # def _create_slaves_old(self):
    #     slaves = {}
    #     for i in range(1, 33):
    #         store = ModbusSlaveContext(
    #             hr=ModbusSparseDataBlock({0: [4, 4, 1, 1, 3, 3, 2, 5, 0, 100 + i, 0, 3, 0, 0], 50: [0, 13]},
    #                                      mutable=True)
    #         )
    #         slaves[i] = store
    #     return slaves

    def _create_slaves(self):
        slaves = {}
        count_num = 1
        store = None
        for sensor in self.sensors:
            if sensor["type"] == 1:
                store = states_ip_535_07ea_rs(sensor["state"], count_num, sensor["slave"],)
            elif sensor["type"] == 2:
                store = states_ipp_helios(sensor["state"], count_num, sensor["slave"])
            elif sensor["type"] == 3:
                store = states_ip_101(sensor["state"], count_num, sensor["slave"])
            elif sensor["type"] == 4:
                store = states_ip_330_zik_krechet(sensor["state"], count_num, sensor["slave"])
            elif sensor["type"] == 5:
                ...
            elif sensor["type"] == 6:
                ...
            elif sensor["type"] == 7:
                store = states_mip(sensor["state"], count_num, sensor["slave"])
            elif sensor["type"] == 8:
                store = state_ipa(sensor["state"], count_num, sensor["slave"])
            elif sensor["type"] == 9:
                ...
            elif sensor["type"] == 11:
                ...
            elif sensor["type"] == 12:
                ...
            elif sensor["type"] == 13:
                ...

            slaves[sensor["slave"]] = store
            count_num += 1
        return slaves






