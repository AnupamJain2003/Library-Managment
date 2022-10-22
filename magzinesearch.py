import mysql.connector
import sys
mydb=mysql.connector.connect(host='localhost',user='root',password='user',database='stjohns')
mycursor=mydb.cursor()
def searchm():
    p=input("ENTER THE NAME OF THE MAGZINE")
    mycursor.execute("SELECT * FROM MAGZINE")
    MYRECORDS=mycursor.fetchall()
    for x in MYRECORDS:
        if(x[1]==p):
            print(x[0],'\t',x[1],'\t',x[2],'\t',x[3],'\t',x[4],'\t',x[5])
            return()
    print("THE MAGZINE IS NOT FOUND IN THE RECORDS")

