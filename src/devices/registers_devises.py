from pymodbus.datastore import ModbusSlaveContext, ModbusSequentialDataBlock, ModbusSparseDataBlock


type_list = {
    1: "ИП-535",             # SKAU03ADDRESSTYPE_MD_EIPR
    2: "ИПП-Гелиос",        # SKAU03ADDRESSTYPE_MD_GELIOS3IK
    3: "ИП-101",            # SKAU03ADDRESSTYPE_MD_EIPT
    4: "ИП-330-Кречет",     # SKAU03ADDRESSTYPE_MD_KRECHET
    5: "ИП-329-Феникс",     # SKAU03ADDRESSTYPE_MD_PHOENIX
    6: "ИПЭС",              # SKAU03ADDRESSTYPE_MD_IPESIKUF
    7: "МИП",               # SKAU03ADDRESSTYPE_MD_MIP
    8: "ИПА",               # SKAU03ADDRESSTYPE_MD_IPA
    9: "NLS",               # SKAU03ADDRESSTYPE_MD_AI

    51: "А2ДПИ",        # ATTYPE_A2DPI
    52: "АВИ",          # ATTYPE_AVI
    53: "АМК",          # ATTYPE_AMK
    54: "АР-1",         # ATTYPE_AR1
    55: "АР-5",         # ATTYPE_AR5
    56: "АРМини",       # ATTYPE_ARMINI
    57: "АТИ",          # ATTYPE_ATI
    58: "АОПИ",         # ATTYPE_AOPI
    59: "ИРС",          # ATTYPE_IRS
    60: "ИР-П",         # ATTYPE_A2RPI
    61: "ИСМ-5",        # ATTYPE_ISM5
    62: "ИСМ-22-1",     # ATTYPE_ISM22_1
    63: "ИСМ-22-2",     # ATTYPE_ISM22_2
    64: "ИСМ-220",      # ATTYPE_ISM4
    65: "МКЗ",          # ATTYPE_MKZ
    66: "ОСЗ",          # ATTYPE_OSZ
    67: "ОСЗ9",         # ATTYPE_OSZ9
}


def states_ipp_helios(status: str, num: int, slave: int = 1) -> ModbusSlaveContext:
    """Регистры состояний ИПП 07еа-RS "Гелиос " (Эридан)"""
    num_l = num
    num_h = 0
    if status == "N":
        return ModbusSlaveContext(
            hr=ModbusSparseDataBlock(
                {0: [slave, 6, 1, 1, 2, 2, 1, 3, num_l, num_h, 0, 3, 0], 51: [795, 100, 0, 0, 50]},
                mutable=True))
    elif status == "F":
        return ModbusSlaveContext( #12288
            hr=ModbusSparseDataBlock(
                {0: [slave, 6, 1, 1, 2, 2, 1, 3, num_l, num_h, 0, 5, 0], 51: [795, 100, 0, 0, 50]},
                mutable=True))
    elif status == "E":
        return ModbusSlaveContext( #1024
            hr=ModbusSparseDataBlock(
                {0: [slave, 6, 1, 1, 2, 2, 1, 3, num_l, num_h, 0, 6, 1024], 51: [795, 100, 0, 0, 50]},
                mutable=True))


def states_ip_535_07ea_rs(status, num, slave=1):
    "Регистры состояний ИП535-07еа-RS (Эридан)"

    if status == "N":
        return ModbusSlaveContext(
            hr=ModbusSparseDataBlock(
                {0: [slave, 4, 1, 1, 3, 3, 2, 5, 2, num, 0, 3, 0, 0], 36: [27, 215, 0], 50: [0, 13]},
                mutable=True))
    elif status == "F":
        return ModbusSlaveContext(
            hr=ModbusSparseDataBlock(
                {0: [slave, 4, 1, 1, 3, 3, 2, 5, 2, num, 0, 5, 256, 8, 0], 36: [27, 215, 0], 50: [0, 13]},
                mutable=True))
    elif status == "E":
        return ModbusSlaveContext(
            hr=ModbusSparseDataBlock(
                {0: [slave, 4, 1, 1, 3, 3, 2, 5, 2, num, 0, 6, 0, 0], 36: [27, 215, 0], 50: [0, 13]},
                mutable=True))


def states_ip_101(status, num, slave=1):
    "Регистры состояний ИП101-07- тепловой"
    if status == "N":
        return ModbusSlaveContext(
            hr=ModbusSparseDataBlock(
                {0: [slave, 4, 1, 1, 1, 1, 3, 6, 6, num, 0, 3, 0],  51: [1, 1, 70, 90, 22, 217, 0]},
                mutable=True))
    elif status == "F":
        return ModbusSlaveContext(
            hr=ModbusSparseDataBlock(
                {0: [slave, 4, 1, 1, 1, 1, 3, 6, 6, num, 0, 5, 0],  51: [1, 1, 70, 90, 80, 807, 50]},
                mutable=True))
    elif status == "E":
        return ModbusSlaveContext(
            hr=ModbusSparseDataBlock(
                {0: [3, 4, 1, 1, 1, 1, 3, 6, 6, 1896, 0, 6, 0],  51: [1, 1, 70, 90, 22, 217, 0]},
                mutable=True))


def states_mip(status, num, slave=1):
    "Регистры состояний МИП"
    if status == "N":
        return ModbusSlaveContext(
            hr=ModbusSparseDataBlock(
                {0: [num, slave, 4, 3, 3, 3, 3, 3, 65535, 65535, 65535, 1792, 1, 1, 1, 0, 0, 0, 0, 0, 0, 255,
                     100, 100, 100, 255, 0, ]},
                mutable=True))
    elif status == "F":
        return ModbusSlaveContext(
            hr=ModbusSparseDataBlock(
                {0: [num, slave, 4, 5, 5, 5, 3, 3, 100, 200, 300, 1792, 1, 1, 1, 255, 255, 255, 0, 0, 0, 255,
                     100, 100, 100, 255, 0, ]},
                mutable=True))
    elif status == "E":
        return ModbusSlaveContext(
            hr=ModbusSparseDataBlock(
                {0: [num, slave, 4, 1, 2, 1, 6, 6, 65535, 65535, 65535, 1792, 1, 1, 1, 0, 0, 0, 0, 0, 0, 255,
                      100, 100, 100, 255, 0, ]},
                mutable=True))


def states_nls(status, num, slave=1):
    # NLS =================================================================================================================
    # регистры    00h 20h - 00h 3Eh | 00h 00h- 00h 0fh |
    # 02h 00h адрес [адрес]
    # 02h 01h скорость RS485    9600        [06]
    # 02h 0Ah паритет / стоп бит  (нет 1)   [1]
    # 02h 05h протокол                      [0]
    # 02h 09h счетчик                       [10]

    if status == "N":
        return ModbusSlaveContext(
            ir=ModbusSparseDataBlock({0: [16511, 5312]*16,
                                      20: [16511, 5312]*16}),
            hr=ModbusSparseDataBlock(
                {20: [0]*16,
                 200: [], #имя модуля
                 212: [], #версия программы
                 512: [slave, 6],
                 522: [1]
                 },
                mutable=True))
    elif status == "F":
        return ModbusSlaveContext(
            ir=ModbusSparseDataBlock({0: [16767, 20707] * 16,
                                      20: [16767, 20707] * 16}),
            hr=ModbusSparseDataBlock(
                {0: [4]*16,
                 20: [4]*16,
                 200: [], #имя модуля 4 регистра
                 212: [], #версия программы
                 512: [slave, 6],
                 522: [1]
                 },
                mutable=True))
    elif status == "E":
        return ModbusSlaveContext(
            ir=ModbusSparseDataBlock({0: [16252, 54290] * 16,
                                      20: [16252, 54290] * 16}),
            hr=ModbusSparseDataBlock(
                {0: [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
                 20: [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],
                 200: [], #имя модуля
                 212: [], #версия программы
                 512: [slave, 6],
                 522: [1]
                 },
                mutable=True))


def states_ip_330_zik_krechet(status, num, slave=1):
    "Регистры состояний ИП 330-3--2-3ИК (Кречет) спектрприбор"

    if status == "N":
        return ModbusSlaveContext(
            hr=ModbusSparseDataBlock({0: [slave, 63119]}, mutable=True),
            ir=ModbusSparseDataBlock({1: [num, 40, 40, 0, 0], 11: [27], 257: [10]*10})
        )
    elif status == "F":
        return ModbusSlaveContext(
            hr=ModbusSparseDataBlock({0: [slave, 63119]}, mutable=True),
            ir=ModbusSparseDataBlock({1: [num, 200, 200, 0, 0], 11: [27], 257: [10]*10})
        )
    elif status == "E":
        return ModbusSlaveContext(
            hr=ModbusSparseDataBlock({0: [slave, 63119]}, mutable=True),
            ir=ModbusSparseDataBlock({1: [num, 0, 0, 0, 0], 11: [27], 257: [10]*10})
        )


def state_ipes_ik_uf(status, num, slave=1):
    "Регистры состояний ИПЭС-ИК/УФ (электронстандарт прибор)"
    # d2h = 0  #Фиксация
    # d1h = 1
    # d0h = 1
    # d2l = 0
    # d1l = 0   #авария
    # d0l = 0   #пожар
    # functions = ((3 & 0xff) << 8) | (0 & 0xff)

    slave_speed = ((slave & 0xff) << 8) | (8 & 0xff)

    if status == "N":
        return ModbusSlaveContext(
            hr=ModbusSparseDataBlock(
                {1: [slave_speed, 768]},
                mutable=True))
    elif status == "F":
        return ModbusSlaveContext(
            hr=ModbusSparseDataBlock(
                {1: [slave_speed, 769]},
                mutable=True))
    elif status == "E":
        return ModbusSlaveContext(
            hr=ModbusSparseDataBlock(
                {1: [slave_speed, 770]},
                mutable=True))


def state_ip_329_330_phoenix(status, num, slave=1):
    """Регистры состояний Феникс ИК/УФ (ИП 329/330-1-1) (П О Ж Г А З П Р И Б О Р)"""
    if status == "N":
        return ModbusSlaveContext(
            hr=ModbusSparseDataBlock(
                {1: [slave, 2, num, 1, 1, 1, 64512, 2]},
                mutable=True))
    elif status == "F":
        return ModbusSlaveContext(
            hr=ModbusSparseDataBlock(
                {1: [slave, 2, num, 1, 1, 1, 28723, 3]},
                mutable=True))
    elif status == "E":
        return ModbusSlaveContext(
            hr=ModbusSparseDataBlock(
                {1: [slave, 2, num, 1, 1, 1, 28676, 16384]},
                mutable=True))


def state_ipa(status, num, slave=1):
    """Регистры состояний ИПА (аспирационник)"""

    if status == "N":
        return ModbusSlaveContext(
            hr=ModbusSparseDataBlock(
                {0: [0, 401, 2, 1, 0, 15, 23000, 100, 100, 240], 18: [730, 1, 1, 1, 0, 4000], 96: [0]*6},
                mutable=True))
    elif status == "F":
        return ModbusSlaveContext(
            hr=ModbusSparseDataBlock(
                {0: [0, 51201, 4, 100, 9000, 6000, 40000, 100, 100, 240], 18: [730, 1, 1, 1, 0, 4000], 96: [0]*6},
                mutable=True))
    elif status == "E":
        return ModbusSlaveContext(
            hr=ModbusSparseDataBlock(
                {0: [0, 51200, 1, 1, 0, 15, 23000, 100, 100, 240, ], 18: [730, 1, 1, 1, 0, 4000], 96: [0]*6},
                mutable=True))


def a2dpi_sigma(status, num, params, slave=1,):
    """А2ДПИ Сигма"""
    ...


def ir_sigma(status, num, params, slave=1,):
    """ИР Сигма"""
    ...


def mkz_sigma(status, num, params, slave=1):
    """МКЗ Сигма"""
    ...
