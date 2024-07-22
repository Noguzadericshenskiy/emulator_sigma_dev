import sqlalchemy
import psycopg2
import operator

from psycopg2 import OperationalError
from sqlalchemy import create_engine, select, Integer, Boolean
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase

from sqlalchemy.dialects.postgresql import BIGINT, VARCHAR
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


class Ka2AddressTraintableMKZ(Base):
    __tablename__ = "ka2addresstraintableattype_mkz"

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    bcpid: Mapped[int] = mapped_column(BIGINT)
    deleted: Mapped[int] = mapped_column(BIGINT, default=0)
    address: Mapped[str] = mapped_column(VARCHAR, primary_key=True)
    isolator: Mapped[str] = mapped_column(VARCHAR(1024), nullable=True)

    __table_args__ = {'schema': 'configurator'}


class Ka2AddressTraintableAMK(Base):
    __tablename__ = "ka2addresstraintableattype_amk"

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    bcpid: Mapped[int] = mapped_column(BIGINT)
    deleted: Mapped[int] = mapped_column(BIGINT, default=0)
    address: Mapped[str] = mapped_column(VARCHAR, primary_key=True)

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


class Ka2AddressTraintableATI(Base):
    __tablename__ = "ka2addresstraintableattype_ati"

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    bcpid: Mapped[int] = mapped_column(BIGINT)
    deleted: Mapped[int] = mapped_column(BIGINT, default=0)
    address: Mapped[str] = mapped_column(VARCHAR, primary_key=True)
    firedetectmode: Mapped[str] = mapped_column(VARCHAR(1024), nullable=True)
    difffiredetectmodeon: Mapped[bool] = mapped_column(Boolean, nullable=True)

    __table_args__ = {'schema': 'configurator'}

class Ka2AddressTraintable_ISM4(Base):
    __tablename__ = "ka2addresstraintableattype_ism4"

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    bcpid: Mapped[int] = mapped_column(BIGINT)
    deleted: Mapped[int] = mapped_column(BIGINT, default=0)
    address: Mapped[str] = mapped_column(VARCHAR, primary_key=True)
    trainr1: Mapped[str] = mapped_column(VARCHAR(1024), nullable=True)
    trainr2: Mapped[str] = mapped_column(VARCHAR(1024), nullable=True)

    __table_args__ = {'schema': 'configurator'}

class Ka2AddressTraintable_ISM5(Base):
    __tablename__ = "ka2addresstraintableattype_ism5"

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    bcpid: Mapped[int] = mapped_column(BIGINT)
    deleted: Mapped[int] = mapped_column(BIGINT, default=0)
    address: Mapped[str] = mapped_column(VARCHAR, primary_key=True)
    trainr1: Mapped[str] = mapped_column(VARCHAR(1024), nullable=True)
    trainr2: Mapped[str] = mapped_column(VARCHAR(1024), nullable=True)

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
        conn = psycopg2.connect(
            dbname=params_conn["name"],
            user=params_conn["user"],
            password=params_conn["password"],
            host=params_conn["host"],
            port=params_conn["port"],
            connect_timeout=2,
        )
        conn.close()
        return True
    except OperationalError:
        return False


def get_net_devices_from_db(params_conn: dict):
    """Подучить список сетевых контроллеров из БД
        возвращает tupl вида (id, type, name, hwserialnumber)
        (2, 'KAU03DConfig', 'КАУ03Д->123', 123)
    """
    list_dev = []
    stmt = select(NetDevice).where(
        # NetDevice.sync == True,
        NetDevice.deleted == 0,
        NetDevice.type.in_(["KAU03DConfig", "SKAU03Config"])
    ).order_by(NetDevice.type)
    engine = engine_db(params_conn,)

    with engine.connect() as conn:
        devices = conn.execute(stmt)
        for device in devices:
            if device[1] == "KAU03DConfig":
                stmt_num = select(KAU03DConfig.hwserialnumber).where(
                    KAU03DConfig.deleted == 0,
                    KAU03DConfig.id == device[0])
                serial_num = conn.execute(stmt_num).scalar()
                list_dev.append((device[0], device[1],  "КАУ03Д->" + serial_num, int(serial_num),))
            elif device[1] == "SKAU03Config":
                stmt_num = select(SKAU03Config.hwserialnumber).where(
                    SKAU03Config.deleted == 0,
                    SKAU03Config.id == device[0])
                serial_num = conn.execute(stmt_num).scalar()
                list_dev.append((device[0], device[1], "CКАУ03Д->" + serial_num, int(serial_num),))
        return sorted(list_dev, key=operator.itemgetter(1, 3))


# @logger.catch()
def handler_devices(params_conn: dict, in_list):
    """
    Основной обработчик адресных устройств
    Создает список адресных устройств для таблицы вывода и thread
    :param params_conn:
    :param in_list: list [('COM17', (23, 'SKAU03Config', 'CКАУ03Д->6030', 6030), None), (...)]
    :return:
    """

    out_list = []
    engine = engine_db(params_conn)
    with (engine.connect() as conn):
        for row_i in in_list:
            sensors_row = []
            if row_i[1][1] =="KAU03DConfig":
                stmt_ad = select(Ka2AddressTraintable,
                                 Ka2AddressTraintableA2DPI,
                                 Ka2AddressTraintableA2RPI,
                                 Ka2AddressTraintableAR1,
                                 Ka2AddressTraintableMKZ,
                                 Ka2AddressTraintableAMK,
                                 Ka2AddressTraintableATI,
                                 Ka2AddressTraintableAOPI,
                                 # Ka2AddressTraintable_ISM5,
                                 )
                stmt_ad = stmt_ad.where(Ka2AddressTraintable.id == row_i[1][0], Ka2AddressTraintable.deleted == 0)
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
                stmt_ad = stmt_ad.outerjoin(Ka2AddressTraintableAMK,
                                            (Ka2AddressTraintable.address == Ka2AddressTraintableAMK.address and
                                             Ka2AddressTraintable.id == Ka2AddressTraintableAMK.id))
                stmt_ad = stmt_ad.outerjoin(Ka2AddressTraintableATI,
                                            (Ka2AddressTraintable.address == Ka2AddressTraintableATI.address and
                                             Ka2AddressTraintable.id == Ka2AddressTraintableATI.id))
                stmt_ad = stmt_ad.outerjoin(Ka2AddressTraintableAOPI,
                                            (Ka2AddressTraintable.address == Ka2AddressTraintableAOPI.address and
                                             Ka2AddressTraintable.id == Ka2AddressTraintableAOPI.id))
                # stmt_ad = stmt_ad.outerjoin(Ka2AddressTraintable_ISM4,
                #                             (Ka2AddressTraintable.address == Ka2AddressTraintable_ISM4.address and
                #                              Ka2AddressTraintable.id == Ka2AddressTraintable_ISM4.id))
                # stmt_ad = stmt_ad.outerjoin(Ka2AddressTraintable_ISM5,
                #                             (Ka2AddressTraintable.address == Ka2AddressTraintable_ISM5.address and
                #                              Ka2AddressTraintable.id == Ka2AddressTraintable_ISM5.id))

                stmt_ad = stmt_ad.distinct(Ka2AddressTraintable.address)
                # stmt_ad = stmt_ad.order_by(Ka2AddressTraintable.address)
                devs = conn.execute(stmt_ad).all()
                for dev_i in devs:
                    match dev_i[4]:
                        case "ATTYPE_A2DPI":
                            sensors_row.append({
                                "type": "А2ДПИ",
                                "state": "Норма",
                                "slave": int(dev_i[1]),
                                "serialnumber": int(dev_i.serialnumber),
                                "state_cod": "N",
                            })
                        case "ATTYPE_AMK":
                            sensors_row.append({
                                "type": "АМК",
                                "state": "Норма",
                                "slave": int(dev_i[1]),
                                "serialnumber": int(dev_i.serialnumber),
                                "state_cod": "N",
                            })
                        case "ATTYPE_AR1":
                            sensors_row.append({
                                "type": "АР1",
                                "state": "Норма",
                                "slave": int(dev_i[1]),
                                "serialnumber": int(dev_i.serialnumber),
                                "state_cod": "N",
                            })
                        case "ATTYPE_ATI":
                            sensors_row.append({
                                "type": "АТИ",
                                "state": "Норма",
                                "slave": int(dev_i[1]),
                                "serialnumber": int(dev_i.serialnumber),
                                "state_cod": "N",
                            })
                        case "ATTYPE_A2RPI":
                            sensors_row.append({
                                "type": "ИР-П",
                                "state": "Норма",
                                "slave": int(dev_i[1]),
                                "serialnumber": int(dev_i.serialnumber),
                                "state_cod": "N",
                            })
                        case "ATTYPE_MKZ":
                            sensors_row.append({
                                "type": "МКЗ",
                                "state": "Норма",
                                "slave": int(dev_i[1]),
                                "serialnumber": int(dev_i.serialnumber),
                                "state_cod": "N",
                            })
                        case "ATTYPE_AOPI":
                            sensors_row.append({
                                "type": "АОПИ",
                                "state": "Норма",
                                "slave": int(dev_i[1]),
                                "serialnumber": int(dev_i.serialnumber),
                                "state_cod": "N",
                            })

                        case _:
                            ...
                    # row_i = ('COM6', (22, 'KAU03DConfig', 'КАУ03Д->100772', 100772), '641')
                    # devs  =
                sensors_sort = sorted(sensors_row, key=lambda s: s["slave"])
                controller = create_controller(sensors_sort, row_i)
                f_presence = False
                if out_list:
                    for port_params in out_list:
                        if port_params["port"] == row_i[0]:
                            port_params["controllers"].append(controller)
                            f_presence = True
                            break
                    if not f_presence:
                        out_list.append({"port": row_i[0], "controllers": [controller]})
                else:
                    out_list.append({"port": row_i[0], "controllers": [controller]})

                        # case "ATTYPE_AVI":
                        #     sensors_row.append({"type": 52, "state": "N", "slave": int(dev_i[1])})
                        # case "ATTYPE_AR5":
                        #     sensors_row.append({"type": 55, "state": "N", "slave": int(dev_i[1])})
                        # case "ATTYPE_ARMINI":
                        #     sensors_row.append({"type": 56, "state": "N", "slave": int(dev_i[1])})

                        # case "ATTYPE_IRS":
                        #     sensors_row.append({"type": 59, "state": "N", "slave": int(dev_i[1])})
                        # case "ATTYPE_ISM5":
                        #     sensors_row.append({
                        #         "type": 61,
                        #         "state": "N",
                        #         "slave": int(dev_i[1]),
                        #         "serialnumber": dev_i.serialnumber,
                        #         "err": None,
                        #         "trainr1": dev_i.trainr1,
                        #         "trainr2": dev_i.trainr2
                        #     })
                        # case "ATTYPE_ISM22_1":
                        #     sensors_row.append({"type": 62, "state": "N", "slave": int(dev_i[1])})
                        # case "ATTYPE_ISM22_2":
                        #     sensors_row.append({"type": 63, "state": "N", "slave": int(dev_i[1])})
                        # case "ATTYPE_ISM4":
                        #     sensors_row.append({
                        #         "type": 64,
                        #         "state": "N",
                        #         "slave": int(dev_i[1]),
                        #         "serialnumber": dev_i.serialnumber,
                        #         "err": None,
                        #         "trainr1": dev_i.trainr1,
                        #         "trainr2": dev_i.trainr2
                        #     })

                        # case "ATTYPE_OSZ":
                        #     sensors_row.append({"type": 66, "state": "N", "slave": int(dev_i[1])})
                        # case "ATTYPE_OSZ9":
                        #     sensors_row.append({"type": 67, "state": "N", "slave": int(dev_i[1])})


                # out_list.append({"port": row_i[0], "net_device": row_i[1],
                #                  "net_dev": "KAU03DConfig", "sensors": sensors_row})
                # sensors_sort = sorted(sensors_row, key=lambda s: s["slave"])
                # out_list.append({"port": row_i[0],
                #                  "net_device": row_i[1],
                #                  "net_dev": "KAU03DConfig",
                #                  "sensors": sorted(sensors_row, key=lambda s: s["slave"])})

            elif row_i[1][1] == "SKAU03Config":
                stmt_ad = select(SKAU03Config).where(
                    SKAU03Config.id == row_i[1][0],
                    SKAU03Config.deleted == 0)
                ans = conn.execute(stmt_ad).one()
                devs = ans.sensoraddressarray.split("=")

                for dev_i in devs:
                    description_dev = dev_i.split("|")
                    match description_dev[0]:
                        case "SKAU03ADDRESSTYPE_MD_EIPR":
                            sensors_row.append({"type": 1, "state": "N", "slave": int(description_dev[1])})
                        case  "SKAU03ADDRESSTYPE_MD_GELIOS3IK":
                            sensors_row.append({"type": 2, "state": "N", "slave": int(description_dev[1])})
                        case  "SKAU03ADDRESSTYPE_MD_EIPT":
                            sensors_row.append({"type": 3, "state": "N", "slave": int(description_dev[1])})
                        case  "SKAU03ADDRESSTYPE_MD_KRECHET":
                            sensors_row.append({"type": 4, "state": "N", "slave": int(description_dev[1])})
                        case  "SKAU03ADDRESSTYPE_MD_PHOENIX":
                            sensors_row.append({"type": 5, "state": "N", "slave": int(description_dev[1])})
                        case  "SKAU03ADDRESSTYPE_MD_IPESIKUF":
                            sensors_row.append({"type": 6, "state": "N", "slave": int(description_dev[1])})
                        case  "SKAU03ADDRESSTYPE_MD_MIP":
                            sensors_row.append({"type": 7, "state": "N", "slave": int(description_dev[1])})
                        case  "SKAU03ADDRESSTYPE_MD_IPA":
                            sensors_row.append({"type": 8, "state": "N", "slave": int(description_dev[1])})
                        case  "SKAU03ADDRESSTYPE_MD_AI":
                            sensors_row.append({"type": 9, "state": "N", "slave": int(description_dev[1])})
                        case  "SKAU03ADDRESSTYPE_MD_EXIP535":
                            # sensors_row.append({"type": 10, "state": "N", "slave": int(description_dev[1])})
                            ...
                        case  "SKAU03ADDRESSTYPE_MD_VEGA":
                            # sensors_row.append({"type": 11, "state": "N", "slave": int(description_dev[1])})
                            ...
                        case  "SKAU03ADDRESSTYPE_NO":
                            ...
                        case  _:
                            logger.info(description_dev[0])

                # out_list.append({"port": row_i[0],
                #                  "net_device": row_i[1],
                #                  "net_dev": "SKAU03Config",
                #                  "sensors": sorted(sensors_row, key=lambda s: s["slave"])})

    return out_list


def create_controller(sensors, net_dev):
    """
    :param sensors:[{'type': 'А2ДПИ', 'state': 'Норма', 'slave': 1, 'serialnumber': '1', 'state_cod': None}, {...},]
    :param net_dev: ('COM6', (24, 'KAU03DConfig', 'КАУ03Д->700', 700), 641)
    :return controller:
    [
        {'port: COM5,
        'controllers'; [
            {'net_device': 'КАУ03Д->5843',
            'net_dev': 'KAU03DConfig',
            'sn_net_dev': "5843",
            'sn_emul': "641",
            'sensors': [
                {'type': 51, 'state': 'N', 'state_cod': 0, 'slave': 1, 'serialnumber': '10'},
                {...},]
            {...},],
        {...},
    ]
    """
    controller = {
        'net_device': net_dev[1][2],
        'net_dev': net_dev[1][1],
        'sn_net_dev': net_dev[1][3],
        'sn_emul': int(net_dev[2]),
        'sensors': sensors
    }
    return controller
