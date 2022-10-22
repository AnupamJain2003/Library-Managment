import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='user',database='stjohns')
mycursor=mydb.cursor()
def displaybooks():
    z={'booklit','bookinfo','bookgen','bookkid','bookhist'}
    mycursor.execute('SELECT *FROM booklit where BORROWED_STATUS="Y"')
    MYRECORDS=mycursor.fetchall()
    for x in MYRECORDS:
        print(x[0],'\t',x[1],'\t',x[2],'\t',x[3],'\t',x[4],'\t',x[5])
    mycursor.execute('SELECT *FROM bookhist where BORROWED_STATUS="Y"')
    MYRECORDS=mycursor.fetchall()
    for x in MYRECORDS:
        print(x[0],'\t',x[1],'\t',x[2],'\t',x[3],'\t',x[4],'\t',x[5])
    mycursor.execute('SELECT *FROM bookgen where BORROWED_STATUS="Y"')
    MYRECORDS=mycursor.fetchall()
    for x in MYRECORDS:
        print(x[0],'\t',x[1],'\t',x[2],'\t',x[3],'\t',x[4],'\t',x[5])
    mycursor.execute('SELECT *FROM bookinfo where BORROWED_STATUS="Y"')
    MYRECORDS=mycursor.fetchall()
    for x in MYRECORDS:
        print(x[0],'\t',x[1],'\t',x[2],'\t',x[3],'\t',x[4],'\t',x[5])
    mycursor.execute('SELECT *FROM bookkid where BORROWED_STATUS="Y"')
    MYRECORDS=mycursor.fetchall()
    for x in MYRECORDS:
        print(x[0],'\t',x[1],'\t',x[2],'\t',x[3],'\t',x[4],'\t',x[5])



    
