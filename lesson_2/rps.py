# My RPS version before walkthrough
import random
import os

VALID_SELECTIONS = ['rock', 'paper', 'scissors']

# Game rules: mapping the players' selections to the outcomes.
# Logic: Rock > Scissors, Paper > Rock, Scissors > Paper; Same selection = tie
# 1 - Player 1 wins, 2 - player 2 wins
OUTCOMES = {
    ('rock', 'paper'):2,
    ('rock', 'scissors'): 1,
    ('paper', 'rock'): 1,
    ('paper', 'scissors'): 2,
    ('scissors', 'rock'): 2,
    ('scissors', 'paper'): 1,
}

# Here we can adjust how we display the outcome of the game
OUTCOME_MESSAGES = {
    0: "It's a tie!",
    1: "You win. Congrats!",
    2: "Computer wins. Sorry!",
}

def prompt(message):
    print(f'==> {message}')

def get_user_selection():
    prompt(f'Select your item: {', '.join(VALID_SELECTIONS)}')
    selection = input().lower().strip()
    while selection not in VALID_SELECTIONS:
        prompt(f'Invalid selection. '
               f'Choose one: {', '.join(VALID_SELECTIONS)}')
        selection = input().lower().strip()

    return selection


def get_computer_selection():
    return random.choice(VALID_SELECTIONS)


def display_summary(user_sel, cpu_sel):
    prompt(f'User: {user_sel} | Computer: {cpu_sel}')

# Calculate result and display outcome message
def display_result(user_sel, cpu_sel):
    result =  (0 if user_sel == cpu_sel
            else OUTCOMES[(user_sel, computer_selection)])

    prompt(OUTCOME_MESSAGES[result])

def play_again():
    prompt('Play again? (y/n)')
    again_reply = input().strip().lower()
    while not (again_reply.startswith('y') or again_reply.startswith('n')):
        prompt('Please enter "y" or "n"')
        again_reply = input().strip().lower()

    return again_reply[0] == 'y'


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

prompt('Welcome to Rock-Paper-Scissors!')

while True:
    user_selection = get_user_selection()
    computer_selection = get_computer_selection()
    display_summary(user_selection, computer_selection)
    display_result(user_selection, computer_selection)

    if not play_again():
        prompt('Goodbye!')
        break

    clear_screen()