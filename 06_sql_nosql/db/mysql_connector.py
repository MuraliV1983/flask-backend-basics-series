import mysql.connector
from config import MYSQL_CONFIG

def get_mysql_connection():
    return mysql.connector.connect(**MYSQL_CONFIG)

# Optional test code at bottom - NO imports from this file here
if __name__ == "__main__":
    conn = get_mysql_connection()
    print("Connected:", conn.is_connected())
    conn.close()
