
#kh Create the commisionRate() function with if/else
def commisionRateCalc(sales):
    commisionRate = 0
    if (sales < 10000):
        commisionRate = 0.10
    else:
        if(sales>=10000 and sales<=15000):
            commisionRate = 0.15
        else:
            if(sales>15000):
                commisionRate = 0.20
    return commisionRate

#kh Test in main with 4 sample inputs
def main():
    commisionRate = commisionRateCalc(1000)
    print("The commision rate for $1000 is", commisionRate)
    commisionRate = commisionRateCalc(10000)
    print("The commision rate for $10000 is", commisionRate)
    commisionRate = commisionRateCalc(15000)
    print("The commision rate for $15000 is", commisionRate)
    commisionRate = commisionRateCalc(15001)
    print("The commision rate for $15001 is", commisionRate)

#kh Call the main()
main()
