"""
Input: year - integer greater than 0

Output: if the number is a leap year or not (True / False)

Algorithm:
if year divisible by 400: 
    return true
else if year divisible by 100:
    return false
else if year divisble by 4:
    return true

return false

"""

GREGORIAN_START = 1752

def is_leap_year(year):
    if year < GREGORIAN_START:
        return year % 4 == 0
    else: 
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        else:
            return year % 4 == 0

# These examples should all print True
# These examples should all print True
print(is_leap_year(1) == False)
print(is_leap_year(2) == False)
print(is_leap_year(3) == False)
print(is_leap_year(4) == True)
print(is_leap_year(1000) == True)
print(is_leap_year(1100) == True)
print(is_leap_year(1200) == True)
print(is_leap_year(1300) == True)
print(is_leap_year(1751) == False)
print(is_leap_year(1752) == True)
print(is_leap_year(1753) == False)
print(is_leap_year(1800) == False)
print(is_leap_year(1900) == False)
print(is_leap_year(2000) == True)
print(is_leap_year(2023) == False)
print(is_leap_year(2024) == True)
print(is_leap_year(2025) == False)

""" 
To involve the countries
1. Create a constant dictionary where the countries are keys and the year they adopted gregorian calendar are values.
2. In the function is_leap_year, 
    1. instead of "if year < GREGORIAN_START" we'd have
    "if year < GREGORIAN_START.get(country, 1752)" where 1752 would be default value if country is not in the dictionary
    2. country would be passed as the function attribute 
"""