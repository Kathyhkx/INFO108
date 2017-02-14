#Project Name: Lab 1 Problem 2
#Date: 01/12/2017
#Programmer Name: Kexin Han
#Project Description: Calculate the area of a room from user input dimensions
print("Please input the room dimensions: ")
length = float(input("Length: "))
width = float(input("Width: "))
height = float(input("Height: "))
#kh calculate the area and store in a variable
area = length * width * 2 + length * height * 2 + width * height * 2
#kh print out the area result
print("The total area is:", area)