"""
Inputs: 1 string and 1 positive integer.
Outputs: print the string N times, where N = the integer argument

Requirement: 
    - validate that the 2nd arg is positive integer
    - validate that the string is not empty

Examples:
repeat('Hello', 3) => 
Hello
Hello
Hello


Algorithm:
1. If the 2nd argument is NOT a positive integer (integer and greater than 0)
        - print error message 
    else, continue
2. If the 1st string is empty: print error message
    else, continue
3. Iterate N times, where n is anargument 
    - for each iteration, print the string argument on a new line 

"""

def repeat(text, repeat_n_times):
    if not (isinstance(repeat_n_times, int) and repeat_n_times > 0):
        print('Error: 2nd argument should be a positive integer')
        return None

    if not (isinstance(text, str) and len(text.strip()) > 0):
        print('Error: 1st argument must be a non-empty string')
        return None

    for _ in range(repeat_n_times):
        print(text)

repeat(11, 1)
repeat(' ', 1)
repeat('abc', -2)
repeat('abc', 0)
repeat('abc', 'abc')

repeat('Hello', 3)
