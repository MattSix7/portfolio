# Finance_calculators
# Request input "Investment" or "Bond" assign to the variable user_calculator
# Using lower() function, convert string to lower case
# if user_calculator is equal to "investment"
#   request input of "Value of deposit". Store as float
#   request input of "Interest rate as a percentage". Store as float
#   request input of "number of years deposit will be invested". Store as integer
#   request input of "simple interest" or "compund interest".
#   Assign to the variable "interest"
#   if interest is equal to "simple"
#       calculate final value using simple interest using formula A = P *(1 + r*t)
#       ‘r’ is the interest entered above divided by 100, e.g. if 8% is entered,
#       then r is 0.08.
#       ‘P’ is the amount that the user deposits.
#       ‘t’ is the number of years that the money is being invested.
#       ‘A’ is the total amount once the interest has been applied.
#   else
#       calculate final value using compund interest using formula A = P * math.pow((1+r),t)
#   output the final value of the investment
# else
#   request input of "Value of house". Store as integer
#   request input of "Interest rate as a percentage". Store as float
#   request input of "Number or monthly repayments". Store as integer
#   calculate the monthly repayment using the formula repayment = (i * P)/(1 - (1 + i)**(-n))
#   'P' = value of the house
#   'i' = interest rate
#   'n' = number of monthly repayments
#   output the monthly repayment amount
import math

# Explain calculator options to user
print('''
Welcome to the Hyperion Bank interest calculator.

Option 1, the investment calulator
    Here you can calculate the amount of interest you will earn on your investment.

Option 2, the bond repayment calculator
    Or you can calculate your repayments on a home loan.

Type "Investment" to use the investment calculator.

Type "Bond" to use the bond repayment calculator.
      ''')

# Ask user for input to determine which calculator is required

user_calculator = input("Please type the name of the calculator you require: ").lower()

# the if loop below runs code block for investment calculator
# when the word "investment" is entered

if user_calculator == "investment":
    print("")
    print("Please enter the following information: ")

    # request input to define three variables required for investment equation
    # deposit, interest rate, and length of investment

    initial_deposit = float(input('''
    Please enter how much you would like to deposit in pounds and pence (£0.00): £ '''))

    interest_rate = float(input('''
    Enter the percentage interest rate: '''))

    investment_years = int(input('''
    Please enter how long you wish to invest for in whole years: '''))

    # request simple or compound interest calculation
    # print final investment value with reminder of inputs
    interest = input('''
    Would you like to see the value of your investment with
    simple interest or compund interest?
        
        Please type "simple" or "compound": ''').lower()
    
    if interest == "simple":
        final_value = initial_deposit * (1 + (interest_rate / 100) * investment_years)
        print(f'''
            Your investment would be worth £ {round(final_value,2)}
            from your initial investment of £ {initial_deposit}
            over {investment_years} years
            at {interest_rate}% interest.
              ''')
        
    elif interest == "compound":
        final_value = initial_deposit * math.pow((1 + (interest_rate / 100)),investment_years)
        print(f'''
            Your investment would be worth £ {round(final_value,2)}
            from your initial investment of £ {initial_deposit}
            over {investment_years} years
            at {interest_rate}% interest.
              ''')

# the elif loop below runs code block for the bond calculator
# when the word "bond" is entered
# input for three variables requested to calculate bond repayments
# house value, interest rate, and number of monthly repayments

elif user_calculator == "bond":
    house_value = int(input('''
    Please enter the value of your house in whole pounds (Example: 100000): £ '''))

    interest_rate = float(input('''
    Please enter the percentage interest rate of the loan: '''))
    
    # monthly interest rate is defined here by 
    # dividing % interest rate by 100 then dividing by 12 months
    month_interest_rate = (interest_rate / 100) / 12

    num_payments = int(input('''
    Enter the number of monthly payments: '''))

    repayment = (month_interest_rate * house_value) / (1 - (1 + month_interest_rate)**(-num_payments))
    
    # print monthly repayment value (rounded to 2 decimal places)
    # with reminder of inputs
    print(f'''
    Your loan of £ {house_value}
    would be repayed in {num_payments} monthly repayments
    of £ {round(repayment,2)} per month
    at {interest_rate}% interest
            ''')

else:
    print("There has been an issue with your request. Please refresh the page.")

