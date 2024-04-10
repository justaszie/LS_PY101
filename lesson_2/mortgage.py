def is_valid_amount(amount_str):
    try:
        # The amount should be positive and above defined minimum float
        return float(amount_str) >= MINIMUM_AMOUNT
    except ValueError:
        return False

def is_valid_apr(apr_str):
    try:
        # APR can be either null or positive float
        return float(apr_str) >= 0
    except ValueError:
        return False

def is_valid_duration(duration_str):
    try:
        # Entered duration must be a positive integer. Float not accepted.
        duration_int = int(duration_str)
        return (duration_int > 0 and float(duration_str) == duration_int)
    except ValueError:
        return False

# We can define minimum loan amount here
MINIMUM_AMOUNT = 100

# Getting inputs and making sure they are valid
loan_amount = input('Enter the loan amount: $')
while not is_valid_amount(loan_amount):
    print(f'Invalid amount. Must be higher than {MINIMUM_AMOUNT}. Try again.')
    loan_amount = input('$')
loan_amount = float(loan_amount)

apr = input('Enter the annual interest rate percent value (e.g. 2.50): ')
while not is_valid_apr(apr):
    print('Invalid APR. It must be either 0 or a positive number. Try again')
    apr = input()
apr = float(apr) / 100

loan_duration_years = input('Enter the loan duration in years: ')
while not is_valid_duration(loan_duration_years):
    print('Invalid duration. Must be a positive whole number. Try again.')
    loan_duration_years = input()
loan_duration_years = int(loan_duration_years)

# Calculating monthly interest rate if it's non-0
monthly_rate = apr / 12 if apr > 0 else 0

# Calculating loan duration in months
loan_duration_months = loan_duration_years * 12

# Calculating and printing out the monthly payment
if monthly_rate:
    monthly_payment = (
        loan_amount *
        (monthly_rate / (1 - (1 + monthly_rate) ** (-loan_duration_months)))
    )
else:
    monthly_payment = loan_amount / 12
print(f'Monthly payment is: ${monthly_payment:.2f}')