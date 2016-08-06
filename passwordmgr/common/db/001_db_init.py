from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, create_engine

metadata = MetaData()
Base = declarative_base(metadata=metadata)

class User(Base):
    __tablename__ = 'user'

    id = Column(String(32), primary_key=True)
    name = Column(String(20), nullable=False, unique=True)
    status = Column(Integer, nullable=False)
    ext = Column(String(32), nullable=True)


class Billing(Base):
    __tablename__ = 'billing'
    id = Column(String(32), primary_key=True)
    user_id = Column(String(32), ForeignKey('user.id'))
    blob = Column(BLOB, nullable=True)


class Migrate(Base):
    __tablename__ = 'migrate_version'
    step = Column(String(32), primary_key=True)
    path = Column(String(128), nullable=False, unique=True)


def upgrade(engine):
    metadata.create_all(engine, checkfirst=True)
    return True


def downgrade(engine):
    metadata.drop_all(engine, checkfirst=True)
    return True

if __name__ == "__main__":
    engine = create_engine('sqlite:///file.db')
    upgrade(engine)