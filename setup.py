from secretos import sqlcred, sensores
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from orm import Device, Sensor
import smability


def main():
    Base = declarative_base()

    engine = create_engine(f'mysql+mysqlconnector://{sqlcred.get("SQL_USER")}:{sqlcred.get("SQL_PASSWORD")}@{sqlcred.get("SQL_HOST")}/{sqlcred.get("SQL_DATABASE")}', echo=True)
    metadata = MetaData()
    metadata.reflect(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()
        
    for key in sensores:
        device_exists = session.query(Device).filter(Device.Token == sensores[key]).first()
        if not device_exists:
            device = Device(Nombre=key, Token=sensores[key], Status='new')
            session.add(device)
            session.commit()
            print(f"Device {device.Nombre} added")
            devSensores = smability.list_sensor(sensores.get(key))

            if devSensores is not None:
                for el in devSensores:
                    if int(el['idSensor']) < 1000:
                        sensor = Sensor(Sensor_No=el['idSensor'], Descript=el['description'], ID_Device=device.ID_Device)
                        session.add(sensor)
                        session.commit()
                        print(f"Sensor {sensor.Descript} added to device {device.Nombre}")
            else:
                device.Status = "error"
                session.commit()
    session.close()

if __name__ == "__main__":
    main()