"""
Inputs: base number (a) and power value (n)
Output: return (a) to the power of (n)

Requirements
    - Input arguments must be numbers 
    - The function must use multiply function 
    - Edge case: if (n) is 0 result should be 1.    
    - Edge cases where (n) is negative. : result = 1 / a^^n

^2 = 1 * a * a  (multiplication 1 time)
^3 = 1 * a * a * a * a (multiplication 2 times)

Algorithm:
    START
    Validate that both base and power are numbers
    Set result to 1 
    Repeat n times: result = result * base
    return result 
    
    
"""
import math

def is_number(value):
    return isinstance(value, float) or isinstance(value, int)

def multiply(number1, number2):
    if not (is_number(number1) and is_number(number2)):
        raise ValueError('Error: Both values must be numbers')

    return number1 * number2


# Messing around with error handling here.
# Not usre yet what is the best approach for such cases.
def power(base, exponent):
    if not (is_number(base) and is_number(exponent)):
        raise ValueError('Error: Both values must be numbers')

    result = 1
    for _ in range(abs(exponent)):
        result = multiply(result, base)

    # If the power value is negative, the result is the opposite: 1 / result
    return result if exponent >= 0 else (1 / result)


try:
    print(power(2, 0) == 1)   # True
    print(power(-2, 3) == -8)  # True
    print(power(-2, 2) == 4)  # True
    print(power(4, 3) == 64) # True
    print(math.isclose(power(2, -2), 0.25)) # True
    print(power('abc', 1)) # Error
except ValueError:
    print('Error: Both values must be numbers')