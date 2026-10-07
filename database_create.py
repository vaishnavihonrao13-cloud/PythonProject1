import mysql.connector
con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)
cursor=con.cursor()
cursor.execute("create database python_data")
print("data base created")
con.close()
