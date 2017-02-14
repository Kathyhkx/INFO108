#Project Name: Lab 2 Problem 1
#Date: 01/19/2017
#Programmer Name: Kexin Han
#Project Description: The program accept a distance in km and converts the value to miles

#kh Declare the rate of km to mile as a global value
KILOMETERS_TO_MILES = 0.6214

#kh Define the function showMiles()
def showMiles(kilometers):
    global KILOMETERS_TO_MILES
    miles = kilometers * KILOMETERS_TO_MILES
    print("The conversion of {} kilometers to miles: {} miles".format(kilometers, miles))

#kh Define the main function
def main():
    kilometers = float(input("Distance in kilometers: "))
    #kh call the function showmiles()
    showMiles(kilometers)

#kh Call the main()
main()