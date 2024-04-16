# We can define minimum loan amount here
import os

MINIMUM_LOAN_AMOUNT = 100
ALLOW_NO_INTEREST = True


def prompt(message):
    print(f'==> {message}')


def get_loan_amount():
    # Getting inputs and making sure they are valid
    prompt('Enter the loan amount:')
    user_input = input('$')

    while not is_valid_amount(user_input):
        prompt(f'Invalid amount. Must be higher than {MINIMUM_LOAN_AMOUNT}. '
              'Try again.')
        user_input = input('$')
    return float(user_input)


def get_apr():
    prompt('Enter the annual interest rate percent value (e.g. 2.50): ')
    user_input = input()

    while not is_valid_apr(user_input):
        invalid_apr_message = (
            'Invalid APR. It must be 0 or a positive number. Try again.'
            if ALLOW_NO_INTEREST
            else 'Invalid APR. It must be a positive number. Try again.'
        )
        prompt(invalid_apr_message)
        user_input = input()

    apr = float(user_input) / 100
    return apr


def get_loan_duration_months():
    prompt('Enter the loan duration in years:')
    user_input = input()

    while not is_valid_duration_years(user_input):
        prompt('Invalid duration. Must be a positive number. '
               'Try again.')
        user_input = input()

    loan_duration_years = float(user_input)

     # Calculating loan duration in months - we round up to the next integer
    loan_duration_months = round(loan_duration_years * 12)

    return loan_duration_months


def is_valid_amount(amount_str):
    try:
        # The amount should be positive and above defined minimum float
        return float(amount_str) >= MINIMUM_LOAN_AMOUNT
    except ValueError:
        return False


def is_valid_apr(apr_str):
    try:
        apr_value = float(apr_str)
        return apr_value >= 0 if ALLOW_NO_INTEREST else apr_value > 0
    except ValueError:
        return False


def is_valid_duration_years(duration_str):
    try:
        # Entered duration must be positive
        return float(duration_str) > 0
    except ValueError:
        return False


def calculate_monthly_payment(loan_amount, monthly_interest_rate,
                              loan_duration):

    # Calculating the monthly payment value
    if monthly_interest_rate > 0:
        monthly_payment = (
            loan_amount *
            (
                monthly_interest_rate /
                (1 - (1 + monthly_interest_rate) ** (-loan_duration))
            )
        )
    else:
        monthly_payment = loan_amount / 12

    return monthly_payment


def display_monthly_payment(monthly_payment):
    print()
    prompt(f'Monthly payment is: ${monthly_payment:.2f}\n')


def calculate_again():
    prompt('Another calculation? Enter y or n')
    again_answer = input().lower().strip()

    while not (again_answer.startswith('y') or again_answer.startswith('n')):
        prompt('Please enter y or n')
        again_answer = input().lower().strip()

    return again_answer[0] == 'y'


def clear_screen():
    # If it's a windows OS
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def display_welcome_message():
    prompt('Welcome to the mortgage calculator.\n')

clear_screen()
display_welcome_message() 

while True:
    loan_amount = get_loan_amount()
    apr = get_apr()
    loan_duration = get_loan_duration_months()

    # Calculating monthly interest rate if it's non-0
    monthly_interest_rate = apr / 12 if apr > 0 else 0

    monthly_payment = calculate_monthly_payment(loan_amount,
                                                monthly_interest_rate,
                                                loan_duration)
    display_monthly_payment(monthly_payment)

    if not calculate_again():
        break

    clear_screen()