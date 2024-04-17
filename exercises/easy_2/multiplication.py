"""
Input: 2 numbers 
Output: return multiplication of the 2 numbers

Requirements
    - Input arguments both must be numbers. Otherwise, return None
    - return  result of multiplying both numbers together 
"""

def is_number(value):
    return isinstance(value, float) or isinstance(value, int)

# Messng around with error handling here. Don't know yet what is the best approach for such cases. 
def multiply(number1, number2):
    if not (is_number(number1) and is_number(number2)):
        raise ValueError('Error: Both values must be numbers')
        # print('Error: Both values must be numbers')
    
    return number1 * number2

try:
    print(multiply(5, 3) == 15)  # True
    print(multiply(5, '3') == 15)  # True
except ValueError:
    print('Error: Both values must be numbers')