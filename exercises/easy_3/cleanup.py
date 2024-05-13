"""
PROBLEM 
Input: string that has words and some non-alphabetic characters.
Output: input string where non-alphabetic characters are replaced by spaces. 
Rules / Requirements: 
    - when multiple non-alphabetic characters in a row, replace them with 1 space only.
    - Numbers are also considered non-alphabetic

Examples:
clean_up("---what's my +*& line??") => " what s my line ")

Algorithm:
convert string to a list of chars
Iterate through all chars
    If non alphabetic
        If current char is NOT last AND next is also non alphabetic, replace with empty string
        Else, replace the current char with a space
    Else, continue to next char
Create a string out of list


"""
def clean_up(text):
    chars_list = list(text)

    for idx, char in enumerate(chars_list):
        if not char.isalpha():
            # If the character is not last and next character 
            #is also non-alphabetic, we remove the character
            if idx != (len(chars_list) - 1) and not chars_list[idx + 1].isalpha():
                chars_list[idx] = ''
            else:
                chars_list[idx] = ' '

    return ''.join(chars_list)

print(clean_up("---what's my +*& line?") == " what s my line ")
print(clean_up("---what's my +*& line???") == " what s my line ")

""" ALTERNATIVE SOLUTION :
Instead of working with a list, create an empty string result and append that string 
as we go through characters. 
Instead of adding space on the last non-alpha char we add it on the first and check to avoid adding it again
A condition checks if last element in result is space ' ', in that case it does not add extra space

def clean_up(text):
    clean_text = ''

    for idx, char in enumerate(text):
        if char.isalpha():
            clean_text += char
        elif idx == 0 or clean_text[-1] != ' ':
            clean_text += ' '

    return clean_text


"""