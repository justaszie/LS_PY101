"""
Inputs: 2 floating point numbers
Output: result of the following operations on the 2 numbers:
    - addition, 
    - subtraction, 
    - product, 
    - quotient, 
    - floor quotient, 
    - remainder, 
    - and power

Example Case 
    ==> Enter the first number:
3.141529
==> Enter the second number:
2.718282
==> 3.141529 + 2.718282 = 5.859811 # Addition
==> 3.141529 - 2.718282 = 0.42324699999999993 # Subtraction
==> 3.141529 * 2.718282 = 8.539561733178 # product 
==> 3.141529 / 2.718282 = 1.1557038600115808 # quotient 
==> 3.141529 // 2.718282 = 1.0 # floor quotient 
==> 3.141529 % 2.718282 = 0.42324699999999993 # remainder
==> 3.141529 ** 2.718282 = 22.45792517468373 # power 

Requirement: no need to validate the input 

"""
def calculate(number1, number2, operator):
    match operator:
        case '+': return number1 + number2
        case '-': return number1 - number2
        case '*': return number1 * number2
        case '/': return number1 / number2
        case '//': return number1 // number2
        case '%': return number1 % number2
        case '**': return number1**number2

def prompt(text):
    print(f'==> {text}')


# def display_result_addition(number1, number2):
#     prompt(f'{number1} + {number2} = {number1 + number2}')


# def display_result_subtraction(number1, number2):
#     prompt(f'{number1} - {number2} = {number1 - number2}')


# def display_result_product(number1, number2):
#     prompt(f'{number1} * {number2} = {number1 * number2}')


# def display_result_quotient(number1, number2):
#     prompt(f'{number1} / {number2} = {number1 / number2}')


# def display_result_floor_quotient(number1, number2):
#     prompt(f'{number1} // {number2} = {number1 // number2}')


# def display_result_remainder(number1, number2):
#     prompt(f'{number1} % {number2} = {number1 % number2}')


# def display_result_power(number1, number2):
#     prompt(f'{number1} ** {number2} = {number1**number2}')

prompt('Enter first number:')
first_number = float(input())

prompt('Enter second number:')
second_number = float(input())

# display_result_addition(first_number, second_number)
# display_result_subtraction(first_number, second_number)
# display_result_product(first_number, second_number)
# display_result_quotient(first_number, second_number)
# display_result_floor_quotient(first_number, second_number)
# display_result_remainder(first_number, second_number)
# display_result_power(first_number, second_number)

# FEEDBACK: this should have been a loop that iterates through operators and calculates and prints out the operation. My solution is too repetitive. 
# SOLUTION: rebuilt with an iteration


operators = ['+', '-', '*', '/', '//', '%', '**']
for operator in operators:
    print(f'{first_number} {operator} {second_number} = '
          f'{calculate(first_number, second_number, operator)}')