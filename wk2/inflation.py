#kh This program ask the user to enter the old price and new price of an item
#kh And then it calculates the inflation rate of the item


#kh A function that calculates the inflation rate based on prices
def inflation(newPrice, oldPrice):
    inflationRate = float("{0:.4f}".format((newPrice - oldPrice)/oldPrice))
    output = str(inflationRate*100) + "%"
    return output

#kh A main function that asks user input and call the calculation function
def main():
    oldPrice = float(input("Please enter the price of the item one year ago: "))
    newPrice = float(input("Please enter the price of the item today: "))
    #kh call the calculation function
    rate = inflation(newPrice, oldPrice)
    print("The inflation rate is", rate)

#kh call the main
main()