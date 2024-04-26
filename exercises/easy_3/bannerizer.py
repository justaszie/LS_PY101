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


FURTHER EXPLORATION:
 
[V1] - Truncate the message if it does not fit within N characters, 
    where N = max width - 4 (| on both sides)
[V2] - For a challenging but fun exercise, try word wrapping messages that are too long to fit, so that they appear on multiple lines but are still contained within the box. This isn't an easy problem, but it's doable with basic Python.
    If text longer than max width - 4: 
        1. cut the message in x parts. X = text length / max characters per line roudned up to the next integer. 
            Maybe iterate over slices of max until no slices left. 
            [0: 9]
            [10, 19]... 
            while index is inside the range [iterator * max_width + max_width - 1]
        2. Iterate over the lines and print a line of text with padding for each line
        3. Last line should be center-justified (padded equally on both sides)


"""
""" Further Exploration - V1
def draw_border(text_length):
    # It would  probably be more readable to add a symbol to + and multiply the - symbol N times.
    line = '+' + ('-' * (text_length + 2)) + '+'
    print(line)


def draw_padding_line(text_length):
    line = '|' + (' ' * (text_length + 2)) + '|'
    print(line)


def print_in_box(text_line, max_width = None):
    text_length = len(text_line)

    # 2 characters reserved for box on each side
    if max_width:
        max_text_length = max_width - 4
        if text_length > max_text_length:
            text_line = text_line[0:max_text_length]
            text_length = len(text_line)

    draw_border(text_length)
    draw_padding_line(text_length)

    print('| ' + text_line.strip() + ' |')

    draw_padding_line(text_length)
    draw_border(text_length)


print_in_box('To boldly go where no one has gone before.', 20)
print_in_box('')
 """

""" FURTHER EXPLORATION - V2 """
import math 

def draw_border(text_length):
    # It would  probably be more readable to add a symbol to + and multiply the - symbol N times.
    line = '+' + ('-' * (text_length + 2)) + '+'
    print(line)


def draw_padding_line(text_length):
    line = '|' + (' ' * (text_length + 2)) + '|'
    print(line)

def print_text_line(text):
    line = '| ' + text + ' |'
    print(line)

def print_in_box(text, max_width = None):
    text = text.strip()

    text_length = len(text)
    text_lines_count = 1
    max_text_length = text_length

    # 2 characters reserved for box on each side
    if max_width and max_width - 4 < text_length:
        max_text_length = max_width - 4
        # Calculate Number of lines to print
        text_lines_count =  math.ceil(text_length / max_text_length)
        
    # Cut the string into lines of max_text_length:
    draw_border(max_text_length)
    draw_padding_line(max_text_length)
    for i in range(text_lines_count):
        line_start = i * max_text_length
        line_end = line_start + max_text_length

        text_line = text[line_start:line_end]
        
        # The last line may need to be padded if it's shorter than a normal line 
        if i == text_lines_count - 1:
            text_line = text_line.ljust(max_text_length)
        print_text_line(text_line)


    draw_padding_line(max_text_length)
    draw_border(max_text_length)


print_in_box('To boldly go where no one has gone before.', 50)
# print_in_box('')