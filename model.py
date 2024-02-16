from datetime import datetime
import mysql.connector
import sys

def get_connection():
        try:
            conn = mysql.connector.connect(
            host="localhost",
            user="iniatserver",
            password="iniat",
            database="smability"
            )
            return conn
        except mysql.connector.Error as error:
            print("MySQL Error at get_LocationData: ", error)

    

class LocataionData:
    """Ubicación de cada sensor, no puede ser cambiada"""
    def __init__(self, idLocation: int, place: str, latitude: float, longitud: float):
        self.idLocation = idLocation
        self.place = place
        self.Latitude = latitude
        self.longitud = longitud
    
    def get_by_id(self, value: int):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            query = "SELECT idLocation, Place, Latitude, Longitude FROM LocationData WHERE idLocation = {}".format(value)
            cursor.execute(query)
            result = cursor.fetchall()

            if __debug__:
                print("LocationData retreived")
        except mysql.connector.Error as error:
            print("MySQL Error at get_LocationData: ", error)

        conn.close()
    
    def post(self):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            query = "SELECT idLocation, Place, Latitude, Longitude FROM LocationData WHERE idLocation = {}".format(value)
            cursor.execute(query)
            conn.commit()
            if __debug__:
                print("LocationData retreived")
        except mysql.connector.Error as error:
            print("MySQL Error at get_LocationData: ", error)

        conn.close()


class UserData:
    """Información de usuarrio"""
    def __init__(self, idUser: int, username: str):
        self.idUser = idUser
        self.username = username

class Report:
    """Reporte de medición"""
    def __init__(self, idReport: int, reportName: str, startDate: datetime, endDate: datetime, idUser: int):
        self.idReport = idReport
        self.reportName = reportName
        self.startDate = startDate
        self.endDate = endDate
        self.idUser = idUser

class Sensor:
    """Sensor information"""
    def __init__(self, idSensor: int, alias: str, token: int, deviceMode: int, idLocation: int):
        self.idSensor = idSensor
        self.alias = alias
        self.token = token
        self.deviceMode = deviceMode
        self.idLocation = idLocation

class Alert:
    """Clase Alerta"""
    def __init__(self, idAlert: int, timeData: datetime, information: str, idSensor: int):
        self.idAlert = idAlert
        self.timeData = timeData
        self.information = information
        self.idSensor = idSensor

class Measure:
    """Meta datos sobre medida"""
    def __init__(self, idMeasure: int, idSmability: int, kindMeasure: str, units: str):
        self.idMeasure = idMeasure
        self.idSmability = idSmability
        self.kindMeasure = kindMeasure
        self.units = units

class Sample:
    """Medida y relaciones"""
    def __init__(self, idSample: int, sampleNumber: int, timeData: datetime, sampleData: float, idReport: int, idSensor: int, idMeasure: int):
        self.idSample = idSample
        self.sampleNumber = sampleNumber
        self.timeData = timeData
        self.sampleData = sampleData
        self.idReport = idReport
        self.idSensor = idSensor
        self.idMeasure = idMeasure