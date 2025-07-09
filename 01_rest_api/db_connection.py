import mysql.connector

def get_connection():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='server',
            database='rest_api'
        )
        return conn
    except Exception as exception:
        return None