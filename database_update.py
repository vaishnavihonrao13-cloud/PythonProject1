import mysql.connector
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="python_data"

)
cursor = con.cursor()
query="update student set name=%s where id =%s"
data=("yogita",2)
cursor.execute(query,data)
con.commit()
print("updated..")