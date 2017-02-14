#Project Name: Lab 2 Problem 2
#Date: 01/26/2017
#Programmer Name: Kexin Han
#Project Description: The program gets monthly expenses from user and display total expense

#kh Declare showExpense() function, it accepts all monthly expenses as inputs
def showExpense(loan, insurance, gas, oil, tire, maintenance):
    monthlyExpense = loan + insurance + gas + oil + tire + maintenance
    yearlyExpense = 12 * monthlyExpense
    print('Total Monthly Expense: $' + '{0:.2f}'.format(monthlyExpense))
    print('Total Annual Expense: $' + '{0:.2f}'.format(yearlyExpense))

#kh Define Main() which asks user inputs and call the showExpense() function
def Main():
    loan = float(input('Monthly loan amount: '))
    insurance = float(input('Monthly insurance amount: '))
    gas = float(input('Monthly gas amount: '))
    oil = float(input('Monthly oil amount: '))
    tires = float(input('Monthly tires amount: '))
    maintenance = float(input('Monthly maintenance amount: '))

    #kh call function inside Main()
    print()
    showExpense(loan, insurance, gas, oil, tires, maintenance)

#kh Call the Main()
Main()

