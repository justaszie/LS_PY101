import random
import os

# Possible moves with their shortcuts
MOVES = {
    'sp': 'spock',
    'sc': 'scissors',
    'r': 'rock',
    'p': 'paper',
    'l': 'lizard'
}

# Player 1 Selection, mapped to the moves against which the selection wins
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


def display_welcome_message():
    prompt('Welcome to Rock, Paper, Scissors, Lizard, Spock!')
    prompt('You are plaing against the computer. '
           f'First one to win {WINS_LIMIT} rounds is the grand winner\n')


def display_rules():
    prompt("The winner of the round is determined using these rules:")
    print("""Scissors cuts Paper
Paper covers Rock
Rock crushes Lizard
Lizard poisons Spock
Spock smashes Scissors
Scissors decapitates Lizard
Lizard eats Paper
Paper disproves Spock
Spock vaporizes Rock
Rock crushes Scissors\n""")


def get_user_selection(first_round = False):
    if first_round:
        selections = valid_selections(include_help = True)
    else:
        selections = valid_selections()

    prompt(f'Select your item: {selections}')
    selection = input().lower().strip()
    while selection not in MOVES and selection not in MOVES.values():
        if selection == 'help':
            display_rules()
            prompt(f'Select your item: {selections}')
        else:
            prompt(f'Invalid selection. '
                f'Choose one: {selections}')
        selection = input().lower().strip()

    # Depending on user input (shortcut or full name) we fetch the full name
    return selection if selection in MOVES.values() else MOVES[selection]


def get_computer_selection():
    return random.choice(list(MOVES.values()))


def display_round_summary(user_sel, computer_sel):
    prompt(f'User: {user_sel.capitalize()} | '
           f'Computer: {computer_sel.capitalize()}')


def calculate_round_result(user_move, computer_move):
    # result code 0 means tie, 1 means user win, 2 means computer win
    if user_move == computer_move:
        return 0

    return 1 if computer_move in WINNING_OUTCOMES[user_move] else 2


# Calculate result and display outcome message
def display_round_result(round_result):
    prompt(ROUND_OUTCOME_MESSAGES[round_result] + '\n')


# Update scoreboard after the round
def update_scoreboard(scores, result_code):
    if result_code == 1:
        scores['user'] += 1
    elif result_code == 2:
        scores['computer'] += 1
    # no change to scoreboard in case of a tie (result = 0)


def display_current_scores(scores):
    prompt(f'User Score: {scores['user']} | '
           f'Computer Score: {scores['computer']}\n')


def display_grand_winner(scores):
    if scores['user'] > scores['computer']:
        prompt(f'You are the grand winner '
               f'{scores['user']} - {scores['computer']}. Great Job!\n')

    else:
        prompt(f'Computer is the grand winner '
               f'{scores['computer']} - {scores['user']}. Sorry!\n')


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


def valid_selections(include_help = False):
    selections =  ', '.join([f'"{shortcut}" for {move}'
                        for shortcut, move in MOVES.items()])
    if include_help:
        selections += '\n(type "help" to see the rules)'

    return selections


def play_rps():
    while True:
        rounds_played = 0

        scoreboard = {
            'user': 0,
            'computer': 0,
        }

        while (scoreboard['user'] < WINS_LIMIT
               and scoreboard['computer'] < WINS_LIMIT):

            user_selection = get_user_selection(rounds_played == 0)
            computer_selection = get_computer_selection()

            result = calculate_round_result(user_selection, computer_selection)

            clear_screen()

            update_scoreboard(scoreboard, result)

            display_current_scores(scoreboard)

            display_round_summary(user_selection, computer_selection)

            display_round_result(result)

            rounds_played += 1

        display_grand_winner(scoreboard)

        if not play_again():
            prompt('Goodbye!')
            break

        clear_screen()

display_welcome_message()

play_rps()