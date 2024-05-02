from sqlalchemy import select

from app.db import session, NetDevice, KA2Config, KAU03DConfig


def get_data():
    stmt = select(NetDevice).where(NetDevice.deleted == 0, NetDevice.sync)
    ans = session.scalars(stmt).all()
    for i in ans:
        print(i.id, i.bcpid, i.sync, i.type, i.deleted)


if __name__ == "__main__":
    get_data()
