import mysql.connector

db = mysql.connector.connect(
    host = 'localhost', 
    user = 'root',
    passwd = 'Admin123!',
)

cursor = db.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS finance")

print('All Done!')