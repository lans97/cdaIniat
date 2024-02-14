class LocataionData:
    """Ubicación de cada sensor, no puede ser cambiada"""
    def __init__(self, idLocation, place, latitude, longitud):
        self.idLocation = idLocation
        self.place = place
        self.Latitude = latitude
        self.longitud = longitud

class UserData:
    """Información de usuarrio"""
    def __init__(self, idUser, username):
        self.idUser = idUser
        self.username = username

class Report:
    """Reporte de medición"""
    def __init__(self, idReport, reportName, startDate, endDate, idUser):
        self.idReport = idReport
        self.reportName = reportName
        self.startDate = startDate
        self.endDate = endDate
        self.idUser = idUser

class Sensor:
    """Sensor information"""
    def __init__(self, idSensor, alias, token, deviceMode, idLocation):
        self.idSensor = idSensor
        self.alias = alias
        self.token = token
        self.deviceMode = deviceMode
        self.idLocation = idLocation

class Alert:
    """Clase Alerta"""
    def __init__(self, idAlert, timeData, information, idSensor):
        self.idAlert = idAlert
        self.timeData = timeData
        self.information = information
        self.idSensor = idSensor

class Measure:
    """Meta datos sobre medida"""
    def __init__(self, idMeasure, idSmability, kindMeasure, units):
        self.idMeasure = idMeasure
        self.idSmability = idSmability
        self.kindMeasure = kindMeasure
        self.units = units

class Sample:
    """Medida y relaciones"""
    def __init__(self, idSample, sampleNumber, timeData, sampleData, idReport, idSensor, idMeasure):
        self.idSample = idSample
        self.sampleNumber = sampleNumber
        self.timeData = timeData
        self.sampleData = sampleData
        self.idReport = idReport
        self.idSensor = idSensor
        self.idMeasure = idMeasure