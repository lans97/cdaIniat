import model
import database
import sensors
import smability
from datetime import datetime, timedelta

#TODO Parsear información que devuelve el API y guardarlo apropiadamente en la base de datos

def main():
    # Ejemplo de como llenar estructuras
    # sensors.py es un archivo con constantes para cada token eventualmente no será necesario
    ld = model.LocationData("Lugar Prueba", 19.363166, 99.270527)
    s1 = model.Sensor("Ibero 1", sensors.IBERO1, 1, ld.idLocation)
    # Si no se ejecutan en orden, el id de "ld" no se encontrará en la DB lanzando un error de MySQL
    database.post_LocationData(ld)
    database.post_Sensor(s1)

if __name__ == "__main__":
    main()