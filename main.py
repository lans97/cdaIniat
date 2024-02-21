import model
import database
import secretos
import smability
from datetime import datetime, timedelta

#TODO Parsear información que devuelve el API y guardarlo apropiadamente en la base de datos

def main():
    # # Ejemplo de como llenar estructuras
    # # sensors.py es un archivo con constantes para cada token eventualmente no será necesario
    # ld = model.LocationData("Lugar Prueba", 19.363166, 99.270527)
    # s1 = model.Sensor("Ibero 1", sensors.IBERO1, 1, ld.idLocation)
    # # Si no se ejecutan en orden, el id de "ld" no se encontrará en la DB lanzando un error de MySQL
    # database.post_LocationData(ld)
    # database.post_Sensor(s1)
    
    d0 = datetime.today() - timedelta(days=90)
    d1 = d0 + timedelta(minutes=5)
    smability.get_data(secretos.IBERO2, (9,12), d0, d1)

    return 0

if __name__ == "__main__":
    main()