""" 
Inputs: 
2 strings

Outputs:
concatenation of shorter string + longer string + shorter string 

Data structure: only strings

Algorithm:
# Given string_1 and string_2
if length of string1 > lenght of string 2:
    return string 2 + string1 + string 2 
else 
    return string 1 + string 2 + string 1
"""

def short_long_short(string_1, string_2):
    if len(string_1) > len(string_2):
        return string_2 + string_1 + string_2
    else:
        return string_1 + string_2 + string_1
    
# These examples should all print True
print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")