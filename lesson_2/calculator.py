from copy import copy
import json
import sys

PROMPTS_FILENAME = 'calculator_prompts.json'

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False

# Allow user to select the language
prompt('Select language. Enter en for English or fr for French')
lang_entered = input()

while lang_entered not in ['en', 'fr']:
    prompt('Incorrect language. Enter en or fr')

LANG = copy(lang_entered)

# Load the prompt messages from config file in chosen language
# Validations
# 1) if there is no file, print explanation and exit
# 2) if the file does not cover all the message scenarios,
# print explanation and exit
try:
    with open(PROMPTS_FILENAME, 'r') as f:
        PROMPTS = json.load(f)[LANG]
except FileNotFoundError:
    print('Prompts configuration file missing. Exiting.')
    sys.exit()
except KeyError:
    print('Language not supported. Exiting.')
    sys.exit()

# Check if all necessary messages were loaded
# For each message that we need, check if it's inside the loaded config
message_types = [
    'welcome',
    'number1',
    'number2',
    'invalid_number',
    'operation',
    'invalid_operation',
    'again',
    ]

if any ([x not in PROMPTS for x in message_types]):
    print('Prompt messages missing in config file. Exiting.')
    sys.exit()

# Start calculator program
prompt(PROMPTS['welcome'])

while True:
    # Ask the user for the 1st number
    prompt(PROMPTS['number1'])
    number1 = input()

    while invalid_number(number1):
        prompt(PROMPTS['invalid_number'])
        number1 = input()

    # Ask the user for the 2nd number
    prompt(PROMPTS['number2'])
    number2 = input()

    # pdb.set_trace()

    while invalid_number(number2):
        prompt(PROMPTS['invalid_number'])
        number2 = input()

    # print(f'Number 1: {number1}\nNumber 2: {number2}')

    prompt(PROMPTS['operation'])
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt(PROMPTS['invalid_operation'])
        operation = input()

    number1 = float(number1)
    number2 = float(number2)

    match operation:
        case '1':
            result = number1 + number2
        case '2':
            result = number1 - number2
        case '3':
            result = number1 * number2
        case '4':
            result = number1 / number2

    prompt(f'The results is {result:.2f}')

    prompt(PROMPTS['again'])
    again_reply = input()

    if again_reply.lower() not in ['yes', 'oui']:
        break