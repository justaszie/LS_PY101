"""
Write a function that returns the number provided as an argument multiplied by two, 
unless the argument is a double number. 
 If the argument is a double number, return the double number as-is

PROBLEM
    - Input: A number
    - Output: A number. Same as input if it's double. If not double, input multiplied by 2

Algorithm:
Start
1. If the input is not a positive int, print error message
2. Check if the input number is double 
3. If the number is double, return it 
    else, return calculated input number * 2
End

Step 2 - Check if the input number is double. 
Requirements for double: 
    - Check the number of digits
    - Split characters to left and right
    - Compare the charac

1. Convert to string
2. Check the number of characters.
3.  If the number of characters is even:
        Split string to left and right (e.g. 4 chars, string[0:1] and string[2:3]. string[0:len/2-1]; string[len/2: len])
        Check if left == right.
        If yes, return True 
        else, return False
    else, return False


    If the number of digits



"""

def is_double(number):
    number_str = str(number)
    str_len = len(number_str)

    if str_len % 2 == 0:
        left = number_str[:str_len // 2]
        right = number_str[str_len // 2:]
        return left == right
    else:
        return False


def twice(number):
    if not isinstance(number, int):
        print('The input should be a number')
        return None

    if is_double(number):
        result = number
    else:
        result = number * 2
    
    return result


print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True