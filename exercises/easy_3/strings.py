"""
Input: positive integer
Output: string starting with 1 and alternating 1s and 0s

Algorithm:

START.
Iterate N number of times, where N is the integer argument
For each iteration, check if the iterator number is even:
    if even, add 0 to result
    else, add 1 to result
"""

def stringy(length):
    result = ''
    for i in range(length):
        result += '1' if i % 2 == 0 else '0'
    
    return result

print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True