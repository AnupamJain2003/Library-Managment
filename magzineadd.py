import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='user',database='stjohns')
mycursor=mydb.cursor()
def additionm():
    mn=input('ENTER THE NAME OF THE MAGZINE')
    mp=input('ENTER THE PUBLISHER OF THE MAGZINE')
    mycursor.execute('SELECT MAX(S_No) FROM MAGZINE')
    sno=mycursor.fetchall()
    s=0
    for k in sno:
        for i in k:
            s=i
    s=s+1
    j=str(s)
    l='N'
    h='noname'
    d='2000-01-01'
    mycursor.execute('SELECT max(SHELVE_NUMBER) FROM MAGZINE')
    no=mycursor.fetchall()
    f=0
    for k in no:
        for i in k:
            f=i
    for i in range(0,s):
        if((i+1)%15==0):
            f=f+1
    y=str(f)               
    mycursor.execute("insert into magzine values("+j+",'"+mn+"','"+mp+"',"+y+",'"+l+"','"+d+"','"+h+"')")
    print("Record added")
    mydb.commit()
