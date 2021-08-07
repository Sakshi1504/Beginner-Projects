#from goto import goto, label
import mysql.connector

conn=mysql.connector.connect(host="localhost", user="root", passwd="sakshi", database="sakshidb")

mycursor=conn.cursor()

#mycursor.execute("Create table LoginData(id int(10), name nvarchar(50), username nvarchar(50), password nvarchar(50))")



print("Welcome to Login Trial System!!")
print("If you are already a member, please login, else register!","1. Login","2. Register",sep="\n")
choice=input()

while(True):
    if(choice.casefold()=='login'):
        user=input("Please enter User Name: ")
        pwd=input("Please enter your Password: ")
        fetchdataquery="Select username from LoginData where username='"+user+"'"
        mycursor.execute(fetchdataquery)
        uname=mycursor.fetchone()
        #print("uname: ",uname)
        #print("uname[0]: ", uname[0])
        if(uname!=None and uname[0]==user):
            fetchdataquery = "Select password from LoginData where username='" + user + "'"
            mycursor.execute(fetchdataquery)
            respwd = mycursor.fetchone()
            if respwd[0]==pwd:
                print("You are logged in Successfully!!")
                break;
            else:
                print("Wrong Password Entered. Try to login again.")
        else:
            print("User does not exist in the system, Please Register first.")
            choice='register'

    elif(choice.casefold()=='register'):
        name=input("Enter your full name: ")

        username=input("Enter username: ")
        usertest="Select * from LoginData where username='"+username+"'"
        mycursor.execute(usertest)
        for i in mycursor:
            if(i!=None):
                print("This username has already been taken up, try again.")
                username = input("Enter username: ")
        pwd=input("Enter password: ")
        insquery="insert into LoginData(name, username, password) values(%s,%s,%s)"
        udata=(name, username, pwd)
       # print("The tuple created is: ", udata)
        mycursor.execute(insquery, udata)
        conn.commit()
        print("You are registered now. Please try to Login.")
        #mycursor.execute("Select * from LoginData")
        choice='login'
    else:
        print("Wrong Choice!! Choose again.")
        choice=input()