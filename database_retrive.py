import mysql.connector
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="python_data"

)
cursor=con.cursor()
cursor.execute("select * from student")
records=cursor.fetchall()
print("id\tname\tmarks\tage")
for row in records:
    print(row)
con.close()