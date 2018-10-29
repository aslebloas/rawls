import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, VARCHAR, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker, scoped_session
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    user_ID = Column(VARCHAR(100), nullable = False, primary_key = True)
    user_name = Column(VARCHAR(50), nullable = False)
    user_email = Column(VARCHAR(50), nullable = False)
    user_password = Column(VARCHAR(20))
    devices = relationship("Devices", cascade="all, delete-orphan", backref= "User")

class Devices(Base):
    __tablename__ = "Devices"
    user_ID = Column(VARCHAR(100), ForeignKey(User.user_ID))
    device_SN = Column(VARCHAR(100), nullable = False, primary_key = True)
    device_brand = Column(VARCHAR(50))
    permissions = relationship("Permissions", cascade= "all, delete-orphan", backref="devices")

class Permissions(Base):
    __tablename__ = "Permissions"
    device_SN = Column(VARCHAR(100), ForeignKey (Devices.device_SN))
    gender = Column(Boolean)
    age = Column(Boolean)
    height = Column(Boolean)
    weight = Column(Boolean)
    heart_rate = Column(Boolean)
    sleeping_cycle = Column(Boolean)
    activity_frequency = Column(Boolean)

engine = create_engine(
    'mysql+mysqldb://test_user:test_123@localhost/RAWLS')

Base.metadata.create_all(engine)
Session = scoped_session(sessionmaker(bind=engine))