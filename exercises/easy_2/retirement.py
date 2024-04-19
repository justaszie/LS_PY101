"""
Inputs
    - current age (user input)
    - age of retirement (user input)

Output: printed message including the calculated values:
    - current year
    - year of retirement 
    - number of years left until retirement

Requirements:
    - Validate that both inputs are positive integers
    - Validate that retirement age > current age
    - Calculate current year 
    - Calculate year of retirement 
    - calculation for retirement = retirement age - current age
    - Format of the ouptut message: 
    "It's {current year}. You will retire in {retirmenet year}.
    You have only {years left} years of work to go!" 

Example: 
What is your age? 30
At what age would you like to retire? 70

It's 2024. You will retire in 2064.
You have only 40 years of work to go!

Data structures
- strings to capture user's inputs
- integers for all other values: current age, 
retirmeent age, current year, retirement year, years left

Algorithm:
1. START
2. ask the user to input their age
3. validate 




Alternative:
1. START
2. get valid current age 
3. get valid retirement age (must be > current age)
4. calculate years left 
5. calculate current year
6. calculate year of retirement 
7. display the message with the data 
8. END 

-- get valit curent age--:
1. START
2. Ask user to input age
3. if (input age is a valid age) : return  integer value of input aged
    else: 
        print error message 
        go to step 2. 

-- get valid retirement age -- 
1. START
2. ask user to input age 
3. if (input age is valid age) and (integer value of input age) > current age
    return integer value of input age 
    else:
        print error message
        go to step 2

-- input age is valid age --
1. The input age string can be converted to an integer value
2. The converted value is greater than 0 

"""
from datetime import datetime

def is_valid_age(user_input):
    try:
        return int(user_input) > 0
    except ValueError:
        return False


def get_age(prompt_message, minimum_age = 0):
    user_input = input(prompt_message)

# NOTE -  I could also do while True: keep asking for input that is valid (I can use branching basd on minimum age param) and break out of the loop once valid entry is provided
    while not is_valid_age(user_input) or int(user_input) < minimum_age:
        print("Hmm. That doesn't look right. It must be a positive number")
        user_input = input(prompt_message)

    return int(user_input)


current_age = get_age('What is your age? ')
retirement_age = get_age('At what age would you like to retire? ',
                         minimum_age=current_age + 1)

years_to_retirement = retirement_age - current_age

current_year = datetime.now().year
retirement_year = current_year + years_to_retirement

print()

output_message = (f"It's {current_year}. You will retire in {retirement_year}.\n"
                  + f"You have only {years_to_retirement} years of work to go!")
print(output_message)