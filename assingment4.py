"""
### Assignment 4
#### Calculation of a debt repayment with recurring payments
This is the reverse of assignments 2 and 3

Calculate how long it will take to completely pay off a debt if regular payments are made.  
Note that each year, the debt will increase by the amount of loan interest, 
but will decrease with youre recurring payment. 

Criteria:
Your program should ask the user for
* an initial debt
* the annual interest rate
* the annual payment
* the program will state how long it will take for the debt to be repaid.
* extra: Calculate the total amount of interest that is paid along with the debt repayment

Sample:
Joey takes a car loan to buy a new Tesla for $62000
The loan has an annual interest rate of .75% per month.  He makes monthly payments of $1000.
How many months will it take him to pay off the car.  How much interest has he paid in that time?

84 months
He will have paid 21711.60 in interest
"""


AMOUNT = 0

DEBT = input("Enter Initial Debt : ")
while DEBT != float:

    try:
        DEBT = float(DEBT)
        break
    except:
        print("Invalid Input")
        DEBT = input("Enter Initial Debt : ")
    continue

RATE = input("Enter Interest Rate : ")
while RATE != float:

    try:
        RATE = float(RATE)
        break
    except:
        print("Invalid Input")
        RATE = input("Enter Interest Rate : ")
    continue

RATE = RATE/100

PAYMENT = input("Enter Annual Payment : ")
while PAYMENT != float:

    try:
        PAYMENT = float(PAYMENT)
        break
    except:
        print("Invalid Input")
        PAYMENT = input("Enter Annual Payment : ")
    continue

MONTH = 0
DEBT_DUE = DEBT
NUM = 0
INTEREST_PAYED = 0

while 0 < DEBT:
    
    #debt
    INTEREST_DEBT = DEBT * RATE
    DEBT = INTEREST_DEBT + DEBT
    DEBT = DEBT - PAYMENT

    MONTH = MONTH + 1

    #Payed in interest
    INTEREST_PAYED = INTEREST_DEBT + INTEREST_PAYED
    INTEREST_PAYED = round(INTEREST_PAYED,2)


print("Took",MONTH,"months to pay of debt.")
print("Paid",INTEREST_PAYED,"in interest.")

#DONE








    


