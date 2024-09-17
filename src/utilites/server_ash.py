import time

from serial import Serial
from PySide6.QtCore import Signal, QThread
from loguru import logger

from utilites.crc import crc_ccitt_16_kermit_b, add_crc


class ServerAH(QThread):
    """Эмулятор адресных устройств АШ
        передается конфигурация 1 ряда согласно порта из списка.
        Эмулятор: код устройство 67 серийник 641
    :param port: название потока и порта
    :param array_controllers: информация о параметрах сетевых устройств с извещателями

    array_controllers= [
        {
            'net_device': 'КАУ03Д->5843',
            'net_dev': 'KAU03DConfig',
            'sn_net_dev': "5843",
            'sn_emul': "641",
            'sensors': [
                {'type': b"\x04",
                'state': 'N',
                'state_cod': 0,
                'slave': 1,
                'serialnumber': '10',
                'state_in': 00 00 00 00},
                {...},
            ],
        },
        {...}
    ]
    """

    sig_state_in = Signal(tuple)

    def __init__(self, array_controllers, name):
        super().__init__()
        self.name = self.port = name
        self.daemon = True
        self.conn = None
        self.controllers = array_controllers
        self.f_run = True
        self.f_response = False

    @logger.catch()
    def run(self) -> None:
        self.conn = Serial(
            port=self.port,
            baudrate=115200,
            timeout=0.3,
        )
        for controller in self.controllers:
            sn_emul = controller["sn_emul"]
            self._delete_config(sn_emul)
            logger.info("end del")
            self._create_sensors(sn_emul, controller["sensors"])
            logger.info("end create")
        logger.info("run")
        while self.f_run:
            for controller in self.controllers:
                sn_emul = controller["sn_emul"]
                self._set_state(sn_emul, controller["sensors"])
                self._get_state_dev(sn_emul, controller["sensors"], controller["net_device"])

    def _delete_config(self, sn):
        msg = bytearray(b"\xB6\x49\x43")
        msg.extend(sn.to_bytes((sn.bit_length() + 7) // 8, byteorder='little')) #add sn
        msg.extend(b"\x01\xA0")
        msg = add_crc(msg, crc_ccitt_16_kermit_b(msg))
        msg = self._indicate_send_b6(msg)
        self.conn.reset_input_buffer()
        self.conn.write(msg)
        self.conn.flush()
        self.conn.read(11)
        self.conn.reset_input_buffer()
        start = time.time()
        while time.time() - start < 2:
            ...

    def _send_msg(self, msg, len_ans):
        self.conn.reset_input_buffer()
        self.conn.write(msg)
        self.conn.flush()
        f_ans = True
        while f_ans:
            if self.conn.read() == b"\xB9" and self.conn.read() == b"\x46":
                ans = bytearray(b"\xB9\x46")
                for _ in range(len_ans - 2):
                    b = self.conn.read()
                    if b == b"\xB9" or b == b"\xB6":
                        self.conn.read()
                    ans.extend(b)
                self.conn.reset_output_buffer()
                if crc_ccitt_16_kermit_b(ans) == 0:
                    f_ans = False
                    self.f_response = False

    def _create_sensors(self, sn, sensors):
        for sensor in sensors:
            self.f_response = True
            serialnumber = sensor["serialnumber"]
            msg = bytearray(b"\xB6\x49\x43")
            msg.extend(sn.to_bytes(2, byteorder='little', signed=True))
            msg.extend(b"\x06\xC3")
            msg.extend(serialnumber.to_bytes(3, byteorder='little'))
            msg.extend(self._compare_type(sensor["type"]))
            msg.append(sensor["slave"])
            msg = add_crc(msg, crc_ccitt_16_kermit_b(msg))
            msg = self._indicate_send_b6(msg)
            while self.f_response:
                self._send_msg(msg, 11)

    def _set_state(self, sn, sensors):
        for sensor in sensors:
            self.f_response = True
            type_sens = self._compare_type(sensor["type"])
            state = self._compare_state(type_sens, sensor["state_cod"])
            msg = bytearray(b"\xB6\x49\x43")
            msg.extend(sn.to_bytes(2, byteorder='little', signed=True))
            msg.extend(b"\x0A")
            msg.extend(b"\xC2")
            msg.extend(sensor["serialnumber"].to_bytes(3, byteorder='little', signed=True))
            msg.extend(type_sens)
            msg.extend(state)
            msg.extend(b"\x80")
            msg = add_crc(msg, crc_ccitt_16_kermit_b(msg))
            msg = self._indicate_send_b6(msg)
            while self.f_response:
                self._send_msg(msg, 11)

    def _get_state_dev(self, sn_emul, sensors, net_device):
        for sensor in sensors:
            f_ans = True
            msg = (bytearray(b"\xB6\x49\x43"))  # Начало пакета, тип устройства
            msg.extend(sn_emul.to_bytes(2, byteorder='little', signed=True))  # serilnumber
            msg.extend(b"\x01")    # length
            msg.extend(b"\xC1")       # command
            msg = add_crc(msg, crc_ccitt_16_kermit_b(msg))
            msg = self._indicate_send_b6(msg)

            self.conn.reset_input_buffer()
            self.conn.write(msg)
            self.conn.flush()

            while f_ans:
                if self.conn.read() == b"\xB9" and self.conn.read() == b"\x46":
                    ans = bytearray(b"\xB9\x46")
                    for _ in range(20 - 2):
                    # for _ in range(23 - 2): # + 1 c
                        b = self.conn.read()
                        if b == b"\xB9" or b == b"\xB6":
                            self.conn.read()
                        ans.extend(b)
                    self.conn.reset_output_buffer()
                    if crc_ccitt_16_kermit_b(ans) == 0:
                        f_ans = False
                        self.f_response = False
                        if sensor["type"] == "ИСМ-5":
                            state_in = revers_bits_8_9(int(ans[13:17][::-1].hex(), 16))
                        else:
                            state_in = ans[13:17][::-1].hex()

                        if sensor["state_in"] != state_in:
                            sensor["state_in"] = state_in
                            self.sig_state_in.emit((self.name, sn_emul, sensor, net_device))

    def _indicate_send_b6(self, array_bytes: bytearray):
        new_msg = bytearray(b"\xB6\x49")
        for i_byte in array_bytes[2:]:
            if i_byte == 182:
                new_msg.append(i_byte)
                new_msg.append(0)
            else:
                new_msg.append(i_byte)
        return new_msg

    def _compare_type(self, type_sens: str) -> bytes:
        match type_sens:
            case "А2ДПИ":
                return b"\x19"
            case "АМК":
                return b"\x0F"
            case "АР1":
                return b"\x0C"
            case "АТИ":
                return b"\x10"
            case "ИР-П":
                return b"\x18"
            case "МКЗ":
                return b"\x01"
            case "ИСМ-5":
                return b"\x04"
            case "ИСМ-220.4":
                return b"\x0D"

            case _:
                logger.info(f"non type {type_sens}")

    def _compare_state(self, type_sens, state_cod="N"):
        "Байты отдаем младшим вперед!"
        match type_sens:
            case b'\x19':    #A2ДПИ
                match state_cod:
                    case "N":
                        return b"\x00\x00\x00\x00"
                    case 31:
                        return b"\x00\x00\x00\x80"
                    case 3:
                        return b"\x08\x00\x00\x00"
                    case 2:
                        return b"\x04\x00\x00\x00"
            case b'\x18':   #ИР
                match state_cod:
                    case "N":
                        return b"\x00\x00\x00\x00"
                    case 31:
                        return b"\x00\x00\x00\x80"
                    case 30:
                        return b"\x00\x00\x00\x40"
            case b'\x0C':   #АР1
                # 13 бит-шум, 14 бит-обрыв, 15 бит кз
                match state_cod:
                    case "N":
                        return b"\x00\x00\x00\x00"
                    case 31:
                        return b"\x00\x00\x00\x80"
                    case 13:
                        return b"\x00\x20\x00\x40"
                    case 14:
                        return b"\x00\x40\x00\x00"
                    case 15:
                        return b"\x00\x80\x00\x00"
            case b'\x01':   #МКЗ
                match state_cod:
                    case "N":
                        return b"\x00\x00\x00\x00"
                    case 31:
                        return b"\x00\x00\x00\x80"
                    case 30:
                        return b"\x00\x00\x00\x40"
            case b'\x0F':   #АМК
                match state_cod:
                    case "N":
                        return b"\x00\x00\x00\x00"
                    case 31:
                        return b"\x00\x00\x00\x80"
            case b'\x10':   #АТИ
                match state_cod:
                    case "N":
                        return b"\x00\x00\x00\x00"
                    case 31:
                        return b"\x00\x00\x00\x80"
                    case 30:
                        return b"\x00\x00\x00\x40"
            case b"\x0D":  # ИСМ220-4
                match state_cod:
                    case "N":
                        return b"\x00\x00\x00\x00"
                    case 31:
                        return b"\x00\x00\x00\x80"
                    case 5:
                        return b"\x20\x00\x00\x00"
                    case 4:
                        return b"\x10\x00\x00\x00"
                    case 7:
                        return b"\x80\x00\x00\x00"
                    case 6:
                        return b"\x40\x00\x00\x00"
                    case 15:
                        return b"\x00\x80\x00\x00"
                    case 14:
                        return b"\x00\x40\x00\x00"
                    case 29:
                        return b"\x00\x00\x00\x20"
                    case 12:
                        return b"\x00\x10\x00\x00"
                    case 11:
                        return b"\x00\x08\x00\x00"
                    case 27:
                        return b"\x00\x00\x00\x08"
            case b"\x04": #ИСМ5
                match state_cod:
                    case "N":
                        return b"\x00\x00\x00\x00"
                    case 31:
                        return b"\x00\x00\x00\x80"
                    case 5:
                        return b"\x20\x00\x00\x00"
                    case 4:
                        return b"\x10\x00\x00\x00"
                    case 7:
                        return b"\x80\x00\x00\x00"
                    case 6:
                        return b"\x40\x00\x00\x00"
                    case 15:
                        return b"\x00\x80\x00\x00"
                    case 14:
                        return b"\x00\x40\x00\x00"
                    case 29:
                        return b"\x00\x00\x00\x20"
                    case 12:
                        return b"\x00\x10\x00\x00"
                    case 11:
                        return b"\x00\x08\x00\x00"
                    case 27:
                        return b"\x00\x00\x00\x08"

            case _:
                logger.error(f"non type {type_sens}")


def revers_bits_8_9(state: int) -> hex:

    if state >> 8 & 1 != 0:
        sensor_state: int = state & ~ (1 << 8)
    else:
        sensor_state: int = state | (1 << 8)
    if state >> 9 & 1 != 0:
        sensor_state: int = sensor_state & ~ (1 << 9)
    else:
        sensor_state: int = sensor_state | (1 << 9)

    return sensor_state.to_bytes(4, "big").hex()
