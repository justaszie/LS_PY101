import json
import sys
import os

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False


# Allow user to select the language
def get_language():
    prompt('Select language. Enter en for English or fr for French')
    lang_entered = input()

    while lang_entered.lower().strip() not in SUPPORTED_LANGUAGES:
        prompt(f'Incorrect language. '
               f'Enter one of the following : {SUPPORTED_LANGUAGES}')
        lang_entered = input()

    return lang_entered.lower().strip()


def get_confirmation_text(language):
    match language:
        case 'en':
            return 'yes'
        case 'fr':
            return 'oui'


def load_prompts(config_filename, language):
    # Load the prompt messages from config file in chosen language
    # Validations
    # 1) if there is no file, print explanation and exit
    # 2) if the file does not cover all the message scenarios,
    # print explanation and exit
    try:
        with open(config_filename, 'r') as f:
            return json.load(f)[language]
    except FileNotFoundError:
        print('Prompts configuration file missing. Exiting.')
        sys.exit()
    except KeyError:
        print('Language not supported. Exiting.')
        sys.exit()
    except json.decoder.JSONDecodeError:
        print('Something is wrong with configuration file. Exiting')
        sys.exit()

# Get a number from user and validate it
def get_number(prompt_message):
    prompt(prompt_message)
    number = input()

    while invalid_number(number):
        prompt(PROMPTS['invalid_number'])
        number = input()

    return float(number)


def get_operation():
    prompt(PROMPTS['operation'])
    operation_code = input()

    while operation_code not in ['1', '2', '3', '4']:
        prompt(PROMPTS['invalid_operation'])
        operation_code = input()

    return operation_code


def calculate_result(num1, num2, operation_code):
    match operation_code:
        case '1':
            return num1 + num2
        case '2':
            return num1 - num2
        case '3':
            return num1 * num2
        case '4':
            try:
                return num1 / num2
            except ZeroDivisionError:
                return 0


def display_result(num1, num2, operation_code, result_value):
    match operation_code:
        case '1':
            summary = f'{num1} + {num2} = {result_value:.2f}'
        case '2':
            summary = f'{num1} - {num2} = {result_value:.2f}'
        case '3':
            summary = f'{num1} * {num2} = {result_value:.2f}'
        case '4':
            summary = f'{num1} / {num2} = {result_value:.2f}'
    prompt(f'{PROMPTS['result']} {summary}')


def clear_screen():
    # If it's a windows OS
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def display_welcome_message():
    prompt(PROMPTS['welcome'])


def display_goodbye_message():
    prompt(PROMPTS['goodbye'])

def calculate_again():
    prompt(PROMPTS['again'])
    reply = input().lower().strip()
    return reply == AGAIN_CONFIRMATION

# Hardcoded configuration values
PROMPTS_FILENAME = 'calculator_prompts.json'
SUPPORTED_LANGUAGES = {'en', 'fr'}
MESSAGE_TYPES = [
    'welcome',
    'number1',
    'number2',
    'invalid_number',
    'operation',
    'invalid_operation',
    'again',
    'result',
    'goodbye',
    ]

# Calculated constants
LANG = get_language()
PROMPTS = load_prompts(PROMPTS_FILENAME, LANG)
AGAIN_CONFIRMATION = get_confirmation_text(LANG)

# Check if all necessary messages were loaded
# For each message that we need, check if it's inside the loaded config
if any ([message_type not in PROMPTS for message_type in MESSAGE_TYPES]):
    print('Prompt messages missing in config file. Exiting.')
    sys.exit()

# Start calculator program
display_welcome_message()

while True:
    number1 = get_number(PROMPTS['number1'])
    number2 = get_number(PROMPTS['number2'])
    operation = get_operation()
    result = calculate_result(number1, number2, operation)
    display_result(number1, number2, operation, result)

    # Asking user if they want to calculate again
    if not calculate_again():
        display_goodbye_message()
        break

    clear_screen()