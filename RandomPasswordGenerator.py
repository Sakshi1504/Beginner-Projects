import random as rn
import string

print("Welcome to Random Password Generator!!")
print("Lets Begin with specifying the password Policy first: ")
numberofupchar=int(input("Enter the number of Upper case characters you want to have in Password. "))
numberoflowchar=int(input("Enter the number of Lower case characters you want to have in Password. "))
numberofspcl=int(input("Enter the number of special characters allowed: "))
numberofdig=int(input("Enter the number of digits allowed: "))

#passwd=rn.random()

#print(string.ascii_lowercase)
#print(string.ascii_uppercase)
#print(string.digits)
#print(string.punctuation)

caps=rn.sample(string.ascii_uppercase, numberofupchar)
print(caps)
lowercase=rn.sample(string.ascii_lowercase, numberoflowchar)
print(lowercase)
spcl=rn.sample(string.punctuation, numberofspcl)
print(spcl)
dig=rn.sample(string.digits, numberofdig)
print(dig)

passwd=caps+lowercase+spcl+dig

print("Your password is: ", str(passwd))

main=string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation

pwd=rn.sample(main,8)
password="".join(pwd)
print("pssword: ",password)