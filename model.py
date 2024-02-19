from datetime import datetime

class LocationData:
    """Ubicación de cada sensor, no puede ser cambiada"""
    def __init__(self, place: str, latitude: float, longitud: float, idLocation = 0):
        self.idLocation = idLocation
        self.place = place
        self.latitude = latitude
        self.longitud = longitud

    def __str__(self):
        return str(self.__dict__)[1:-1].replace("'", "")
    
class UserData:
    """Información de usuarrio"""
    def __init__(self, username: str, idUser = 0):
        self.idUser = idUser
        self.username = username

    def __str__(self):
        return str(self.__dict__)[1:-1].replace("'", "")

class Report:
    """Reporte de medición"""
    def __init__(self, reportName: str, startDate: datetime, endDate: datetime, idUser: int, idReport = 0):
        self.idReport = idReport
        self.reportName = reportName
        self.startDate = startDate.strftime('%Y-%m-%d %H:%M:%S')
        self.endDate = endDate.strftime('%Y-%m-%d %H:%M:%S')
        self.idUser = idUser

    def __str__(self):
        return str(self.__dict__)[1:-1].replace("'", "")

class Sensor:
    """Sensor information"""
    def __init__(self, alias: str, token: int, deviceMode: int, idLocation: int, idSensor = 0):
        self.idSensor = idSensor
        self.alias = alias
        self.token = token
        self.deviceMode = deviceMode
        self.idLocation = idLocation

    def __str__(self):
        return str(self.__dict__)[1:-1].replace("'", "")

class Alert:
    """Clase Alerta"""
    def __init__(self, timeData: datetime, information: str, idSensor: int, idAlert = 0):
        self.idAlert = idAlert
        self.timeData = timeData.strftime('%Y-%m-%d %H:%M:%S')
        self.information = information
        self.idSensor = idSensor

    def __str__(self):
        return str(self.__dict__)[1:-1].replace("'", "")

class Measure:
    """Meta datos sobre medida"""
    def __init__(self, idSmability: int, kindMeasure: str, units: str, idMeasure = 0):
        self.idMeasure = idMeasure
        self.idSmability = idSmability
        self.kindMeasure = kindMeasure
        self.units = units

    def __str__(self):
        return str(self.__dict__)[1:-1].replace("'", "")

class Sample:
    """Medida y relaciones"""
    def __init__(self, sampleNumber: int, timeData: datetime, sampleData: float, idReport: int, idSensor: int, idMeasure: int, idSample = 0):
        self.idSample = idSample
        self.sampleNumber = sampleNumber
        self.timeData = timeData.strftime('%Y-%m-%d %H:%M:%S')
        self.sampleData = sampleData
        self.idReport = idReport
        self.idSensor = idSensor
        self.idMeasure = idMeasure

    def __str__(self):
        return str(self.__dict__)[1:-1].replace("'", "")