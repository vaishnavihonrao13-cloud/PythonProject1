import mysql.connector
con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="python_data"
)
cursor = con.cursor()
query="""
    create table student(
    id int primary key auto_increment,
    name varchar(40) not null,
    marks int,
    age int)
"""
cursor.execute(query)
print("table created successfully")
