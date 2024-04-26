"""
Input: line of text (string)

Output: input printed "inside a box"
Requirements:
    - Box has a size of 5 lines x (length of input + 2 chars on either side)


Examples: 

print_in_box('To boldly go where no one has gone before.')

+--------------------------------------------+
|                                            |
| To boldly go where no one has gone before. |
|                                            |
+--------------------------------------------+

Algorithm:
1. Draw top border of the box
    * + symbol
    * - symbol repeated times N where N = length of text + 2 chars
    * + symbol 
2. Draw empty line bordered by |
    * | symbol 
    * empty spaces N times N where N = length of text + 2 chars
    * | symbol 
3. print the line, bordered by empty space and | on both sides
    * | symbol
    * empty space
    * input line of text 
    * empty space 
    * | symbol 
4. Same as (2)
5. Draw bottom border of the box (same as 1)

"""

def draw_border(text_length):
    line = '+' + ('-' * (text_length + 2)) + '+'
    print(line)


def draw_padding_line(text_length):
    line = '|' + (' ' * (text_length + 2)) + '|'
    print(line)


def print_in_box(text_line):
    text_length = len(text_line)

    draw_border(text_length)
    draw_padding_line(text_length)

    print('| ' + text_line.strip() + ' |')

    draw_padding_line(text_length)
    draw_border(text_length)


print_in_box('To boldly go where no one has gone before.')
print_in_box('')
