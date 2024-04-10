import secretos
import smability
from datetime import datetime, timedelta

devSensores = smability.list_sensor(secretos.sensores.get('IBERO2'))
sensor_ids = tuple([el['idSensor'] for el in devSensores])

current_time = datetime.now()
five_minutes_ago = current_time - timedelta(minutes=5)

measures_data = smability.get_data(secretos.sensores.get('IBERO2'), sensor_ids, five_minutes_ago, current_time)

for measure in measures_data:
    print(measure)
    print("")
