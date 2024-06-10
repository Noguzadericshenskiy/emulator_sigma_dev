import sqlalchemy
from sqlalchemy import create_engine, select, desc, Integer, Boolean
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase, sessionmaker

from sqlalchemy.dialects.postgresql import BYTEA, BIGINT, VARCHAR
from loguru import logger


class Base(DeclarativeBase):
    pass


class NetDevice(Base):
    """Сетевой контроллер"""
    __tablename__ = "netdevice"

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    type: Mapped[str] = mapped_column(VARCHAR(256))
    sync: Mapped[bool] = mapped_column(Boolean, default=False, nullable=True)
    bcpid: Mapped[int] = mapped_column(BIGINT)
    deleted: Mapped[int] = mapped_column(Integer, default=0)
    attached: Mapped[bool] = mapped_column(Boolean, default=False)

    __table_args__ = {'schema': 'configurator'}


class KAU03DConfig(Base):
    """"Сетевой контроллер КАУ03Д"""
    __tablename__ = "kau03dconfig"

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    bcpid: Mapped[int] = mapped_column(BIGINT)
    deleted: Mapped[int] = mapped_column(Integer, default=0)
    hwserialnumber: Mapped[str] = mapped_column(VARCHAR(256), nullable=True)
    ka2addresstraintable: Mapped[str] = mapped_column(VARCHAR, nullable=True)

    __table_args__ = {'schema': 'configurator'}


class SKAU03Config(Base):
    """Сетевой контроллер СКАУ03Д (ModBus)"""
    __tablename__ = "skau03config"

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    bcpid: Mapped[int] = mapped_column(BIGINT)
    deleted: Mapped[int] = mapped_column(Integer, default=0)
    hwserialnumber: Mapped[str] = mapped_column(VARCHAR(256), nullable=True)
    sensoraddressarray: Mapped[str] = mapped_column(VARCHAR, nullable=True)

    __table_args__ = {'schema': 'configurator'}


class Ka2AddressTraintable(Base):
    __tablename__ = "ka2addresstraintable"

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    address: Mapped[str] = mapped_column(VARCHAR, primary_key=True)
    bcpid: Mapped[int] = mapped_column(BIGINT)
    deleted: Mapped[int] = mapped_column(BIGINT, default=0)
    devicetype: Mapped[str] = mapped_column(VARCHAR, nullable=True)
    serialnumber: Mapped[str] = mapped_column(VARCHAR, nullable=True)

    __table_args__ = {'schema': 'configurator'}


class Ka2AddressTraintableA2DPI(Base):
    __tablename__ = "ka2addresstraintableattype_a2dpi"

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    bcpid: Mapped[int] = mapped_column(BIGINT)
    deleted: Mapped[int] = mapped_column(BIGINT, default=0)
    address: Mapped[str] = mapped_column(VARCHAR, primary_key=True)
    threshold: Mapped[str] = mapped_column(VARCHAR(256), nullable=True)
    fdefault: Mapped[bool] = mapped_column(Boolean, nullable=True)

    __table_args__ = {'schema': 'configurator'}


class Ka2AddressTraintableA2RPI(Base):
    __tablename__ = "ka2addresstraintableattype_a2rpi"

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    deleted: Mapped[int] = mapped_column(Integer, default=0)
    address: Mapped[str] = mapped_column(VARCHAR, primary_key=True)
    isolator: Mapped[str] = mapped_column(VARCHAR(1024), nullable=True)

    __table_args__ = {'schema': 'configurator'}


class Ka2AddressTraintableAR1(Base):
    __tablename__ = "ka2addresstraintableattype_ar1"

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    deleted: Mapped[int] = mapped_column(Integer, default=0)
    address: Mapped[str] = mapped_column(VARCHAR, primary_key=True)
    trainr1: Mapped[str] = mapped_column(VARCHAR(1024), nullable=True)

    __table_args__ = {'schema': 'configurator'}


class Ka2AddressTraintableAOPI(Base):
    __tablename__ = "ka2addresstraintableattype_aopi"

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    bcpid: Mapped[int] = mapped_column(BIGINT)
    deleted: Mapped[int] = mapped_column(BIGINT, default=0)
    address: Mapped[str] = mapped_column(VARCHAR, primary_key=True)
    trainr1: Mapped[str] = mapped_column(VARCHAR(1024))
    trainr2: Mapped[str] = mapped_column(VARCHAR(1024))
    fdefault: Mapped[bool] = mapped_column(Boolean, nullable=True)
    threshold: Mapped[str] = mapped_column(VARCHAR(1024), nullable=True)

    __table_args__ = {'schema': 'configurator'}


class Ka2AddressTraintableMKZ(Base):
    __tablename__ = "ka2addresstraintableattype_mkz"

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    bcpid: Mapped[int] = mapped_column(BIGINT)
    deleted: Mapped[int] = mapped_column(BIGINT, default=0)
    address: Mapped[str] = mapped_column(VARCHAR, primary_key=True)
    isolator: Mapped[str] = mapped_column(VARCHAR(1024), nullable=True)

    __table_args__ = {'schema': 'configurator'}


def url_db(params: dict) -> str:
    """ Получаем url для подключения к БД"""
    user = params["user"]
    password = params["password"]
    host = params["host"]
    port = params["port"]
    name = params["name"]
    return f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{name}"


def engine_db(params_db: dict) -> sqlalchemy.Engine:
    """Создать движок БД"""
    url = url_db(params_db)
    return create_engine(
        url,
        # echo=True
    )


def check_conn(params_conn) -> bool:
    "Проверка подключения к БД"
    try:
        conn = engine_db(params_conn)
        return True
    except Exception:
        return False


def get_connect():
    ...


def get_net_devices_from_db(params_conn: dict):
    """Подучить список сетевых контроллеров из БД
        возвращает tupl вида (id, type, name, hwserialnumber)
        (2, 'KAU03DConfig', 'КАУ03Д->123', '123')
    """
    list_dev = []
    stmt = select(NetDevice).where(
        # NetDevice.sync == True,
        NetDevice.deleted == 0,
        NetDevice.type.in_(["KAU03DConfig", "SKAU03Config"])
    ).order_by(NetDevice.type)
    engine = engine_db(params_conn)

    with engine.connect() as conn:
        devices = conn.execute(stmt)
        for device in devices:
            if device[1] == "KAU03DConfig":
                stmt_num = select(KAU03DConfig.hwserialnumber).where(
                    KAU03DConfig.deleted == 0,
                    KAU03DConfig.id == device[0])
                serial_num = conn.execute(stmt_num).scalar()
                list_dev.append((device[0], device[1],  "КАУ03Д->" + serial_num, serial_num,))
            elif device[1] == "SKAU03Config":
                stmt_num = select(SKAU03Config.hwserialnumber).where(
                    SKAU03Config.deleted == 0,
                    SKAU03Config.id == device[0])
                serial_num = conn.execute(stmt_num).scalar()
                list_dev.append((device[0], device[1], "CКАУ03Д->" + serial_num, serial_num,))
        return list_dev


@logger.catch()
def handler_devices(params_conn: dict, in_list):
    """
    Основной обработчик адресных устройств
    Создает список адресных устройств для таблицы вывода и thread
    :param params_conn : dict
    :param in_list: list
    :return: [['COM13', 'CКАУ03Д->6030', {'type': 1, 'state': 'N', 'slave': 4}, {...},], []]
    """

    out_list = []
    engine = engine_db(params_conn)
    with (engine.connect() as conn):
        for row_i in in_list:
            sensors_row = []
            if "KAU03DConfig" == row_i[2][1]:
                stmt_ad = select(Ka2AddressTraintable,
                                 Ka2AddressTraintableA2DPI,
                                 Ka2AddressTraintableA2RPI,
                                 Ka2AddressTraintableAR1,
                                 Ka2AddressTraintableMKZ,
                                 Ka2AddressTraintableAOPI,
                                 )
                stmt_ad = stmt_ad.where(Ka2AddressTraintable.id == row_i[2][0], Ka2AddressTraintable.deleted == 0)
                stmt_ad = stmt_ad.order_by(Ka2AddressTraintable.address)
                stmt_ad = stmt_ad.outerjoin(Ka2AddressTraintableA2DPI,
                                            (Ka2AddressTraintable.address == Ka2AddressTraintableA2DPI.address and
                                             Ka2AddressTraintable.id == Ka2AddressTraintableA2DPI.id))
                stmt_ad = stmt_ad.outerjoin(Ka2AddressTraintableA2RPI,
                                            (Ka2AddressTraintable.address == Ka2AddressTraintableA2RPI.address and
                                             Ka2AddressTraintable.id == Ka2AddressTraintableA2RPI.id))
                stmt_ad = stmt_ad.outerjoin(Ka2AddressTraintableAR1,
                                            (Ka2AddressTraintable.address == Ka2AddressTraintableAR1.address and
                                             Ka2AddressTraintable.id == Ka2AddressTraintableAR1.id))
                stmt_ad = stmt_ad.outerjoin(Ka2AddressTraintableMKZ,
                                            (Ka2AddressTraintable.address == Ka2AddressTraintableMKZ.address and
                                             Ka2AddressTraintable.id == Ka2AddressTraintableMKZ.id))
                stmt_ad = stmt_ad.outerjoin(Ka2AddressTraintableAOPI,
                                            (Ka2AddressTraintable.address == Ka2AddressTraintableAOPI.address and
                                             Ka2AddressTraintable.id == Ka2AddressTraintableAOPI.id))
                stmt_ad = stmt_ad.distinct(Ka2AddressTraintable.address)

                devs = conn.execute(stmt_ad).all()
                for dev_i in devs:
                    # logger.info(f"dev  {dev_i.devicetype} {dev_i.address} {dev_i.serialnumber}")
                    if dev_i[4] == "ATTYPE_A2DPI":
                        sensors_row.append({
                            "type": 51,
                            "state": "N",
                            "slave": int(dev_i[1]),
                            "threshold": dev_i.threshold,
                            "serialnumber": dev_i.serialnumber,
                        })
                    elif dev_i[4] == "ATTYPE_A2RPI":
                        sensors_row.append({
                            "type": 60,
                            "state": "N",
                            "slave": int(dev_i[1]),
                            "serialnumber": dev_i.serialnumber,
                        })
                    elif dev_i[4] == "ATTYPE_AR1":
                        sensors_row.append({
                            "type": 54,
                            "state": "N",
                            "slave": int(dev_i[1]),
                            "serialnumber": dev_i.serialnumber,
                            "trainr1": dev_i.trainr1,
                        })
                    elif dev_i[4] == "ATTYPE_AVI":
                        sensors_row.append({"type": 52, "state": "N", "slave": int(dev_i[1])})
                    elif dev_i[4] == "ATTYPE_AMK":
                        sensors_row.append({"type": 53, "state": "N", "slave": int(dev_i[1])})
                    elif dev_i[4] == "ATTYPE_AR5":
                        sensors_row.append({"type": 55, "state": "N", "slave": int(dev_i[1])})
                    elif dev_i[4] == "ATTYPE_ARMINI":
                        sensors_row.append({"type": 56, "state": "N", "slave": int(dev_i[1])})
                    elif dev_i[4] == "ATTYPE_ATI":
                        sensors_row.append({"type": 57, "state": "N", "slave": int(dev_i[1])})
                    elif dev_i[4] == "ATTYPE_AOPI":
                        sensors_row.append({
                            "type": 58,
                            "state": "N",
                            "slave": int(dev_i[1]),
                            "serialnumber": dev_i.serialnumber,
                            "trainr1": dev_i.trainr1,
                            "trainr2": dev_i.trainr2,
                            "fdefault": dev_i.fdefault,
                            "threshold": dev_i.threshold,
                        })
                    elif dev_i[4] == "ATTYPE_IRS":
                        sensors_row.append({"type": 59, "state": "N", "slave": int(dev_i[1])})
                    elif dev_i[4] == "ATTYPE_ISM5":
                        sensors_row.append({"type": 61, "state": "N", "slave": int(dev_i[1])})
                    elif dev_i[4] == "ATTYPE_ISM22_1":
                        sensors_row.append({"type": 62, "state": "N", "slave": int(dev_i[1])})
                    elif dev_i[4] == "ATTYPE_ISM22_2":
                        sensors_row.append({"type": 63, "state": "N", "slave": int(dev_i[1])})
                    elif dev_i[4] == "ATTYPE_ISM4":
                        sensors_row.append({"type": 64, "state": "N", "slave": int(dev_i[1])})
                    elif dev_i[4] == "ATTYPE_MKZ":
                        sensors_row.append({
                            "type": 65,
                            "state": "N",
                            "slave": int(dev_i[1]),
                            "isolator": dev_i.isolator,
                            "serialnumber": dev_i.serialnumber,
                        })
                    elif dev_i[4] == "ATTYPE_OSZ":
                        sensors_row.append({"type": 66, "state": "N", "slave": int(dev_i[1])})
                    elif dev_i[4] == "ATTYPE_OSZ9":
                        sensors_row.append({"type": 67, "state": "N", "slave": int(dev_i[1])})
                # logger.info(li)
                out_list.append({"port": row_i[0], "net_device": row_i[1],
                                 "net_dev": "KAU03DConfig", "sensors": sensors_row})

            elif "SKAU03Config" == row_i[2][1]:
                stmt_ad = select(SKAU03Config).where(
                    SKAU03Config.id == row_i[2][0],
                    SKAU03Config.deleted == 0)
                ans = conn.execute(stmt_ad).one()
                devs = ans.sensoraddressarray.split("=")
                # sensors_row.append(row_i[0])
                # sensors_row.append(row_i[1])
                for dev_i in devs:
                    description_dev = dev_i.split("|")
                    if description_dev[0] == "SKAU03ADDRESSTYPE_MD_EIPR":
                        sensors_row.append({"type": 1, "state": "N", "slave": int(description_dev[1])})
                    elif description_dev[0] == "SKAU03ADDRESSTYPE_MD_GELIOS3IK":
                        sensors_row.append({"type": 2, "state": "N", "slave": int(description_dev[1])})
                    elif description_dev[0] == "SKAU03ADDRESSTYPE_MD_EIPT":
                        sensors_row.append({"type": 3, "state": "N", "slave": int(description_dev[1])})
                    elif description_dev[0] == "SKAU03ADDRESSTYPE_MD_KRECHET":
                        sensors_row.append({"type": 4, "state": "N", "slave": int(description_dev[1])})
                    elif description_dev[0] == "SKAU03ADDRESSTYPE_MD_PHOENIX":
                        sensors_row.append({"type": 5, "state": "N", "slave": int(description_dev[1])})
                    elif description_dev[0] == "SKAU03ADDRESSTYPE_MD_IPESIKUF":
                        sensors_row.append({"type": 6, "state": "N", "slave": int(description_dev[1])})
                    elif description_dev[0] == "SKAU03ADDRESSTYPE_MD_MIP":
                        sensors_row.append({"type": 7, "state": "N", "slave": int(description_dev[1])})
                    elif description_dev[0] == "SKAU03ADDRESSTYPE_MD_IPA":
                        sensors_row.append({"type": 8, "state": "N", "slave": int(description_dev[1])})
                    elif description_dev[0] == "SKAU03ADDRESSTYPE_MD_AI":
                        sensors_row.append({"type": 9, "state": "N", "slave": int(description_dev[1])})
                    elif description_dev[0] == "SKAU03ADDRESSTYPE_MD_EXIP535":
                        # sensors_row.append({"type": 10, "state": "N", "slave": int(description_dev[1])})
                        ...
                    elif description_dev[0] == "SKAU03ADDRESSTYPE_MD_VEGA":
                        # sensors_row.append({"type": 11, "state": "N", "slave": int(description_dev[1])})
                        ...
                    elif description_dev[0] == "SKAU03ADDRESSTYPE_NO":
                        ...
                    else:
                        print(description_dev[0])
                # out_list.append(sensors_row)
                out_list.append({"port": row_i[0], "net_device": row_i[1],
                                 "net_dev": "SKAU03Config", "sensors": sensors_row})
                logger.info(out_list)
    return out_list


def list_dev_from_str(str_dev) -> list:
    ans = []
    devs = str_dev.split("=")
    for i in range(1, len(devs)):
        a = devs[i].split("|")
        ans.append(a)
    return []


def get_device_mb(device, params_conn):
    """Получить извещатели ModBus"""
    stmt = select(KAU03DConfig).where(KAU03DConfig.id == device.id)
    engine = engine_db(params_conn)

    with engine.connect() as conn:
        return conn.execute(stmt)


def get_device_al(device):
    """Получить извещатели АШ"""
    ...


