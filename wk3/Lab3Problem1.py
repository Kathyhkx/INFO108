#Project Name: Lab 3 Problem 1
#Date: 02/02/2017
#Programmer Name: Kexin Han
#Project Description: The program helps the bookseller to award points to customers

#kh Create a function that has books as input and return points using simple if statement
def simpleIfFunction(books):
    points = 0
    if(books==0):
        points = 0
    if(books==1):
        points = 5
    if(books==2):
        points = 15
    if(books==3):
        points = 30
    if(books>=4):
        points = 60
    return points


