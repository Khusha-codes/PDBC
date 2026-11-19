import mysql.connector

class database:
    def connect(self):
        conn = mysql.connector.connect(
            host = 'localhost',
            port = 3306,
            user = "root",
            password = "khushi",
            database = "pdbc"
            )
        return conn

    
