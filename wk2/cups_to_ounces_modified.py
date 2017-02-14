#kh define the main function which calls all three other functions

def main():
    #kh print the intro information
    intro()

    #kh get input of cups needed
    cups_needed = int(input('Enter the number of cups: '))

    #kh conver cups to ounces using the function
    cups_to_ounces(cups_needed)


#kh the function contains intro information prints
def intro():
    print ('This program converts measurements')
    print ('in cups to fluid ounces. For your')
    print ('reference the formula is:')
    print ('    1 cup = 8 fluid ounces')
    print ()


#kh define the function which calculates the number of ounces based on the number of cups
def cups_to_ounces(cups):
    ounces = cups * 8
    print ('That converts to', ounces, 'ounces.')

#kh call the main function
main()
