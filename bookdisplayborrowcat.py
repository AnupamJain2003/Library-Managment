import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='user',database='stjohns')
mycursor=mydb.cursor()
def displayborrowcategory():
    tn=('booklit','bookinfo','bookgen','bookkid','bookhist')
    print('ENTER THE GERNE OF BOOK YOU WANT TO DISPLAY')
    p=input()
    i=""
    if(p=="LITERATURE"):
        i=tn[0]
    elif(p=="INFORMATVE"):
        i=tn[1]
    elif(p=="KNOWLEDGEABLE"):
        i=tn[2]
    elif(p=="KIDS"):
        i=tn[3]
    elif(p=="HISTORICAL"):
        i=tn[4]
    else:
        print("Sorry the section is not avilable in our library")
    mycursor.execute("SELECT * FROM "+i+" where BORROWED_STATUS='Y'")
    MYRECORDS=mycursor.fetchall()
    for x in MYRECORDS:
        print(x[0],'\t',x[1],'\t',x[2],'\t',x[3],'\t',x[4],'\t',x[5])

