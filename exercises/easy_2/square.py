"""
Input: 1 number
Output: return square value of the number

Requirements
    - Input arguments must be a number
"""

def is_number(value):
    return isinstance(value, float) or isinstance(value, int)

def multiply(number1, number2):
    if not (is_number(number1) and is_number(number2)):
        raise ValueError('Error: Both values must be numbers')
        # print('Error: Both values must be numbers')
    
    return number1 * number2

# Messng around with error handling here. Don't know yet what is the best approach for such cases. 
def square(number):
    if not is_number(number):
        raise ValueError('Error: Both values must be numbers')
        # print('Error: Both values must be numbers')
    
    return multiply(number, number)

try:
    print(square(5) == 25)   # True
    print(square(-8) == 64)  # True
    print(square('abc')) # Error 
except ValueError:
    print('Error: Both values must be numbers')