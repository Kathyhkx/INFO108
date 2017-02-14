#kh Create a function to test if the student is passed or failed
def passOrFail(exam, programsDone):
    if(exam>=60 and programsDone>=10):
        print("PASSED")
    else:
        print("FAILED")

#kh Test with several sets of data in main()
def main():
    passOrFail(80,8)
    passOrFail(50,12)
    passOrFail(90,12)
    passOrFail(59,9)

#kh Call the main()
main()
