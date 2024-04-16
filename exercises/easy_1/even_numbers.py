"""
PEDAC:

Input: no input
Output: printed even numbers from 1 to 99

Requirements: 
print even numbers from 1 to 99. Each number printed on its own line
Even number is a number that has no remainder when divided by 2

Examples:
2
4
6
...
98

Data structure: any sequence that allows to iterate from 1 to 99

Algorithm:
Iterate over numbers from 2 to 98, by skipping one number on each iteration. 

"""

even = [print(i) for i in range(2,99, 2)]