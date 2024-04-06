from datetime import datetime

class Location_Data:
    """Ubicación de cada dispositivo"""
    def __init__(self, place: str, latitude: float, longitud: float, id_Location: int = 0) -> None:
        self.id_Location = id_Location
        self.place = place
        self.latitude = latitude
        self.longitud = longitud

    def __str__(self):
        return str(self.__dict__)[1:-1].replace("'", "")

class Device:
    """Dispositivo con varios sensores"""
    def __init__(self, nombre: str, token: str, location: Location_Data, id_Device: int = 0) -> None:
        self.id_Device = id_Device
        self.nombre = nombre
        self.token = token
        self.location = location

    def __str__(self):
        return str(self.__dict__)[1:-1].replace("'", "")

class Sensor:
    """Sensor individual"""
    def __init__(self, descript: str, device: Device, id_Sensor = 0) -> None:
        self.id_Sensor = id_Sensor
        self.descript = descript
        self.Device = device

    def __str__(self):
        return str(self.__dict__)[1:-1].replace("'", "")

class Measure:
    """Meta datos sobre medida"""
    def __init__(self, id_Smability: int, kind_Measure: str, units: str, id_Measure = 0):
        self.id_Measure = id_Measure
        self.id_Smability = id_Smability
        self.kind_Measure = kind_Measure
        self.units = units

    def __str__(self):
        return str(self.__dict__)[1:-1].replace("'", "")

class Sample:
    """Medida y relaciones"""
    def __init__(self, time_Data: str, sample_Data: float, sensor: Sensor, measure: Measure, id_Sample = 0):
        self.id_Sample = id_Sample
        self.time_Data = datetime.strptime(time_Data, '%Y-%m-%d %H:%M:%S')
        self.sample_Data = sample_Data
        self.sensor = sensor
        self.measure = measure

    def __str__(self):
        return str(self.__dict__)[1:-1].replace("'", "")