"""
PROBLEM
Input: year (integer)
Output: century of the input year (string value with appropriate suffix: 'st', 'nd' etc. )
Requirements:
    - Century starts with the 1st year (e.g. 2001 is 21st while 2000 is still 20th
    - Suffixes based on last digit:
        - 1: st
        - 2: nd 
        - 3: rd
        - 4...N: th 

Algorithm:
1..100: 1st | (98 // 100 = 0) + (98 % 100 = 98). Modulo 0 = 1st cent
101..200: 2nd | (156 // 100 = 1) + (156 % 100 = 56) = Modulo 1 = 2nd cent 
2001..2100: 21st | (2024 // 100 = 20) + (2024 % 100 = 24). Modulo 20 = 21st cent

If year % 100 = 0:
    century = year // 100
else
    century = year // 100 + 1

last_digit = century % 10 
math last digit:
    case 1 
    case 2...
    _ th 

    
Exceptions: 1st, 12th, 113th, 1011th.
"""

def get_century_suffix(century):
    # If the last 2 digits are in the 10s, we apply -th suffix. 
    if (century % 100) // 10 == 1:
        return 'th'
    else:
        match century % 10:
            case 1:
                return 'st'
            case 2:
                return 'nd'
            case 3:
                return 'rd'
            case _:
                return 'th'

def century(year):
    cent = (year // 100 + 1) if year % 100 != 0 else year // 100
    return f"{cent}{get_century_suffix(cent)}"

print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True
