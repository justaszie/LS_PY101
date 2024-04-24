"""
--- PROBLEM ---
Input: number
Output: negative number passed as argument

Requirements:
    - If the number is negative,return as-is
    - If the number is positive, return negative of that number 
    - Assuming that it works with floats 

    
---- Example cases ----- 
print(negative(5) == -5)      # True
print(negative(-3) == -3)     # True
print(negative(0) == 0)       # True 

Data structures: integers

Algorithm:
START
1. If the argument is a number (int or float)
    - Continue
   else
    - print error message and return None
2. If the number is positive:
    - return negative form of number
   else:
    - return the number in argument 
"""

def negative(number):
    if not isinstance(number, (float, int)):
        print('Error: argument must be a number')
        return None

    return -number if number > 0 else number


print(negative('30') == -5)      # True
print(negative(-3) == -3)     # True
print(negative(0) == 0)       # True