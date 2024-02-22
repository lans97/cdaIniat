# Wrapper para API de Smability
from datetime import datetime, timedelta
import requests
import model

def get_data(token: str, sensors: tuple, date_0: datetime, date_f: datetime):
    start = date_0.replace(second=0, microsecond=0)
    end = date_f.replace(second=0, microsecond=0)
    delta = start - end
    if delta.seconds < 300:
        raise Exception("Delta time is smaller than 5 minutes")

    output = []
    url = 'http://smability.sidtecmx.com/smabilityapi/getdata?'
    for n in sensors:
        query = {'dtstart': start, 'dtend': end, 'token': token, 'idsensor': str(n)}
        response = requests.get(url, params=query)
        data = response.json()
        output.append(data)


    return output
