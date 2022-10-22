import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='user',database='stjohns')
mycursor=mydb.cursor()
def displaybooks():
    z={'booklit','bookinfo','bookgen','bookkid','bookhist'}
    print("LITERATURE SECTION")
    mycursor.execute('SELECT *FROM booklit')
    MYRECORDS=mycursor.fetchall()
    for x in MYRECORDS:
        print(x[0],'\t',x[1],'\t',x[2],'\t',x[3],'\t',x[4],'\t',x[5])
    mycursor.execute('SELECT *FROM bookhist')
    MYRECORDS=mycursor.fetchall()
    print("HISTORY SECTION")
    for x in MYRECORDS:
        print(x[0],'\t',x[1],'\t',x[2],'\t',x[3],'\t',x[4],'\t',x[5])
    mycursor.execute('SELECT *FROM bookgen')
    MYRECORDS=mycursor.fetchall()
    print("G.KNOWLEDGE SECTION")
    for x in MYRECORDS:
        print(x[0],'\t',x[1],'\t',x[2],'\t',x[3],'\t',x[4],'\t',x[5])
    mycursor.execute('SELECT *FROM bookinfo')
    print("IMFORMATIVE SECTION")
    MYRECORDS=mycursor.fetchall()
    for x in MYRECORDS:
        print(x[0],'\t',x[1],'\t',x[2],'\t',x[3],'\t',x[4],'\t',x[5])
    mycursor.execute('SELECT *FROM bookkid')
    print("KIDS SECTION")
    MYRECORDS=mycursor.fetchall()
    for x in MYRECORDS:
        print(x[0],'\t',x[1],'\t',x[2],'\t',x[3],'\t',x[4],'\t',x[5])

