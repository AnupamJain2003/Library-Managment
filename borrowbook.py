import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='user',database='stjohns')
mycursor=mydb.cursor()
def borrowbook():
    tn=('booklit','bookinfo','bookgen','bookkid','bookhist')
    print('ENTER THE GERNE OF BOOK YOU WANT TO BORROW')
    p=input()
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
    mycursor.execute("SELECT * FROM "+i+"")
    MYRECORDS=mycursor.fetchall()
    bon=input('ENTERED THE NAME OF BORRWED BOOK')
    date1=input('ENTER DATE OF BORROW IN YYYY-MM-DD FORMATE')
    cn=input('ENTER NAME OF CUSTOUMER')
    h=0
    for x in MYRECORDS:
             if(x[1]==bon):
                 mycursor.execute("UPDATE "+i+" SET DATE_OF_BORROW='"+date1+"', CUSTOMER_NAME='"+cn+"', BORROWED_STATUS='Y' where Book_Name='"+bon+"'")
    print("Book borrowed")
    mydb.commit()

