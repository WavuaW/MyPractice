import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password123'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create the database
cursorObject.execute('CREATE DATABASE chrisco')

print("All Done!")
