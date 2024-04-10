"""
P: expected input / output; requirements explicit; rules. Mental models
E: examples
D: Data structure
A: algorithm
C: code 

Inputs: None
Outputs: list of odd numbers between 1 and 99, inclusive  

Requirements: print all the odd numbers between 1 and 99 inclusive. 
Each number must be printed on a separate line
Odd number: number that is divided by 2 has a non-0 remainder

E: examples:
1
3
5
... 

D: data structure: any sequence that can store a list of  numbers from 1 to 99. 

A: pseudo code 
V1: iterate through numbers 1 to 99 one by one
        if current number is odd, print it on its own line
        else: move to next number

V2: set iterator to 1: 
    iterate through numbers n to m
    print the number
    set iterator=iterator+2
"""

# V1:
# for i in range(1, 100):
#     if i % 2 != 0:
#         print(i)

# V2:
# i = 1
# while i <= 99:
#     print(i)
#     i += 2

# Further Exploration
def print_odd(first, last):
    for i in range(first, last+1):
        if i % 2 == 1:
            print(i)

first_num = int(input('Enter first number: '))
last_num = int(input('Enter last number: '))

print_odd(first_num, last_num)
