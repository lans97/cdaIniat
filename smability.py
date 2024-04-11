# Wrapper para API de Smability
from datetime import datetime, timedelta
import requests
import logging

logger = logging.getLogger('smability_logger')
logger.setLevel(logging.DEBUG)  # Set the logging level as needed

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler = logging.FileHandler('smability.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def get_data(token: str, sensors: tuple, date_0: datetime, date_f: datetime):
    """Get sensor measures from date_0 to date_f"""
    start = date_0.replace(second=0, microsecond=0)
    end = date_f.replace(second=0, microsecond=0)
    delta = start - end
    if delta.seconds < 300:
        raise Exception("Delta time is smaller than 5 minutes")

    output = []
    url = 'http://smability.sidtecmx.com/smabilityapi/GetData?'
    for n in sensors:
        query = {'dtstart': start, 'dtend': end, 'token': token, 'idsensor': str(n)}
        logger.info(f"Getting data from {token}: {n}.")
        response = requests.get(url, params=query)
        data = response.json()
        if len(data) != 0:
            output.append(data[0])
        else:
            output.append({})

    return output

def list_sensor(token: str):
    """Get sensor description and IDs from a given device toke from a given device token"""
    url = 'http://smability.sidtecmx.com/smabilityapi/ListSensor?'
    query = {'token': token}
    response = requests.get(url, params=query)
    data = response.json()
    return data

def bio_box(token: str):
    """Get last data from sensor"""
    url = 'http://smability.sidtecmx.com/smabilityapi/BioBox?'
    query = {'token': token}
    response = requests.get(url, params=query)
    data = response.json()
    return data