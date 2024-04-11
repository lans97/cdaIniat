from datetime import datetime, timedelta
import time
from secretos import sqlcred
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from orm import Device, Sensor, Sample
import smability
import setup

engine = create_engine(f'mysql+mysqlconnector://{sqlcred.get("SQL_USER")}:{sqlcred.get("SQL_PASSWORD")}@{sqlcred.get("SQL_HOST")}/{sqlcred.get("SQL_DATABASE")}', echo=True)
Session = sessionmaker(bind=engine)

def update():
    session = Session()
    
    try:
        devices = session.query(Device).filter(Device.Status != "error")

        for device in devices:
            if device.Status == "error":
                next
            token = device.Token
            sensors = [sensor for sensor in device.sensors]
            sensor_nos = tuple([sensor.Sensor_No for sensor in sensors])
            
            current_time = datetime.now()
            five_minutes_ago = current_time - timedelta(seconds=301)
            measures_data = smability.get_data(token, sensor_nos, five_minutes_ago, current_time)
            

            for data in measures_data:
                if len(data) == 0:
                    continue
                ts = data[0].get('TimeStamp').split("T")
                ts = ts[0] + " " + ts[1]
                index = measures_data.index(data)
                sensor_no = sensor_nos[index]
                f_result = list(filter(lambda sensor: sensor.Sensor_No == sensor_no, sensors))
                curr_sensor = f_result[0]
                data_value = data[0].get("Data")
                if data_value is None:
                    next
                sample = Sample(Time_Data=ts, Sample_Data=data_value, Units="", ID_Sensor=curr_sensor.ID_Sensor)
                session.add(sample)
                session.commit()
            device.Status = "ok"
            session.commit()
    except Exception as e:
        print("Error:", e)
        exit(-1)
    finally:
        session.close()


def main():
    while(True):
        update()
        time.sleep(300)
    return 0

if __name__ == "__main__":
    main()