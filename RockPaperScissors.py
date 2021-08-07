import random as rn

hscore, cscore=0,0
print("Welcome to the Rock Paper Scissors Game!!")
print("You'll be playing this against the computer! So  Let's Begin!!")
gchoice="yes"
while(gchoice.casefold()=="yes"):
    print("Enter your Choice in number: ","0. Rock", "1. Paper", "2. Scissors", sep="\n")
    options=["Rock", "Paper", "Scissors"]
    humanchoice=int(input())
    print("You chose: ",options[humanchoice])

    compchoice=rn.randint(0, len(options)-1)
    print("Computer Chose: ", options[compchoice])

    if humanchoice==compchoice:
        hscore+=1
        cscore+=1
        print("Its a Draw!!")
    elif(humanchoice==1 and compchoice==0) or (humanchoice==0 and compchoice==2) or (humanchoice==2 and compchoice==1):
        hscore+=1
        print("You won!")
    else:
        cscore+=1
        print("Computer Won.")

    gchoice=input("Do you wish to play again:(yes/no)")
    if(gchoice.casefold()=="no"):
        print("End of Game.")
        print("Your Score is: ", hscore)
        print("Computer Score is: ", cscore)
        if(hscore>cscore):
            print("You won!")
        elif(hscore==cscore):
            print("Its a draw")
        else:
            print("Computer Won.")


ran=input("Press any key..")