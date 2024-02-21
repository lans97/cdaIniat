import mysql.connector
import model
import secretos

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

def post_LocationData(item: model.LocationData):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = "INSERT INTO LocationData (Place, Latitude, Longitude) VALUES ('{}', {}, {})".format(item.place, item.latitude, item.longitude)
        cursor.execute(query)
        conn.commit()
        if __debug__:
            print(cursor.rowcount, "record inserted.")
    except mysql.connector.Error as error:
        print("MySQL Error at post_LocationData: ", error)
    conn.close()

def get_LocationData_by_id(value: int):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM LocationData WHERE idLocation = {}".format(value)
        cursor.execute(query)
        result = cursor.fetchall()[0]
        
        return model.LocationData(result[1], result[2], result[3], result[0])

        if __debug__:
            print("LocationData retreived from database.")
    except mysql.connector.Error as error:
        print("MySQL Error at get_LocationData_by_id : ", error)

    conn.close()

def post_UserData(item: model.UserData):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = "INSERT INTO userData (UserName) VALUES ('{}')".format(item.username)
        cursor.execute(query)
        conn.commit()
        if __debug__:
            print(cursor.rowcount, "record inserted.")
    except mysql.connector.Error as error:
        print("MySQL Error at post_UserData: ", error)
    conn.close()

def get_UserData_by_id(value: int):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM userData WHERE idUser = {}".format(value)
        cursor.execute(query)
        result = cursor.fetchall()[0]
        
        return model.UserData(result[1], result[0])

        if __debug__:
            print("UserData retreived from database.")
    except mysql.connector.Error as error:
        print("MySQL Error at get_UserData_by_id : ", error)

    conn.close()

def post_Report(item: model.Report):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = "INSERT INTO Report (RerportName, StartDate, EndDate, idUser) VALUES ('{}', '{}', '{}', {})".format(item.reportName, item.startDate, item.endDate, item.idUser)
        cursor.execute(query)
        conn.commit()
        if __debug__:
            print(cursor.rowcount, "record inserted.")
    except mysql.connector.Error as error:
        print("MySQL Error at post_Report: ", error)
    conn.close()

def get_Report_by_id(value: int):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM Report WHERE idReport = {}".format(value)
        cursor.execute(query)
        result = cursor.fetchall()[0]
        
        return model.Report(result[1], result[2], result[3], result[4], result[0])

        if __debug__:
            print("UserData retreived from database.")
    except mysql.connector.Error as error:
        print("MySQL Error at get_Report_by_id : ", error)

    conn.close()

def post_Sensor(item: model.Sensor):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = "INSERT INTO Sensor (Alias, Token, DeviceMode, idLocation) VALUES ('{}', {}, {}, {})".format(item.alias, item.token, item.deviceMode, item.idLocation)
        cursor.execute(query)
        conn.commit()
        if __debug__:
            print(cursor.rowcount, "record inserted.")
    except mysql.connector.Error as error:
        print("MySQL Error at post_Sensor: ", error)
    conn.close()

def get_Sensor_by_id(value: int):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM Sensor WHERE idSensor = {}".format(value)
        cursor.execute(query)
        result = cursor.fetchall()[0]
        
        return model.Report(result[1], result[2], result[3], result[4], result[0])

        if __debug__:
            print("UserData retreived from database.")
    except mysql.connector.Error as error:
        print("MySQL Error at get_Sensor_by_id : ", error)

    conn.close()

def post_Alert(item: model.Alert):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = "INSERT INTO Alert (TimeData, information, idSensor) VALUES ('{}', '{}', {})".format(item.timeData, item.information, item.idSensor)
        cursor.execute(query)
        conn.commit()
        if __debug__:
            print(cursor.rowcount, "record inserted.")
    except mysql.connector.Error as error:
        print("MySQL Error at post_Alert: ", error)
    conn.close()

def get_Alert_by_id(value: int):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM Alert WHERE idAlert = {}".format(value)
        cursor.execute(query)
        result = cursor.fetchall()[0]
        
        return model.Alert(result[1], result[2], result[3], result[0])

        if __debug__:
            print("UserData retreived from database.")
    except mysql.connector.Error as error:
        print("MySQL Error at get_Alert_by_id : ", error)

    conn.close()

def post_Measure(item: model.Measure):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = "INSERT INTO Measure (idSmability, kindMeasure, units) VALUES ({}, '{}', '{}')".format(item.idSmability, item.kindMeasure, item.units)
        cursor.execute(query)
        conn.commit()
        if __debug__:
            print(cursor.rowcount, "record inserted.")
    except mysql.connector.Error as error:
        print("MySQL Error at post_Measure: ", error)
    conn.close()

def get_Measure_by_id(value: int):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM Measure WHERE idMeasure = {}".format(value)
        cursor.execute(query)
        result = cursor.fetchall()[0]
        
        return model.Measure(result[1], result[2], result[3], result[0])

        if __debug__:
            print("UserData retreived from database.")
    except mysql.connector.Error as error:
        print("MySQL Error at get_Report_by_id : ", error)

    conn.close()

def post_Sample(item: model.Sample):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = "INSERT INTO Sample (SampleNumber, TimeData, SampleData, idReport, idSensor, idMeasure) VALUES ({}, '{}', {}, {}, {}, {})".format(
            item.sampleNumber, item.timeData, item.sampleData, item.idReport, item.idSensor, item.idMeasure)
        cursor.execute(query)
        conn.commit()
        if __debug__:
            print(cursor.rowcount, "record inserted.")
    except mysql.connector.Error as error:
        print("MySQL Error at post_Sample: ", error)
    conn.close()

def get_Sample_by_id(value: int):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM Sample WHERE idSample = {}".format(value)
        cursor.execute(query)
        result = cursor.fetchall()[0]
        
        return model.Sample(result[1], result[2], result[3], result[4], result[5], result[6], result[0])

        if __debug__:
            print("UserData retreived from database.")
    except mysql.connector.Error as error:
        print("MySQL Error at get_Sample_by_id : ", error)

    conn.close()