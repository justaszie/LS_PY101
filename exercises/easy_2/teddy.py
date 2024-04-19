"""
Inputs: No inputs
Outputs: printed message including a randomly generated age

Requirements:
    - Age must be randomly generated between 20 and 100 inclusive

Example: 
Teddy is 69 years old!

Algorithm
1. START
2. Generated age
3. Print the message with name 
4. STOP

---- FURTHER EXPLORATION----

Input: name 
Output : message with user's entered name and random generated age. 
Requirement:
    - If no name entered, use 'Teddy' by default 

Algorithm:
1. START
2. Get user's name 
3. If name is null: name = 'Teddy'
    else name = user's input 
4. randomly generate age between 20 and 100 
5. Print formattted message with name and age 
6. STOP
"""
import random

def generate_age():
    # return random.choice(range(20, 101)) # better method randint
    return random.randint(20, 100)


def get_name():
    user_input = input('Enter a name: ')
    return user_input


name = get_name()
if not name:
    name = 'Teddy'

age = generate_age()

print(f'{name} is {age} years old!')