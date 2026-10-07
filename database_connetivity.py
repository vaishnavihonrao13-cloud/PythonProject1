import mysql.connector
con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mydatabaseclass",
)
if con.is_connected():
    print("connected successfully")
