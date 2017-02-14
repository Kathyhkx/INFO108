#kh The function to test if score is above 100 using if/else
def testScore(x):
    if (x > 100):
        print("High")
    else:
        print("Low")

#kh test testScore() function with 3 inputs in main
def main():
    testScore(120)
    testScore(100)
    testScore(90)

#kh Call the main()
main()
