import mysql.connector
import sys
mydb=mysql.connector.connect(host='localhost',user='root',password='user',database='stjohns')
mycursor=mydb.cursor()
def search():
    p=input("ENTER THE NAME OF THE BOOK")
    mycursor.execute("SELECT * FROM booklit")
    MYRECORDS=mycursor.fetchall()
    for x in MYRECORDS:
        if(x[1]==p):
            print(x[0],'\t',x[1],'\t',x[2],'\t',x[3],'\t',x[4],'\t',x[5])
            return()
    mycursor.execute("SELECT * FROM bookhist")
    MYRECORDS=mycursor.fetchall()
    for x in MYRECORDS:
        if(x[1]==p):
            print(x[0],'\t',x[1],'\t',x[2],'\t',x[3],'\t',x[4],'\t',x[5])
            return()
    mycursor.execute("SELECT * FROM bookgen")
    MYRECORDS=mycursor.fetchall()
    for x in MYRECORDS:
        if(x[1]==p):
            print(x[0],'\t',x[1],'\t',x[2],'\t',x[3],'\t',x[4],'\t',x[5])
            return()
    mycursor.execute("SELECT * FROM bookkid")
    MYRECORDS=mycursor.fetchall()
    for x in MYRECORDS:
        if(x[1]==p):
            print(x[0],'\t',x[1],'\t',x[2],'\t',x[3],'\t',x[4],'\t',x[5])
            return()
    mycursor.execute("SELECT * FROM bookinfo")
    MYRECORDS=mycursor.fetchall()
    for x in MYRECORDS:
        if(x[1]==p):
            print(x[0],'\t',x[1],'\t',x[2],'\t',x[3],'\t',x[4],'\t',x[5])
            return()
    print("THE BOOK IS NOT FOUND IN THE RECORDS")

