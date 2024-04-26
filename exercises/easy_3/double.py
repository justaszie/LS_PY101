"""
Input: string argument
Output: new string that contains the value of the original string consecutive duplicate characters replaced by a single character

Requirements:
    - Assuming no changes to lower / upper case.
    - Empty string is accepted
    - Edge case where we have consecutive characters aA etc. In this case, we'll treat them as separate characters.


Examples: 
# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')

Data structures:
- strings for input and output

Algorithm
Set result list to an empty list # to capture the empty string case
Iterate over characters in indexes 0 to the one before the last character
    - If the next character (current position + 1) is different from the current character: 
     (comparison is case-sensitive)
        Add it to a list 
      else:
        go to next character
    if the lenght of the result list > 0:
        result string = list converted to string 
    else:
        return empty string. 
"""

def crunch(str_value):
    # Note: I used list unnecessarily. We can just append to a string
    # result = []
    result = '' 
    # for i in range(len(str_value)):
    # Another useful way to iterate over a string's charactes is enumerate
    for i, char in enumerate(str_value):
        if i == len(str_value) - 1 or str_value[i] != str_value[i + 1]:
            result += str_value[i]

    # print(result)
    # return ''.join(result)
    return result


print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')
