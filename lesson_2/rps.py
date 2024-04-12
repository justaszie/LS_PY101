# My RPS version before walkthrough
import random
import os

MOVES = {
    'sp': 'spock',
    'sc': 'scissors',
    'r': 'rock',
    'p': 'paper',
    'l': 'lizard'
}

VALID_SELECTIONS = ', '.join([f'"{shortcut}" for {move}'
                        for shortcut, move in MOVES.items()])

WINNING_OUTCOMES = {
    'lizard': ['paper', 'spock'],
    'rock': ['lizard', 'scissors'],
    'paper': ['rock', 'spock'],
    'scissors': ['lizard', 'paper'],
    'spock': ['rock', 'scissors'],
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


def display_round_summary(user_sel, computer_sel):
    prompt(f'User: {user_sel.capitalize()} |'
           f' Computer: {computer_sel.capitalize()}')


def calculate_round_result(user_sel, computer_sel):
    # result code 0 means tie, 1 means user win, 2 means computer win
    if user_sel == computer_sel:
        return 0

    return 1 if computer_sel in WINNING_OUTCOMES[user_sel] else 2


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

    while user_score < WINS_LIMIT and computer_score < WINS_LIMIT:
        user_selection = get_user_selection()
        computer_selection = get_computer_selection()

        display_round_summary(user_selection, computer_selection)

        result = calculate_round_result(user_selection, computer_selection)

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