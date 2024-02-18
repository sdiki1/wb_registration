from sqlalchemy import create_engine, Column, Integer, String, MetaData, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

user = "root"
password = "vukSTxKmPMF"
host = "213.226.127.94"
db_name = "buys_mp"
DATABASE_URL = f"postgresql://{user}:{password}@{host}/{db_name}"

engine = create_engine(DATABASE_URL) 
Base = declarative_base()


class SMS(Base):
    __tablename__ = 'sms'

    Id = Column(Integer, primary_key=True)
    Phone = Column(String)
    Tzid = Column(Integer)
    Sms = Column(Integer)

class Accounts(Base):
    __tablename__ = 'accounts'
    Id = Column(Integer, primary_key=True)
    Name = Column(String)
    Is_man = Column(Boolean)
    AuthV3 = Column(String)
    Date_active = Column(DateTime)
    Is_using = Column(Boolean)

class modems(Base):
    __tablename__ = "modems"

    Id = Column(Integer, primary_key=True)
    Ip = Column(String)
    Is_using = Column(Boolean)
    To_reboot = Column(Boolean)
    

Base.metadata.create_all(engine)

