import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pit5cxcy",
    database="TUTORIALS"
)

mycursor = mydb.cursor()

sqlcmd = "select column_name from information_schema.columns where table_name='tutorials_tbl'"

mycursor.execute(sqlcmd)

myresult = mycursor.fetchall()

for r in myresult:
    print(r)
