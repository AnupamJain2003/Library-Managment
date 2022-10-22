import mysql.connector
import sys
mydb=mysql.connector.connect(host='localhost',user='root',password='user',database='stjohns')
mycursor=mydb.cursor()
def bookadd():
    tn=('booklit','bookinfo','bookgen','bookkid','bookhist')
    sn=("LITERATURE","IMFORMATIVE","G.KNOWLEDGE","KIDS","HISTORY")
    print('ENTER THE GERNE OF BOOK YOU WANT TO ADD ')
    p=input()
    sy=""
    if(p=="LITERATURE"):
        i=tn[0]
        sy=sn[0]
    elif(p=="INFORMATIVE"):
        i=tn[1]
        sy=sn[0]
    elif(p=="KNOWLEDGEABLE"):
        i=tn[2]
        sy=sn[0]
    elif(p=="KIDS"):
        i=tn[3]
        sy=sn[0]
    elif(p=="HISTORICAL"):
        i=tn[4]
        sy=sn[0]
    else:
        print("Sorry the section is not avilable in our library")
        sys.exit()
    mn=input("ENTER THE NAME OF THE BOOK")
    ma=input("ENTER THE AUTHOR OF THE BOOK")
    mp=input("ENTER THE PUBLISHER OF THE BOOK")
    mycursor.execute('SELECT MAX(S_No) FROM '+i+'')
    sno=mycursor.fetchall()
    s=0
    for k in sno:
        for g in k:
            s=g
    s=s+1
    j=str(s)
    l='N'
    h='noname'
    d='2000-01-01'
    mycursor.execute('SELECT max(SHELVE_NUMBER) FROM '+i+'')
    no=mycursor.fetchall()
    f=0
    for k in no:
        for g in k:
            f=g
    for g in range(0,s):
        if((g+1)%15==0):
            f=f+1
    y=str(f)               
    mycursor.execute("insert into "+i+" values("+j+",'"+mn+"','"+ma+"','"+mp+"','"+sy+"',"+y+",'"+l+"','"+h+"','"+d+"')")
    print("Record added")
    mydb.commit()




