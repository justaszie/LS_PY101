"""
Input: positive integer N
Output: printed right triangle of height N

Example: 
triangle(5)

    *
   **
  ***
 ****
*****

Algorithm:
START
Draw N lines. For each line:
    - Draw K spaces. Where K = N - iterator 
    - Draw [iterator] times asterisk (*)
END
"""

def triangle(height):
    for i in range(1, height + 1):
        line = ' ' * (height - i) + '*' * i
        print(line)

triangle(9)