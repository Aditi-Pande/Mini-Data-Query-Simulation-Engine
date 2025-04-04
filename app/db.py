
import mysql.connector
from config import Config

def get_db_connection():
    try:
        return mysql.connector.connect(
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            database=Config.DB_NAME
        )
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        return None
