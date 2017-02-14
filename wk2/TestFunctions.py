#kh get user input values for part (a)
posInteger = int(input("Please enter a positive integer: "))
negInteger = int(input("Please enter a negative integer: "))
myChar = int(input("Please enter an integer between 48 to 122: "))
myString = input("Please enter a string: ")

#kh print absolute value of posInteger (b)
print("The absolute value of posInteger is", abs(posInteger))

#kh pring absolute value of negInteger (c)
print("The absolute value of negInteger is", abs(negInteger))

#kh print the character stored in myChar (d)
print("The character stored in myChar is", chr(myChar))

#kh print the length of the str (e)
print("The length of myString is", len(myString))

#kh raise the value of posInteger to the power 4 and print out the value (f)
myPower = posInteger ** 4
print("The power 4 of posInteger is", myPower)
