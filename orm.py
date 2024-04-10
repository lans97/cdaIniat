from secretos import sqlcred
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, TIMESTAMP, DECIMAL, Enum, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Device(Base):
    __tablename__ = 'Device'
    ID_Device = Column(Integer, primary_key=True, autoincrement=True)
    Nombre = Column(String(20))
    Token = Column(String(64))
    Status = Column(Enum('new', 'error', 'ok'))
    sensors = relationship("Sensor", back_populates="device")

class LocationData(Base):
    __tablename__ = 'Location_Data'
    ID_Location_Data = Column(Integer, primary_key=True, autoincrement=True)
    Place = Column(String(50))
    Latitude = Column(Float(10, 8))
    Longitude = Column(Float(10, 8))
    ID_Device = Column(Integer, ForeignKey('Device.ID_Device', ondelete='NO ACTION', onupdate='CASCADE'))
    device = relationship('Device', backref='locations')

class Sensor(Base):
    __tablename__ = 'Sensor'
    ID_Sensor = Column(Integer, primary_key=True)
    Sensor_No = Column(Integer, nullable=False)
    Descript = Column(String(40))
    ID_Device = Column(Integer, ForeignKey('Device.ID_Device'))
    device = relationship("Device", back_populates="sensors")

class Sample(Base):
    __tablename__ = 'Sample'
    ID_Sample = Column(Integer, primary_key=True, autoincrement=True)
    Time_Data = Column(TIMESTAMP, nullable=True)
    Sample_Data = Column(DECIMAL(10, 7))
    Units = Column(String(8))
    ID_Sensor = Column(Integer, ForeignKey('Sensor.ID_Sensor'), nullable=False)
    
if __name__ == "__main__":
    
    engine = create_engine(f'mysql+mysqlconnector://{sqlcred.get("SQL_USER")}:{sqlcred.get("SQL_PASSWORD")}@{sqlcred.get("SQL_HOST")}/{sqlcred.get("SQL_DATABASE")}', echo=True)
    Base.metadata.create_all(engine)