import math
#Request imput from user
choose=input("Choose either 'investment' or 'bond' from the menu below to proceed:\n \ninvestment  -  to calculate the amount of interest you'll learn on your investment\nbond        -  the amount you'll have to pay on a home loan  \n").lower()

#If user choose investment,ask user the investment plan
if choose == "investment":
    money_amount=int(input("How much money would you like to deposit? \n"))
    interest_rate=float(input("Insert a number that corrispond to the interest rate \n"))
    year_time=int(input("Insert the number of years you plan on investing \n"))
    interest=input("Choose between simple and compound interest \n")
    
#Calculate and display  the 2 different interest plans
    if interest == "simple":
        interest=money_amount * (1 + (interest_rate / 100) * year_time)
        print(interest)
    elif interest == "compound":
        interest=money_amount * math.pow ((1 + (interest_rate / 100)), year_time)
        print(interest)
        
#If user choose bond, create home loan repayment calculator
elif choose =="bond":
    value_house=int(input("Insert the value of the house \n"))
    interest_rate=float(input("Insert a number that corrispond to the interest rate \n"))
    month_time=int(input("Insert the number of months you plan to take to repay the bond \n"))
    
#NB:I used this other formula that i found on the web because for me was a bit confusing the one on my task
    money_month=(interest_rate / 12) * (1 /( 1 - (1 + interest_rate /12) ** (- month_time))) * value_house
    print(money_month)

else:
    print("Error choice. Choose between Investment and Bond")
