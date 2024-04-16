"""
PEDAC

Inputs:
    - length of the room: user input
    - width of the room: user input
Outputs: 
    - printed room's area in (1) square meters and (2) square feet

Rules:
    - User inputs length and width in METERS
    Output units:
        - We can immediately calculate the area in square meters. 
        - But we will need to convert it to square feet. 
        - 1 square meter = 10.76391042 square feet
        - output in sqft will be rounded to 2 decimals
    - We need to validate user's input for both length and width. 
        - User is free to enter integer or float values. 
        So we should consider it as float either way
        - If user inputs an invalid value, we should keep on asking. 
        Invalid value is negative or 0

Examples / Test Cases:
    Example 1:
        Inputs: length = 12, width = 11.5
        Outputs: 
            * 138 sqm
            * 1485.42 sqft
    Example 2:
        Inputs: length = 0, width = 11.2
        Outputs: user is asked to enter length again. 

        
Algorithm:
    1. Ask user for length in meters
    2. Validate length
    3. If length is invalid
        go to step 1 
       else continue
    4. Ask user for width in meters
    5. Validate width
    6. If width is invalid
            go to step 4
        else continue
    7. calculate area in sqm 
    8. calculate area in sqft by converting sqm value
    9. round up the sqft area to 2 decimal digits
    10. print the area in both units

Further exploration: 

# Ask to choose meters or feet (1 for meters, 2 for feet)
# Validate the input
# Validate the length as before
# Branching logic to calculate and convert the area based on chosen units
"""

# Further Exploration
def is_valid_number(number):
    try:
        value = float(number)
        return value > 0
    except ValueError:
        return False


unit = input('Which units to use? Enter 1 for meters, 2 for feet: ')
while unit not in ['1', '2']:
    unit = input('Choice must be 1 or 2. Try again: ')

length = input('Enter room length: ')

while not is_valid_number(length):
    length = input('Invalid length. Try again: ')

width = input('Enter room width: ')

while not is_valid_number(width):
    width = input('Invalid width. Try again: ')

if unit == '1':
    area_sqm = float(length) * float(width)
    area_sqft = area_sqm * 10.76391042
    print(f'Room area is: {area_sqm:.2f} m2 ({area_sqft:.2f} ft2)')
else:
    area_sqft = float(length) * float(width)
    area_sqm = area_sqft / 10.76391042
    print(f'Room area is: {area_sqft:.2f} ft2 ({area_sqm:.2f} m2)')