def is_valid_number(number):
    try:
        return int(number) > 0
    except ValueError:
        return False

def calculate_sum(last_num):
    return sum(range(1, last_num + 1))

def calculate_product(last_num):
    product_result = 1

    for num in range(1, last_num + 1):
        product_result *= num

    return product_result

last_number = input('Please enter an integer greater than 0: ')

while not is_valid_number(last_number):
    last_number = input('Invalid number. Must be an integer > 0. Try again: ')

last_number = int(last_number)

operation_code = input('Enter "s" to compute the sum, '
                       'or "p" to compute the product: ')

while (not operation_code) or (operation_code[0].lower() not in ['s','p']):
    operation_code = input('Invalid code. Please type "s" or "p": ')

match operation_code:
    case 's':
        operation_name = 'sum'
        result = calculate_sum(last_number)
    case 'p':
        operation_name = 'product'
        result = calculate_product(last_number)

print(f'The {operation_name} of the integers '
      f'between 1 and {last_number} is {result}.')


    