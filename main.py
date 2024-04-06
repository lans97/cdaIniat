import model
import database
import secretos
import smability
from datetime import datetime, timedelta
import csv

#TODO Parsear información que devuelve el API y guardarlo apropiadamente en la base de datos

def setup() -> None:
    
    pass
        

def main():
    
    sensores = {"P.M. 2.5": 9, "P.M. 10": 8, "Ozono": 7, "CO": 2, "Temperatura": 12, "Humedad": 3}
    d0 = datetime.today() - timedelta(days=90)
    d1 = d0 + timedelta(minutes=5)
    data = smability.get_data(secretos.METEORO1, tuple(sensores.values()), d0, d1)
    data = [data[i][0] for i in range(len(data))]


    return 0

if __name__ == "__main__":
    main()