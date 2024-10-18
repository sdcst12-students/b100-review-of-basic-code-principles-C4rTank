"""
### Assignment 2
#### Calculation of an investment with a recurring deposit
The simple interest formula only works if the principal or initial investment is not touched.  
If an amount is added to the principal every year, 
then the interest must be calculated and added along with the future deposit to determine the
 starting balance at the beginning of the next year.

For example, suppose you invest $100 every year, and earn 5% interest per year.
At the start of the first year, you will have your $100 that you invested.  
At the start of the second year, you will have the initial $100, 
$5 interest as well as an additional $100 that is invested in the second year, 
for a total of $205 dollars.  
Write a program that uses a for loop to determine the amount of money in an account after a certain number of years.

Criteria:
Your program should ask the user for
* the annual investment
* the annual interest rate (as a percentage)
* the number of years
* calculate the amount of money at the end of each year until the specified number of years has been reached.
* appropriate formatting and variable names will be important
* use a *for* loop to iterate through the years.

Sample data
annual investment: 100
rate: 5%
10 years
final balance: 1320.68

"""

TIMES = 0

INVESTMENT = input("Enter Annual investment : ")
while INVESTMENT != float:

    try:
        INVESTMENT = float(INVESTMENT)
        break
    except:
        print("Invalid Input")
        INVESTMENT = input("Enter Annual investment : ")
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

TIME = input("Enter Number of Years : ")
while TIME != float:

    try:
        TIME = float(TIME)
        break
    except:
        print("Invalid Input")
        TIME = input("Enter Number of Years : ")
    continue

MONEY = INVESTMENT
TIME = int(TIME)

#for loop
for TIMES in range(TIME):

    TIMES = TIMES + 1

    INTEREST = INVESTMENT * RATE

    INVESTMENT = INVESTMENT + INTEREST + MONEY

#fix
INVESTMENT = INVESTMENT - MONEY
INVESTMENT = round(INVESTMENT,2)

print("In",TIME,"years, you will have",INVESTMENT,"$")

#DONE


    

