import time

from serial import Serial, rs485
from PySide6.QtCore import Signal, QThread
from loguru import logger

from src.utilites.crc import crc_ccitt_16_kermit_b, add_crc


state_trainr_aopi = ["TRAIN1Type_NZwithoutControl", "TRAIN1Type_NRwithoutControl",
                     "TRAIN1Type_1izvNRwithControl", "TRAIN1Type_1izvNZwithControl"]


class ServerAH(QThread):
    """Эмулятор адресных устройств АШ Сигма
        передается конфигурация 1 ряда согласно порта из списка.
        Эмулятор: код устройство 67 серийник 641
    :param port: название сетевого контроллера
    :param sensors: адресные устройства
    """

    sig_1 = Signal(tuple)
    sig_2 = Signal(tuple)

    def __init__(self, sensors, name,):
        super().__init__()
        self.name = name
        self.port = name
        self.daemon = True
        # self.conn = None
        self.sensors = sensors
        self.f_run = True
        self.f_change_state = False
        self.sn_emul = 641


    def run(self) -> None:
        self.conn = Serial(
            port=self.port,
            baudrate=19200,
            # timeout=2,
            # rs485_mode=rs485.RS485Settings()
        )

        self._delete_config(self.sn_emul)
        time.sleep(1)
        self.conn.read_all()
        self._create_sensors(self.sn_emul)
        self._set_state(self.sn_emul)

    # rts_level_for_tx=True, rts_level_for_rx=False
    # self.conn.setRTS(True)
    # self.conn.rs485_mode
    # self.conn.set_buffer_size(1, 1)
    # logger.info(self.sensors)
    # self.init_sensors()
    # self.handler_init_response()
    # msg_create_dev = bytearray(b"\xB6\x49\x43\x81\x02\x06\xC3\x01\x00\x00\x19\x01")
    # msg_create_dev = add_crc(msg_create_dev, crc_ccitt_16_kermit_b(msg_create_dev))
    # msg_set_status = bytearray(b"\xB6\x49\x43\x81\x02\x0A\xC2\x01\x00\x00\x19\x00\x00\x00\x00\x00")
    # msg_set_status = add_crc(msg_set_status, crc_ccitt_16_kermit_b(msg_set_status))
    # msg_get_status = bytearray(b"\xB6\x49\x43\x81\x02\x01\xC1")
    # msg_get_status = add_crc(msg_get_status, crc_ccitt_16_kermit_b(msg_get_status))

        logger.info("run ")
        while self.f_run:
            time.sleep(0.1)
            if self.f_change_state:
                logger.info("Изменить состояние")
            else:
                self._status_request(self.sn_emul)



    def _delete_config(self, sn):
        msg = bytearray(b"\xB6\x49\x43")
        msg.extend(sn.to_bytes((sn.bit_length() + 7) // 8, byteorder='little')) #add sn
        msg.extend(b"\x01\xA0")
        msg = add_crc(msg, crc_ccitt_16_kermit_b(msg))
        self.conn.write(msg)

    def _create_sensors(self, sn):
        for sensor in self.sensors:
            time.sleep(0.1)
            serialnumber = int(sensor["serialnumber"])
            msg = bytearray(b"\xB6\x49\x43")
            msg.extend(sn.to_bytes(2, byteorder='little', signed=True))
            msg.extend(b"\x06\xC3")
            msg.extend(serialnumber.to_bytes(3, byteorder='little', signed=True))
            msg.extend(self._compare_type(sensor["type"]))
            msg.append(int(sensor["slave"]))
            msg = add_crc(msg, crc_ccitt_16_kermit_b(msg))
            msg = self._indicate_send_b6_b9(msg)
            logger.info(f"{sensor}")
            self._send_msg(msg, 7)

    def _send_msg(self, msg, len_ans):
        f_send = True
        count = 0
        while f_send:
            count += 1
            logger.info(f"send {msg.hex()} {count} in-{self.conn.in_waiting} out-{self.conn.out_waiting}")
            self.conn.write(msg)
            if self.conn.read() == b"\xB9" and self.conn.read() == b"\x46":
                ans = bytearray(b"\xB9\x46")
                for index in range(len_ans):
                    b = self.conn.read()
                    if b == b"\xB9" and b == b"\xB6":
                        self.conn.read()
                    ans.append(int.from_bytes(b, "little"))
                crc_ans = self.conn.read(2)
                crc = crc_ccitt_16_kermit_b(ans)
                if int.from_bytes(crc_ans, 'little') == crc:
                    logger.info(f"crc ok")
                    if ans[7:8] == b'\x00' and ans[8:9] == b'\x00':
                        logger.info(f"ans-ok={ans.hex()} state-{ans[7:9].hex()}")
                        f_send = False
                        self.conn.flush()
                    elif ans[7:8] == b'\x00' and ans[8:9] == b'\x81':
                        logger.info(f"ans-bad={ans.hex()} state-{ans[7:9].hex()}")
            logger.info(f"end count-{count} {self.conn.in_waiting} {self.conn.out_waiting}")

    def _set_state(self, sn_emul):
        for sensor in self.sensors:
            time.sleep(0.1)
            logger.info(sensor)
            msg = bytearray(b"\xB6\x49\x43")
            msg.extend(sn_emul.to_bytes(2, byteorder='little', signed=True))
            msg.extend(b"\x0A")
            msg.extend(b"\xC2")
            msg.extend(int(sensor["serialnumber"]).to_bytes(3, byteorder='little', signed=True))
            msg.extend(self._compare_type(sensor["type"]))
            msg.extend(b"\x00\x00\x00\x00")
            msg.extend(b"\x80")
            msg = add_crc(msg, crc_ccitt_16_kermit_b(msg))
            msg = self._indicate_send_b6_b9(msg)
            logger.info(msg.hex())
            self._send_msg(msg, 7)

    def changing_state(self, params):
        self.f_change_state = True
        logger.info(params)

        for sensor in self.sensors:
            if sensor["slave"] == params["slave"]:
                state = self._compare_state(self._compare_type(params["type"]), params["state"])
                logger.info(sensor)
                logger.info(state)
                msg = bytearray(b"\xB6\x49\x43")
                msg.extend(self.sn_emul.to_bytes(2, byteorder='little', signed=True))
                msg.extend(b"\x0A")
                msg.extend(b"\xC2")
                msg.extend(int(sensor["serialnumber"]).to_bytes(3, byteorder='little', signed=True))
                msg.extend(self._compare_type(sensor["type"]))
                msg.extend(state)
                msg.extend(b"\x80")
                msg = add_crc(msg, crc_ccitt_16_kermit_b(msg))
                msg = self._indicate_send_b6_b9(msg)
                logger.info(msg.hex())
                self._send_msg(msg, 7)
                break

        self.f_change_state = False

    
    def _status_request(self, sn_emul):
        msg = (bytearray(b"\xB6\x49\x43"))
        msg.extend(sn_emul.to_bytes(2, byteorder='little', signed=True))
        msg.extend(b"\x01\xC1")
        msg = add_crc(msg, crc_ccitt_16_kermit_b(msg))
        msg = self._indicate_send_b6_b9(msg)
        logger.info(f"send {msg.hex()}")
        self.conn.write(msg)
        self.conn.flush()
        if self.conn.read() == b"\xB9" and self.conn.read() == b"\x46":
            ans = bytearray(b"\xB9\x46")
            type_s = self.conn.read().hex()
            sn_l = self.conn.read().hex()
            sn_h = self.conn.read().hex()
            l = self.conn.read().hex()
            cmd = self.conn.read().hex()
            logger.info(f"read [{ans}] [{type_s} {sn_l} {sn_h}] [{l}] [{cmd}]")
            self.conn.read_all()
            # self.conn.flush()
            # for index in range(3):
            #     b = self.conn.read()
            #     if b == b"\xB9" and b == b"\xB6":
            #         self.conn.read()
            #     ans.append(int.from_bytes(b, "little"))
            # len_msg = self.conn.read()
            # ans.extend(len_msg)
            # logger.info(ans.hex())
            # logger.info(len_msg)
            # if int(len_msg)


        #     crc_ans = self.conn.read(2)
        #     crc = crc_ccitt_16_kermit_b(ans)
        #     if int.from_bytes(crc_ans, 'little') == crc:
        #         logger.info(f"crc ok")
        #         if ans[7:8] == b'\x00' and ans[8:9] == b'\x00':
        #             logger.info(f"ans-ok={ans.hex()} state-{ans[7:9].hex()}")
        #             f_send = False
        #         elif ans[7:8] == b'\x00' and ans[8:9] == b'\x81':
        #             logger.info(f"ans-bad={ans.hex()} state-{ans[7:9].hex()}")
        # logger.info(f"end count-{count}")

    def _compare_type(self, type_sens):
        match type_sens:
            case 51:            # A2DPI
                return b"\x19"
            case 53:            # АМК
                return b"\x0F"
            case 54:            # AR1
                return b"\x0C"
            case 55:            # АР5
                return b"\x20"
            case 56:            # АРМИНИ
                return b"\x1A"
            case 57:            # АТИ
                return b"\x10"
            case 60:            # ИР-П
                return b"\x18"
            case 61:            # ИСМ-5
                return b"\x04"
            case 65:            # МКЗ
                return b"\x01"
            case 66:            # ОСЗ
                return b"\x16"
            case 67:            # ОСЗ9
                return b"\x09"
            case _:
                return b"\x19"

    def _indicate_send_b6_b9(self, array_bytes: bytearray):
        new_msg = bytearray(b"\xB6\x49")
        for i_byte in array_bytes[2:]:
            if i_byte == 182 or i_byte == 185:
                new_msg.append(i_byte)
                new_msg.append(0)
            else:
                new_msg.append(i_byte)
        return new_msg

    def _compare_state(self, type_sens, state):
        match type_sens:
            case b'\x19':    #A2ДПИ
                match state:
                    case "N":
                        return b"\x00\x00\x00\x00"
                    case "F":
                        return b"\x00\x00\x00\x80"
                    case "E":
                        ...
            case b'\x18':   #ИР
                match state:
                    case "N":
                        return b"\x00\x00\x00\x00"
                    case "F":
                        return b"\x00\x00\x00\x80"
                    case "E":
                        return b"\x00\x00\x00\x40"
            case b'\x0C':   #АР1
                match state:
                    case "N":
                        return b"\x00\x00\x00\x00"
                    case "F":
                        return b"\x00\x00\x00\x80"
                    case "E":
                        ...
