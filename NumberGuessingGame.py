import random


print("Welcome to Number Guessing Game.")
print("Computer will chosse the Number and it will be in range of 1-10")
num=random.randint(1,10)

#print(num)

trials=0

uc=int(input("Can you guess what is the number"))

while(True):
    if(uc==num):
        print("Yaayy!! You guessed the number right. You Won!!")
        print("You took ",trials, " trials.")
        trials+=1
        break;
    elif(uc>num):
        trials+=1
        print("You have entered a greater number. Try Again")
        uc = int(input("Can you guess what is the number"))
    elif(uc<num):
        trials+=1
        print("You have entered a smaller number. Try Again")
        uc = int(input("Can you guess what is the number"))


