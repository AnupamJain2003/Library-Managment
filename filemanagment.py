import os
def createfile():
    f=open("story.txt","a")
    w=input("Enter a few words")
    f.write(w)
    print("The words has been added sucessfully to the file")
def read():
    f=open("story.txt","r")
    s=f.read()
    dict=s.split()
    n=0
    for i in dict:
        if(i[0]=='r')or(i[0]=='R'):
            n+=1
    print("The total number of words starting from r/R:",n)
while True:
    
    print("Text file editing")
    print("-----------------")
    print("Select the choice you want to maniuplate")
    print("1.For adding new text to the file")
    print("2.For reading the file and count the number of words starting with r/R")
    print("3.For exiting the program")
    c=int(input("Enter your choice"))
    if(c==1):
        createfile()
    elif(c==2):
        read()
    elif(c==3):
        print("You have quit the program")
        break
    else:
        print("Please enter a valid choice")


            
    
