import mysql.connector

db = mysql.connector.connect(
    host = 'localhost', 
    user = 'root',
    passwd = 'Admin123',
)

cursor = db.cursor()

cursor.execute("CREATE DATABASE mydb")

print('All Done!')