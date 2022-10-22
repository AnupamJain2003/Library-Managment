import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='user',database='library')
mycursor=mydb.cursor()
while True:
    print("Library Management")
    print("------------------")
    print("Chose one of the following choices")
    print("1.For inserting new records in the table")
    print("2.For displaying existing records")
    print("3.For quit")
    c=int(input("Enter your choice"))
    if(c==1):
        b_id=input("Enter the id of book")
        b_title=input("Enter the title of the book")
        b_subject=input("Enter the subject of the book")
        b_quan=input("Enter the number of the books")
        mycursor.execute("INSERT INTO BOOKS("+b_id+",'"+b_title+"','"+b_subject+"',"+b_quan+")")
    elif(c==2):
        mycursor.execute("SELECT * FROM BOOKS")
        myrec=mycursor.fetchall()
        print("The records are as follows")
        for r in myrec:
            print(r)
    elif(c==3):
        print("You have quit the program")
        break
    else:
        print("Please enter a valid choice")
        
    
