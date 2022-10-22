import bookdisplaycat #d
import bookadd
import booksearch #d
import borrowbook #d
import borrowbookdisplay #d
import bookdisplay
import bookdisplayborrowcat
import magzineadd
import magzineboroowed
import magzinedisplay
import magzinesearch
import magzineborrow
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='user',database='stjohns')
mycursor=mydb.cursor()
k="ANUABHVAS"
print("                  HELLO USER")
print('              WELLCOME TO OUR LIBARY')
pas=input("ENTER YOUR PASSWORD PLEASE")
if(pas==k):
    while True:
        print("ENTER THE SECTION THE SECTION EHICH YOU WANT TO INQUIRE TODAY")
        print("PRESS 1 FOR BOOKS")
        print("PRESS 2 FOR MAGZINE")
        print('PRESS 3 FOR QUIT')
        c=int(input())
        if(c==1):
            while True:
                print("ENTER THE TASK YOU WANT TO PERFORM")
                print("PRESS 1 FOR ADDING NEW BOOK TO THE LIBARY")
                print("PRESS 2 FOR BORROWING A BOOK FROM LIBARY")
                print("PRESS 3 FOR DISPLAYING ALL BOOK OF THE LIBARY")
                print("PRESS 4 FOR DISPLAYING ALL BOOK OF THE LIBARY OF PARTICULAR SECTION")
                print("PRESS 5 FOR DISPLAYING ALL BORROWED BOOK OF THE LIBARY")
                print("PRESS 6 FOR DISPLAYING ALL BORROWED BOOK OF THE LIBARY OF PARTICULAR SECTION")
                print("PRESS 7 FOR SEARCHING A BOOK")
                print("PRESS 8 FOR BACK")
                ch=int(input())
                if(ch==1):
                    bookadd.bookadd()
                elif(ch==2):
                    borrowbook.borrowbook()
                elif(ch==3):
                    bookdisplay.displaybooks()
                elif(ch==4):
                    bookdisplaycat.displaycategory()
                elif(ch==5):
                    borrowbookdisplay.displaybooks()
                elif(ch==6):
                    bookdisplayborrowcat.displayborrowcategory()
                elif(ch==7):
                    booksearch.search()
                elif(ch==8):
                    break
                else:
                    print("WRONG CHOICE")
        elif(c==2):
            while True:
                print("ENTER THE TASK YOU WANT TO PERFORM")
                print("PRESS 1 FOR ADDING NEW MAGZINE TO THE LIBARY")
                print("PRESS 2 FOR BORROWING A MAGZINE FROM LIBARY")
                print("PRESS 3 FOR DISPLAYING ALL MAGZINE OF THE LIBARY")
                print("PRESS 4 FOR DISPLAYING ALL BORROWED MAGZINE OF THE LIBARY")
                print("PRESS 5 FOR SEARCHING A MAGZINE")
                print("PRESS 6 FOR BACK")
                ch=int(input())
                if(ch==1):
                    magzineadd.additionm()
                elif(ch==2):
                    magzineboroowed.borrowmagzine()                    
                elif(ch==3):
                    magzinedisplay.displaymagzine()
                elif(ch==4):
                    magzineborrow.displaymagzine()
                elif(ch==5):
                    magzinesearch.searchm()
                elif(ch==6):
                    break
                else:
                    print("WRONG CHOICE")
        elif(c==3):
            break
        else:
            print("Wrong Choice")
                
            
