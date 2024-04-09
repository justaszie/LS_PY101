# Ask user to select the operation: add, subtract, multiple or divide
# Ask user the 1st operand
# Ask user the 2nd operand
# Print out the result

print('Welcome to the calculator!')

# Ask the user for the 1st number
print("What's the first number?")
number1 = input()

# Ask the user for the 2nd number
print("What's the second number?")
number2 = input()

# print(f'Number 1: {number1}\nNumber 2: {number2}')

print('What operation should we do?\n1) Add 2) Subtract 3) Multiply 4)Divide')
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

if result:
    print(f'The result is: {result}')
else:
    print('Wrong selection')