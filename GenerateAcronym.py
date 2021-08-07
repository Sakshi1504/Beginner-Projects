userinput=input("Enter the word for which you want the acronym: ")
acr=""
for i in userinput.split(" "):
    acr=acr+i[0].upper()+"."

print(acr[:-1])