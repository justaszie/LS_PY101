# My RPS version before walkthrough
import random
import os

MOVES={
    'sp': 'spock',
    'sc': 'scissors',
    'r': 'rock',
    'p': 'paper',
    'l': 'lizard'
}

VALID_SELECTIONS = ', '.join([f'"{shortcut}" for {move}'
                        for shortcut, move in MOVES.items()])

# Game rules: mapping the players' selections to the outcomes.
# Logic: Rock > Scissors, Paper > Rock, Scissors > Paper; Same selection = tie
# 1 - Player 1 wins, 2 - player 2 wins
OUTCOMES = {
    ('lizard', 'rock'): 2,
    ('lizard', 'paper'): 1,
    ('lizard', 'scissors'): 2,
    ('lizard', 'spock'): 1,
    ('rock', 'lizard'): 1,
    ('rock', 'paper'): 2,
    ('rock', 'scissors'): 1,
    ('rock', 'spock'): 2,
    ('paper', 'lizard'): 2,
    ('paper', 'rock'): 1,
    ('paper', 'scissors'): 2,
    ('paper', 'spock'): 1,
    ('scissors', 'lizard'): 1,
    ('scissors', 'rock'): 2,
    ('scissors', 'paper'): 1,
    ('scissors', 'spock'): 2,
    ('spock', 'lizard'): 2,
    ('spock', 'rock'): 1,
    ('spock', 'paper'): 2,
    ('spock', 'scissors'): 1,
}

# Here we can adjust how we display the outcome of the game
ROUND_OUTCOME_MESSAGES = {
    0: "It's a tie!",
    1: "You win this round. Congrats!",
    2: "Computer wins this round. Sorry!",
}

WINS_LIMIT = 3

def prompt(message):
    print(f'==> {message}')

def get_user_selection():
    prompt(f'Select your item: {VALID_SELECTIONS}')
    selection = input().lower().strip()
    while selection not in MOVES:
        prompt(f'Invalid selection. '
               f'Choose one: {VALID_SELECTIONS}')
        selection = input().lower().strip()

    return MOVES[selection]


def get_computer_selection():
    return random.choice(list(MOVES.values()))


def display_round_summary(user_sel, cpu_sel):
    prompt(f'User: {user_sel.capitalize()} | Computer: {cpu_sel.capitalize()}')


def calculate_round_result(user_sel, cpu_sel):
    return (0 if user_sel == cpu_sel
            else OUTCOMES[(user_sel, computer_selection)])

# Calculate result and display outcome message
def display_round_result(round_result):
    prompt(ROUND_OUTCOME_MESSAGES[round_result])

def display_current_scores(user, computer):
    prompt(f'User Score: {user} | Computer Score: {computer}')

def display_grand_winner(user, computer):
    if user > computer:
        prompt(f'You are the grand winner {user} - {computer}.'
               ' Great Job!')
    else:
        prompt(f'Computer is the grand winner {computer} - {user}.'
               ' Sorry!')

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
    user_score = 0
    computer_score = 0

    while user_score < 3 and computer_score < 3:
        user_selection = get_user_selection()
        computer_selection = get_computer_selection()
        
        result = calculate_round_result(user_selection, computer_selection)
        
        display_round_summary(user_selection, computer_selection)
        display_round_result(result)

        if result == 1:
            user_score += 1
        elif result == 2:
            computer_score += 1

        display_current_scores(user_score, computer_score)

    display_grand_winner(user_score, computer_score)

    if not play_again():
        prompt('Goodbye!')
        break

    clear_screen()