import mysql.connector
import model

def get_connection():
        try:
            conn = mysql.connector.connect(
            host="localhost", user="iniatserver",
            password="iniat",
            database="smability"
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
        result = cursor.fetchall()

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
        result = cursor.fetchall()
        return result

        if __debug__:
            print("LocationData retreived from database.")
    except mysql.connector.Error as error:
        print("MySQL Error at get_UserData_by_id : ", error)

    conn.close()