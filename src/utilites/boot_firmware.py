import time
from serial import Serial
from loguru import logger

from src.utilites.crc import add_crc, crc_ccitt_16_kermit_b
from src.utilites.ash_util import indicate_send_b6


def get_data_from_file(path):
    with open(path, "br") as f:
        data = f.read()
    return data


def reboot_emulator(conn, sn, cmd):
    msg = bytearray(b"\xB6\x49\x43")
    msg.extend(sn)  # add sn
    if cmd == "A1":
        msg.extend(b"\x01\xA1")
    else:
        msg.extend(b"\x01\xA0")
    msg = add_crc(msg, crc_ccitt_16_kermit_b(msg))
    msg = indicate_send_b6(msg)
    conn.reset_input_buffer()
    conn.write(msg)
    conn.flush()
    conn.read(11)
    conn.reset_input_buffer()
    start = time.time()
    while time.time() - start < 2:
        ...


def get_version(conn, sn):
    """
    прочитать версию, убедиться что в state установлен бит загрузчика;
    :param conn:
    :param sn:
    :return:
    """
    while True:
        msg = bytearray(b"\xB6\x49\x43")
        msg.extend(sn)
        msg.extend(b"\x01\x80")
        msg = add_crc(msg, crc_ccitt_16_kermit_b(msg))
        msg = indicate_send_b6(msg)
        conn.reset_input_buffer()
        conn.write(msg)
        conn.flush()
        ans = response_msg(conn, 24)
        # logger.info(ans.hex(sep=" "))
        if ans:
            return ans

def send_firmware(conn, data, sn):
    """
    <hid (3)> <len (1)> <cmd (1)> <index 24(3)> <count 7 eof 1 (1)> <data (1...128)> <crc>

    -передать командой 0xA2 файл начиная с нулевого смещения;
    -передавать файл далее, начиная со смещения, указанного в ответе на 0xA2;
    -последний блок файла передать с признаком EOF;

    :return:
    """

    index = 0
    len_chunk = 128
    eof = 0
    len_data = len(data)
    while eof == 0:
        if 0 <= index + len_chunk + 1 < len_data:
            chunk = data[index:index + len_chunk]
            count = len_chunk - 1
        else:
            chunk = data[index:]
            eof = 1
            len_chunk = len(chunk)
            count = len_chunk - 1 | 128

        msg = bytearray(b"\xB6\x49\x43")
        msg.extend(sn)              # sn 2
        msg.append(1 + 3 + 1 + len_chunk)    #len (1)
        msg.extend(b"\xA2")         #cmd A2
        msg.extend(index.to_bytes(3, byteorder='little'))  # index
        msg.append(count)  # count_eof
        msg.extend(chunk)
        msg = add_crc(msg, crc_ccitt_16_kermit_b(msg))
        msg = indicate_send_b6(msg)
        conn.reset_input_buffer()
        conn.write(msg)
        conn.flush()
        logger.info(msg.hex(sep=" "))
        ans = response_msg(conn, 15)
        next_index: bytearray = ans[9:12]
        index = int.from_bytes(next_index, byteorder="little")

        if eof != 0:
            if check_state_uploading(ans):
                logger.info("Загрузка закончена успешно")
            else:
                logger.info("Ошибка загрузки")


def response_msg(conn, len_msg):

    while True:
        if conn.read() == b"\xB9" and conn.read() == b"\x46":
            ans = bytearray(b"\xB9\x46")
            for _ in range(len_msg - 2):
                b = conn.read()
                if b == b"\xB9" or b == b"\xB6":
                    conn.read()
                ans.extend(b)
            conn.reset_output_buffer()
            if crc_ccitt_16_kermit_b(ans) == 0:
                return ans
            else:
                return None


def boot_firmware(port, sn, data):
    """    Запрос в эмулятор
        < hid[3] > < len[1] > < cmd[1] > < index[24] > < count[7 // N - 1] > < eof[1] > < data[1 - 128] > < crc >
        Ответ от эмулятора
        < hid[3] > < len[1] > < result[1] > <>
    """
    sn_b = sn.to_bytes((sn.bit_length() + 7) // 8, byteorder='little')

    with Serial(port=port, baudrate=19200, timeout=0.3) as conn:
        reboot_emulator(conn, sn_b, "A1")
        logger.info("reboot end")
        version = get_version(conn, sn_b)
        logger.info("get version end")
        send_firmware(conn, data, sn_b)
        logger.info("send end")
        reboot_emulator(conn, sn_b, "A0")
        logger.info("reboot end")

def check_state_uploading(msg):
    eof = msg[12]
    state = msg[7]
    logger.info(f"eof {eof.to_bytes().hex()} state {state.to_bytes().hex()}")

    return True