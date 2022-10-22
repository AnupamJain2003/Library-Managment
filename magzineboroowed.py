import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='user',database='stjohns')
mycursor=mydb.cursor()
def borrowmagzine():
    mycursor.execute("SELECT * FROM MAGZINE")
    MYRECORDS=mycursor.fetchall()
    bon=input('ENTERED THE NAME OF BORRWED MAGZINE')
    date1=input('ENTER DATE OF BORROW IN YYYY-MM-DD FORMATE')
    cn=input('ENTER NAME OF CUSTOUMER')
    flag=0
    for x in MYRECORDS:
        y=str(x[1])
        if(y==bon):
            flag=1
            break
    if(flag==1):
        mycursor.execute("UPDATE MAGZINE SET DATE_OF_BORROW='"+date1+"', CUSTOMER_NAME='"+cn+"', BORROWED_STATUS='Y' where MAGZINE_NAME='"+bon+"'")
        print("Magzine Borrowed")
    else:
        print("MAgzine not avilable")
    mydb.commit()

