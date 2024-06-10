from serial import Serial
from PySide6.QtCore import Signal, QThread
from loguru import logger


state_trainr_aopi = ["TRAIN1Type_NZwithoutControl", "TRAIN1Type_NRwithoutControl",
             "TRAIN1Type_1izvNRwithControl", "TRAIN1Type_1izvNZwithControl"]

# Эмулятор код устройство 67 серийник 641

class ServerAH(QThread):
    """Эмулятор адресных устройств АШ Сигма
        передается конфигурация 1 ряда согласно порта из списка.
    :param name: название сетевого контроллера
    :param devices: адресные устройства
    """
    sig_1 = Signal(tuple)
    sig_2 = Signal(tuple)

    def __init__(self, sensors, port):
        super().__init__()
        self.port = port
        self.daemon = True
        self.conn = None
        self.sensors = sensors

    def run(self) -> None:
        self.conn = Serial(port=self.port, baudrate=19200)
        logger.info(self.sensors)
        self.init_sensors()
        #
        # self.handler_init_response()

    def init_sensors(self):
        for sensor in self.sensors:
            # print(sensor)
            ...

    def handler_response(self):
        while True:
            if self.conn.read() == "" and self.conn.read() == "":
                type_sensor = self.conn.read()
                sn_lo = self.conn.read()
                sn_hi = self.conn.read()
                cmd = self.conn.read()
                lenght = self.conn.read()
                data = self.conn.read()

                print("Начало пакета")

    def handler_init_response(self):
        while True:
            if self.conn.read() == "" and self.conn.read() == "":
                type_sensor = self.conn.read()
                if type_sensor.hex() == "B9":
                    self.conn.read()
                sn_lo = self.conn.read()
                if sn_lo.hex() == "B9":
                    self.conn.read()
                sn_hi = self.conn.read()
                if sn_hi.hex() == "B9":
                    self.conn.read()
                cmd = self.conn.read()
                if cmd.hex() == "B9":
                    self.conn.read()
                state = self.conn.read()
                if state.hex() == "B9":
                    self.conn.read()
                crc = self.conn.read(2)

                print("Начало инит пакета", )
