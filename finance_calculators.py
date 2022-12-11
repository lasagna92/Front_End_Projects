import math
# Ask the user to choose between investment or bond
menu_i = 'investment - to calculate the amount of interest you\'ll earn on your investment'
menu_b = 'bond       - to calculate the amount you\'ll have to pay on home loan'
question1 = input('Choose either \'investment\' or \'bond\' from the menu below:\n' + '\n'
                  + menu_i + '\n' + menu_b + '\n')

# Based on the user choice for investment request more information
if question1.lower() == 'investment':
    deposit = int(input('Please enter the amount of money you want to deposit:\t'))     # Money to invest
    int_inv = int(input('Please enter the interest rate (%):\t'))   # Interest rate
    years = int(input('Please enter the years of investment:\t'))   # Years of investment
    interest = input('Would you like to apply for \'simple\' or \'compound\' interest?\t') # Simple or compound interest

    # Work out and display the achieved capital with simple interest
    if interest.lower() == 'simple':
        capital_s = deposit*(1+(int_inv/100)*years)
        print('\n')
        print(f'After {years} years with the {int_inv}% of interest rate your capital will amount at £{capital_s}.')
    # Work out and display the achieved capital with compound interest
    elif interest.lower() == 'compound':
        capital_c = round(deposit*(math.pow((1+(int_inv/100)), years)), 2)
        print('\n')
        print(f'After {years} years with the {int_inv}% of interest rate your capital will amount at £{capital_c}.')
    else:
        print('\n')
        print('Please enter a valid option.')

# Based on user choice on bond request more information, work out and display the amount of the monthly repayment
elif question1.lower() == 'bond':
    house_value = int(input('Please enter the value of the property:\t'))   # Value of the house
    int_bond = int(input('Please enter the interest rate (%):\t'))      # Interest rate
    months = int(input('Please enter the number of months to repay the bond:\t'))       # Month of repayment
    month_pay = round((house_value * ((int_bond/100)/12))/(1-(1+((int_bond/100)/12))**(-months)), 2)
    print('\n')
    print(f'For a bond of £{house_value} for {months} months with an interest rate of {int_bond}% '
          f'your monthly payments will be £{month_pay}.')
    
else:
    print('\n')
    print('Please enter a valid option.')
