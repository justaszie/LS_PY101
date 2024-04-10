"""
SET keep_going = True
WHILE keep_going:
	# do the usual steps: get numbers, operator, display
	GET again
	IF again == False:
		SET keep_going = False
STOP
"""

# import pdb

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True
    return False

# Ask user to select the operation: add, subtract, multiple or divide
# Ask user the 1st operand
# Ask user the 2nd operand
# Print out the result

prompt('Welcome to the calculator!')

while True:
    # Ask the user for the 1st number
    prompt("What's the first number?")
    number1 = input()

    while invalid_number(number1):
        prompt("Hmm... that doesn't look like a valid number. Try again.")
        number1 = input()

    # Ask the user for the 2nd number
    prompt("What's the second number?")
    number2 = input()

    # pdb.set_trace()

    while invalid_number(number2):
        prompt("Hmm... that doesn't look like a valid number. Try again.")
        number2 = input()

    # print(f'Number 1: {number1}\nNumber 2: {number2}')

    prompt("""What operation should we do?
    1) Add 2) Subtract 3) Multiply 4) Divide""")
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt("You must enter 1, 2, 3 or 4")
        operation = input()

    number1 = int(number1)
    number2 = int(number2)

    match operation:
        case '1':
            result = number1 + number2
        case '2':
            result = number1 - number2
        case '3':
            result = number1 * number2
        case '4':
            result = number1 / number2

    prompt(f'The result is: {result}')

    prompt('Should we do another calculation? enter Yes to start again.')
    again_reply = input()

    if again_reply.lower() != 'yes':
        break