import logging
from datetime import datetime, timedelta
import time
from secretos import sqlcred
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from orm import Device, Sensor, Sample
import smability
import setup

# SQLALCHEMY LOGGING
logging.basicConfig(filename="sqlalchemy.log", level=logging.INFO)
sql_logger = logging.getLogger('sqlalchemy.engine')
sql_logger.setLevel(logging.INFO)
handler = logging.FileHandler('sqlalchemy.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
sql_logger.addHandler(handler)
engine = create_engine(f'mysql+mysqlconnector://{sqlcred.get("SQL_USER")}:{sqlcred.get("SQL_PASSWORD")}@{sqlcred.get("SQL_HOST")}/{sqlcred.get("SQL_DATABASE")}', echo=True)
engine.logger = sql_logger
Session = sessionmaker(bind=engine)

# SERVICE LOGGING
logger = logging.getLogger('cda_update')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler = logging.FileHandler('cdaUpdate.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def update():
    session = Session()
    
    try:
        devices = session.query(Device).filter(Device.Status != "error")

        for device in devices:
            if device.Status == "error":
                next
            token = device.Token
            
            sensors = device.sensors
            logger.info(f"Retreiving sensors from device {device.Nombre}")
            sensor_nos = [sensor.Sensor_No for sensor in device.sensors]
            
            current_time = datetime.now()
            five_minutes_ago = current_time - timedelta(seconds=300)
            measures_data = smability.get_data(token, sensor_nos, five_minutes_ago, current_time)

            for i, data in enumerate(measures_data):
                if data == {}:
                    continue
                timestamp_str = data.get('TimeStamp')
                timestamp = datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%S")
                formatted_timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')

                sensor_no = sensors[i].Sensor_No
                sensor_id = sensors[i].ID_Sensor
                data_value = data.get("Data")

                existing_sample = session.query(Sample).filter(Sample.Time_Data == formatted_timestamp, Sample.ID_Sensor == sensor_id).first()
                if existing_sample:
                    logger.warning("Sample already in database")
                else:
                    sample = Sample(Time_Data=formatted_timestamp, Sample_Data=data_value, Units="", ID_Sensor=sensor_id)
                    session.add(sample)
                    session.commit()
                    logger.info(f"Sensor [{sensors[i].Descript}] from Device [{device.Nombre}] updated.")
            device.Status = "ok"
            session.commit()
            time.sleep(5)
    except Exception as e:
        logger.error("Error:", e)
        exit(-1)
    finally:
        session.close()
    
    print("Succesfully updated. Waiting for next update...")

def main():
    while(True):
        last_update = datetime.now()
        update()
        wait_time = datetime.now() - last_update
        time.sleep(301 - wait_time.seconds)
    return 0

if __name__ == "__main__":
    main()