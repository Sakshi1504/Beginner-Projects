import os

f=open("C:\\Users\\lenovo\\PycharmProjects\\pythonProject\\pythonProject\\NumberGuessingGameMain\\SearchWordinFile.py", "r")
count=0
#print(f.read())

search=input("Enter the word you want to search in file: ")
for i in f:
    #print("In")
    #print(i)
    if search in i:
        #print("inin")
        count+=1
    #print(i, sep=" ")

print("Number of occurences: ", count)