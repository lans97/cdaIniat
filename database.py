import mysql.connector
import model
import secretos

"""Devuelve una conexión a mySql/MariaDB"""
def get_connection():
        try:
            conn = mysql.connector.connect(
            host=secretos.SQLHOST,
            user=secretos.SQLUSER,
            password=secretos.SQLPASSWORD,
            database=secretos.SQLDATABASE
            )
            return conn
        except mysql.connector.Error as error:
            print("MySQL Error at get_connection: ", error)
            exit(-1)

"""Agrega un Location_Data a la bd y devuelve el ID"""
def post_Location_Data(item: model.Location_Data) -> int:
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = "INSERT INTO Location_Data (Place, Latitude, Longitude) VALUES (%s, %s, %s)"
        cursor.execute(query, (item.place, item.latitude, item.longitud))
        conn.commit()
        insert_id = cursor._last_insert_id
        conn.close()
        return insert_id
    except mysql.connector.Error as error:
        print("MySQL Error at post_Location_Data: ", error)

def get_Location_Data_by_id(value: int):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM LocationData WHERE ID_Location_Data = %s"
        cursor.execute(query, (value,))
        result = cursor.fetchone()
        conn.close()
        return model.Location_Data(id_Location=result[0], place=result[1], latitude=result[2], longitud=result[3])

    except mysql.connector.Error as error:
        print("MySQL Error at get_Location_Data_by_id : ", error)
        exit(-1)

def post_Device(item: model.Device):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = "INSERT INTO Device (Nombre, Token, ID_Location_Data) VALUES (%s, %s, %s)"
        cursor.execute(query, [item.nombre, item.token, item.location.id_Location])
        conn.commit()
        insert_id = cursor._last_insert_id
        conn.close()
        return insert_id
    except mysql.connector.Error as error:
        print("MySQL Error at post_Device: ", error)
        exit(-1)
        
def get_Device_by_id(value: int):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM Device WHERE id_Device = %s"
        cursor.execute(query, (value,))
        result = cursor.fetchone()
        conn.close()
        return model.Device(id_Device=result[0], nombre=result[1], token=result[2], location=get_LocationData_by_id(result[3]))
    except mysql.connector.Error as error:
        print("MySQL Error at get_Device_by_id: ", error)
        exit(-1)

def post_Sensor(item: model.Sensor):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = "INSERT INTO Sensor (ID_Sensor, Descript, ID_Device) VALUES (%s, %s, %s)"
        cursor.execute(query, (item.sensor, item.descript, item.Device.id_Device))
        conn.commit()
        insert_id = cursor._last_insert_id
        conn.close()
        return insert_id
    except mysql.connector.Error as error:
        print("MySQL Error at post_Sensor: ", error)

def get_Sensor_by_id(value: int):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM Sensor WHERE idSensor = %s"
        cursor.execute(query, (value,))
        result = cursor.fetchone()
        conn.close()
        return model.Sensor(id_Sensor=result[0], descript=result[1], device=get_Device_by_id(result[2]))

    except mysql.connector.Error as error:
        print("MySQL Error at get_Sensor_by_id : ", error)
        exit(-1)

def post_Measure(item: model.Measure):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = "INSERT INTO Measure (ID_Smability, Kind_Measure, Units) VALUES (%s, %s, %s)"
        cursor.execute(query, (item.id_Smability, item.kind_Measure, item.units))
        conn.commit()
        insert_id = cursor._last_insert_id
        conn.close()
        return insert_id
    except mysql.connector.Error as error:
        print("MySQL Error at post_Measure: ", error)
        exit(-1)

def get_Measure_by_id(value: int):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM Measure WHERE idMeasure = %s"
        cursor.execute(query, (value,))
        result = cursor.fetchone()
        conn.close()       
        return model.Measure(id_Measure=result[0], id_Smability=result[1], kind_Measure=result[2], units=result[3])
    except mysql.connector.Error as error:
        print("MySQL Error at get_Measure_by_id : ", error)
        exit(-1)

def post_Sample(item: model.Sample):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = "INSERT INTO Sample (Time_Data, Sample_Data, ID_Sensor, ID_Measure) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (item.time_Data.strftime('%Y-%m-%d %H:%M:%S'), item.sample_Data, item.sensor.id_Sensor, item.measure.id_Measure))
        conn.commit()
        insert_id = cursor._last_insert_id
        conn.close()
        return insert_id
    except mysql.connector.Error as error:
        print("MySQL Error at post_Sample: ", error)
        exit(-1)

def get_Sample_by_id(value: int):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM Sample WHERE ID_Sample = %s"
        cursor.execute(query, (value,))
        result = cursor.fetchone()
        conn.close()
        return model.Sample(id_Sample=result[0], time_Data=result[1], sample_Data=result[2], sensor=get_Sensor_by_id(result[3]), measure=get_Measure_by_id(result[4]))

    except mysql.connector.Error as error:
        print("MySQL Error at get_Sample_by_id : ", error)
        exit(-1)