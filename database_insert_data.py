import mysql.connector
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="python_data"

)
cursor=con.cursor()
query="insert into student (name,marks,age) values(%s,%s,%s)"
#data=("vaishnavi",88,21)
student=[
    ("priya",65,21),
    ("shruti",89,22),
    ("siddhi",99,24)
]
cursor.executemany(query,student)
con.commit()
print("inserted successfully")
con.close()