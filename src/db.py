# import os
# from sqlalchemy import create_engine, String, create_engine, Integer, Boolean, BigInteger
# from sqlalchemy.orm import declarative_base, mapped_column, Mapped, DeclarativeBase, sessionmaker
# from sqlalchemy.dialects.postgresql import BYTEA
#
# # user = os.getenv("USER_DB")
# # user1 = os.environ.get("USER_DB")
# # password = os.getenv("PASSWORD_DB")
# # name = os.getenv("NAME_DB")
# # host = 'localhost'
# # port = "5432"
#
# user = "postgres"
# password = "postgres"
# name = "idspoconfig"
# host = 'localhost'
# port = "5432"
#
#
# URL = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{name}"
#
# # schimas = 'information_schema'.,
#
# engine = create_engine(
#     URL,
#     # connect_args=
#     # echo=True
# )
#
# Session = sessionmaker(bind=engine)
# session = Session()
#
#
# # сетевые устройства
# # BISMConfig
# # IBP05DConfig
# # KA2Config
# # KAU03DConfig
# # KD2Config
# # PKR01DConfig
# # PKR02DConfig
# # PPD01Config
# # PSF03DConfig
# # SKAU01Config
# # SKAU03Config
# # SKIU01Config
# # SKIU02Config
# # SKUP01Config
# # UPS07Config
#
#
# class Base(DeclarativeBase):
#     pass
#
#
# class NetDevice(Base):
#     __tablename__ = "netdevice"
#
#     id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
#     type: Mapped[str] = mapped_column(String(250))
#     sync: Mapped[bool] = mapped_column(Boolean, default=False)
#     bcpid: Mapped[int] = mapped_column(BigInteger)
#     deleted: Mapped[int] = mapped_column(Integer, default=0)
#     attached: Mapped[bool] = mapped_column(Boolean, default=False)
#
#     __table_args__ = {'schema': 'configurator'}
#
#
# class KA2Config(Base):
#     __tablename__ = "ka2config"
#
#     id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
#     bcpid: Mapped[int] = mapped_column(BigInteger)
#     deleted: Mapped[int] = mapped_column(Integer, default=0)
#     ka2addresstraintable: Mapped[str] = mapped_column(String, nullable=True)
#
#     __table_args__ = {'schema': 'configurator'}
#
#
# class KAU03DConfig(Base):
#     __tablename__ = "kau03dconfig"
#
#     id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
#     bcpid: Mapped[int] = mapped_column(BigInteger)
#     deleted: Mapped[int] = mapped_column(Integer, default=0)
#     ka2addresstraintable: Mapped[str] = mapped_column(String, nullable=True)
#
#     __table_args__ = {'schema': 'configurator'}

# class SKAU01Config(Base):
#     __tablename__ = "skau01config"
#
#
# class SKAU03Config(Base):
#     __tablename__ = "skau03config"
#
#
# class SKIU01Config(Base):
#     __tablename__ = "skiu01config"
#
#
# class SKIU02Config(Base):
#     __tablename__ = "skiu02config"



