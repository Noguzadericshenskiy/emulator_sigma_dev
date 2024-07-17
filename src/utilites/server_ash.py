import time

from serial import Serial
from PySide6.QtCore import Signal, QThread
from loguru import logger

from src.utilites.crc import crc_ccitt_16_kermit_b, add_crc


class ServerAH(QThread):
    """Эмулятор адресных устройств АШ Сигма
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
                {'type': 51, 'state': 'N', 'state_cod': 0, 'slave': 1, 'serialnumber': '10'},
                {...},
            ],
        },
        {...}
    ]
    """

    # sig_1 = Signal(tuple)
    # sig_2 = Signal(tuple)

    def __init__(self, array_controllers, name):
        super().__init__()
        self.name = self.port = name
        self.daemon = True
        self.conn = None
        self.controllers = array_controllers
        self.f_run = True
        self.f_response = False

    def run(self) -> None:
        self.conn = Serial(
            port=self.port,
            baudrate=19200,
            timeout=0.3,
        )
        for controller in self.controllers:
            sn_emul = int(controller["sn_emul"])
            self._delete_config(sn_emul)
            logger.info("end del")
            self._create_sensors(sn_emul, controller["sensors"])
            logger.info("end create")
            # self._set_state(sn_emul) ????
        logger.info("run")
        while self.f_run:
            for controller in self.controllers:
                sn_emul = int(controller["sn_emul"])
                self._set_state(sn_emul, controller["sensors"])

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

    # def _send_msg(self, msg):
    #     self.conn.reset_input_buffer()
    #     self.conn.write(msg)
    #     self.conn.flush()
    #     f_ans = True
    #     while f_ans:
    #         if self.conn.read() == b"\xB9" and self.conn.read() == b"\x46":
    #             b_arr = self.conn.read_all()
    #             if self._clear_response(b_arr):
    #                 f_ans = False
    #                 self.f_response = False
    #             else:
    #                 f_ans = False

    def _send_msg(self, msg, num_ans):
        self.conn.reset_input_buffer()
        self.conn.write(msg)
        self.conn.flush()
        f_ans = True
        while f_ans:
            if self.conn.read() == b"\xB9" and self.conn.read() == b"\x46":
                ans = bytearray(b"\xB9\x46")
                for _ in range(num_ans - 2):
                    b = self.conn.read()
                    if b == b"\xB9" or b == b"\xB6":
                        self.conn.read()
                    ans.extend(b)
                self.conn.reset_output_buffer()
                if crc_ccitt_16_kermit_b(ans) == 0:
                    f_ans = False
                    self.f_response = False

    # def _clear_response(self, b_arr):
    #     # ans = bytearray(b"\xB9\x46")
    #     ld = []
    #     for i in range(len(b_arr)):
    #         p = b_arr[i]
    #         if b_arr[i] == 182 or b_arr[i] == 185:
    #             ld.append(i)
    #     if ld:
    #         for i in ld:
    #             b_arr.pop(i + 1)
    #     return True

    def _create_sensors(self, sn, sensors):
        for sensor in sensors:
            self.f_response = True
            serialnumber = int(sensor["serialnumber"])
            msg = bytearray(b"\xB6\x49\x43")
            msg.extend(sn.to_bytes(2, byteorder='little', signed=True))
            msg.extend(b"\x06\xC3")
            msg.extend(serialnumber.to_bytes(3, byteorder='little'))
            msg.extend(self._compare_type(sensor["type"]))
            msg.append(int(sensor["slave"]))
            msg = add_crc(msg, crc_ccitt_16_kermit_b(msg))
            msg = self._indicate_send_b6(msg)
            logger.info(f"{sensor}")
            while self.f_response:
                self._send_msg(msg, 11)

    # @logger.catch()
    def _set_state(self, sn, sensors):
        for sensor in sensors:
            self.f_response = True
            msg = bytearray(b"\xB6\x49\x43")
            msg.extend(sn.to_bytes(2, byteorder='little', signed=True))
            msg.extend(b"\x0A")
            msg.extend(b"\xC2")
            msg.extend(int(sensor["serialnumber"]).to_bytes(3, byteorder='little', signed=True))
            msg.extend(self._compare_type(sensor["type"]))
            msg.extend(self._compare_state(self._compare_type(sensor["type"]), sensor["state"], sensor["state_cod"]))
            msg.extend(b"\x80")
            msg = add_crc(msg, crc_ccitt_16_kermit_b(msg))
            msg = self._indicate_send_b6(msg)
            while self.f_response:
                self._send_msg(msg, 11)

    def changing_state(self, params):
        for controllers in self.controllers:
            if controllers["sn_emul"] == params["sn_emul"]:
                for sensor in controllers["sensors"]:
                    if sensor["slave"] == params["slave"]:
                        sensor["state"] = params["state"]
                        sensor["state_cod"] = params["state_cod"]
                        break

    def _status_request(self, sn_emul):
        msg = (bytearray(b"\xB6\x49\x43"))
        msg.extend(sn_emul.to_bytes(2, byteorder='little', signed=True))
        msg.extend(b"\x01\xC1")
        msg = add_crc(msg, crc_ccitt_16_kermit_b(msg))
        msg = self._indicate_send_b6(msg)
        logger.info(f"send {msg.hex()}")
        self.conn.write(msg)
        if self.conn.read() == b"\xB9" and self.conn.read() == b"\x46":
            ans = bytearray(b"\xB9\x46")
            type_s = self.conn.read().hex()
            sn_l = self.conn.read().hex()
            sn_h = self.conn.read().hex()
            l = self.conn.read().hex()
            cmd = self.conn.read().hex()
            logger.info(f"read [{ans}] [{type_s} {sn_l} {sn_h}] [{l}] [{cmd}]")
            self.conn.read_all()

    def _indicate_send_b6(self, array_bytes: bytearray):
        new_msg = bytearray(b"\xB6\x49")
        for i_byte in array_bytes[2:]:
            if i_byte == 182:
                new_msg.append(i_byte)
                new_msg.append(0)
            else:
                new_msg.append(i_byte)
        return new_msg

    def _compare_type(self, type_sens: int) -> bytes:
        match type_sens:
            case 51:            # A2DPI
                return b"\x19"
            case 53:            # АМК
                return b"\x0F"
            case 54:            # AR1
                return b"\x0C"
            case 57:            # АТИ
                return b"\x10"
            case 60:            # ИР-П
                return b"\x18"
            case 65:            # МКЗ
                return b"\x01"

            # case 61:            # ИСМ5
            #     return b"\x04"
            # case 64:            # ИСМ220-4
            #     return b"\x0D"

            case _:
                logger.info(f"non type {type_sens}")

    def _compare_state(self, type_sens, state, state_cod=0):
        match type_sens:
            case b'\x19':    #A2ДПИ
                match state:
                    case "N":
                        return b"\x00\x00\x00\x00"
                    case "F":
                        return b"\x00\x00\x00\x80"
                    case "E":
                        match state_cod:
                            case 3:
                                return b"\x08\x00\x00\x00"
                            case 2:
                                return b"\x04\x00\x00\x00"
            case b'\x18':   #ИР
                match state:
                    case "N":
                        return b"\x00\x00\x00\x00"
                    case "F":
                        return b"\x00\x00\x00\x80"
                    case "E":
                        return b"\x00\x00\x00\x40"
            case b'\x0C':   #АР1
                # 13 бит-шум, 14 бит-обрыв, 15 бит кз
                match state:
                    case "N":
                        return b"\x00\x00\x00\x00"
                    case "F":
                        return b"\x00\x00\x00\x80"
                    case "E":
                        match state_cod:
                            case 13:
                                return b"\x00\x20\x00\x40"
                            case 14:
                                return b"\x00\x40\x00\x00"
                            case 15:
                                return b"\x00\x80\x00\x00"
            case b'\x01':   #МКЗ
                match state:
                    case "N":
                        return b"\x00\x00\x00\x00"
                    case "F":
                        return b"\x00\x00\x00\x00"
                    case "E":
                        return b"\x00\x00\x00\x40"
            case b'\x0F':   #АМК
                match state:
                    case "N":
                        return b"\x00\x00\x00\x00"
                    case "F":
                        return b"\x00\x00\x00\x80"
                    # case "E":
                    #     return b"\x00\x00\x00\x40"

            case b'\x10':   #АТИ
                match state:
                    case "N":
                        return b"\x00\x00\x00\x00"
                    case "F":
                        return b"\x00\x00\x00\x80"
                    case "E":
                        return b"\x00\x00\x00\x40"
            case b"\x0D":  # ИСМ220-4
                match state:
                    case "N":
                        return b"\x00\x03\x00\x00"
                    case "F":
                        return b"\x00\x03\x00\x80"
                    case "E":
                        match state_cod:
                            case 5:
                                return b"\x20\x03\x00\x00"
                            case 4:
                                return b"\x10\x03\x00\x00"
                            case 7:
                                return b"\x80\x03\x00\x00"
                            case 6:
                                return b"\x40\x03\x00\x00"
                            case 15:
                                return b"\x00\x83\x00\x00"
                            case 14:
                                return b"\x00\x43\x00\x00"
                            case 29:
                                return b"\x00\x03\x00\x20"
                            case 12:
                                return b"\x00\x13\x00\x00"
                            case 11:
                                return b"\x00\x0b\x00\x00"
                            case 27:
                                return b"\x00\x03\x00\x08"
            # case b"\x04": #ИСМ5
            #     match state:
            #         case "N":
            #             return b"\x00\x03\x00\x00"
            #         case "F":
            #             return b"\x00\x03\x00\x80"
            #         case "E":
            #             match err:
            #                 case 5:
            #                     return b"\x20\x03\x00\x00"
            #                 case 4:
            #                     return b"\x10\x03\x00\x00"
            #                 case 7:
            #                     return b"\x80\x03\x00\x00"
            #                 case 6:
            #                     return b"\x40\x03\x00\x00"
            #                 case 15:
            #                     return b"\x00\x83\x00\x00"
            #                 case 14:
            #                     return b"\x00\x43\x00\x00"
            #                 case 29:
            #                     return b"\x00\x03\x00\x20"
            #                 case 12:
            #                     return b"\x00\x13\x00\x00"
            #                 case 11:
            #                     return b"\x00\x0b\x00\x00"
            #                 case 27:
            #                     return b"\x00\x03\x00\x08"

            case _:
                logger.info(f"non type {type_sens}")
