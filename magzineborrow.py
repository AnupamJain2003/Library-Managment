import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='user',database='stjohns')
mycursor=mydb.cursor()
def displaymagzine():
    mycursor.execute('SELECT *FROM MAGZINE where BORROWED_STATUS="Y"')
    MYRECORDS=mycursor.fetchall()
    for x in MYRECORDS:
        print(x[0],'\t',x[1],'\t',x[2],'\t',x[3])



