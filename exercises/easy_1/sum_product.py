# V1
# def is_valid_number(number):
#     try:
#         return int(number) > 0
#     except ValueError:
#         return False

# def calculate_sum(last_num):
#     return sum(range(1, last_num + 1))

# def calculate_product(last_num):
#     product_result = 1

#     for num in range(1, last_num + 1):
#         product_result *= num

#     return product_result

# last_number = input('Please enter an integer greater than 0: ')

# while not is_valid_number(last_number):
#   last_number = input('Invalid number. Must be an integer > 0. Try again: ')

# last_number = int(last_number)

# operation_code = input('Enter "s" to compute the sum, '
#                        'or "p" to compute the product: ')

# while (not operation_code) or (operation_code[0].lower() not in ['s','p']):
#     operation_code = input('Invalid code. Please type "s" or "p": ')

# match operation_code:
#     case 's':
#         operation_name = 'sum'
#         result = calculate_sum(last_number)
#     case 'p':
#         operation_name = 'product'
#         result = calculate_product(last_number)

# print(f'The {operation_name} of the integers '
#       f'between 1 and {last_number} is {result}.')


# V2 - Further Exploration
def calculate_sum(numbers_list):
    return sum(numbers_list)

def calculate_product(numbers_list):
    product_result = 1

    for num in numbers_list:
        product_result *= num

    return product_result

numbers_list_input = input('Please enter a list of positive integers,'
                           ' separated by a space. For example: "1 2 4 5": ')

numbers_list = numbers_list_input.split()

# The list must contain only integers
while not numbers_list or any([not x.isdigit() or
                              int(x) <= 0 for x in numbers_list
                              ]):
    numbers_list_input = input('Invalid list. Must be only positive integers.'
                               ' Try again: ')
    numbers_list = numbers_list_input.split()

numbers_list = [int(x) for x in numbers_list]

operation_code = input('Enter "s" to compute the sum, '
                       'or "p" to compute the product: ')

while (not operation_code) or (operation_code[0].lower() not in ['s','p']):
    operation_code = input('Invalid code. Please type "s" or "p": ')

match operation_code:
    case 's':
        operation_name = 'sum'
        result = calculate_sum(numbers_list)
    case 'p':
        operation_name = 'product'
        result = calculate_product(numbers_list)

print(f'The {operation_name} of the provided integers is {result}.')
    