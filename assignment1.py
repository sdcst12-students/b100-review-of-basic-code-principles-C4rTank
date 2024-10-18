"""
### Assignment 1
#### Calculation of Simple Interest
The simple interest formula is I = P*r*t where I = the amount of interest, P is the principal 
or the amount invested, r is the interest rate per year (converted to a decimal) and t is the 
length of time in years.
Write a program that calculates the amount of simple interest for an investment.

Criteria:
Your program should ask the user for 
* an initial investment
* the annual interest rate as a percentage
* the length of time.
  * the user should have the option of entering in the length of time in years, months or days
* The program will calculate the amount of interest earned and display it.
* Appropriate formatting of the output is a requirement for this assignment
"""

T = "a"
t = 0


#P
P = input("Enter Principal : ")

#check if P is a num
while P != float:

    try:
        P = float(P)
        break
    except:
        print("Invalid Input")
        P = input("Enter Principal : ")
    continue
    
#r
r = input("Enter Interest Rate : ")

#check if r is a num
while r != float:

    try:
        r = float(r)
        break
    except:
        print("Invalid Input")
        r = input("Enter Interest Rate : ")
    continue

#Convert r into percentage
r = r/100

#Year month or day?
while T != "y" or "m" or "d":
    print("For time would you like to enter Year/Month/Days")
    T = input("y/m/d : ")

#Year
    if T == "y":
        t = float(input("Enter Year : "))
    
        I = P * r * t

        #Results
        print("Your Interest :",I)
        break

#Month
    if T == "m":
        t = float(input("Enter Month : "))

        t = t/12
        I = P * r * t

        #Results
        print("Your Interest :",I)
        break

#Day
    if T == "d":
        t = float(input("Enter Days : "))
        
        t = t/365
        I = P * r * t

        #Results
        print("Your Interest :",I)
        break

#DONE
