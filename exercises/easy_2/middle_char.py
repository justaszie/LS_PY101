"""
Input: a string of text
Output: Middle character(s)

Requirements:
- If the string length is even
    return 2 middle characters
  else:
    return 1 middle character

Examples:
'abcd' => 'bc'. Length 4 => chars 4/2 - 1 , 4/2  
'abc' => 'b' Legnth 3 => chars 3/2

'abcde' . 

Algortihm:
START
middle_index = length / 2
if string length % 2 == 0: return string[middle_index]
else return string string[middle_index - 1:middle_index + 1]

"""

def center_of(text):
    str_len = len(text)
    middle_index = str_len // 2
    return text[middle_index - 1:middle_index+1] if str_len % 2 == 0 \
            else text[middle_index]

print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True