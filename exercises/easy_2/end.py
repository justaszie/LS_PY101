"""
Input: input string containing 2 or more words. Words = sequence of non-blank chars, separated by blank spaces
Output: return the next to last word (last - 1) in the sentence

Examples:
# These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")

Data structures: Strings 

Algorithm:
START
1. Split the sentence into a list of words
2. Return the word that is second to last
STOP 

"""

""" FURTHER EXPLORATION 
Suppose we need a function that retrieves the middle word of a phrase/sentence. What edge cases need to be considered? 
=> No words
=> even number of words (if len=4, do we pick word number 2 or 3)
=> 1 word: the word is in the middle 

Algorithm:
1. START
2. if sentence length = 0: return None
3. else: return words[len / 2]

if 1 : first element
if 2: first elemenet = 2 / 2 
if 3: second element = 3 / 2 + 1
if 4: second element = 4 / 2 
if 5: third element = 5 / 2 + 1

if no remainder, use quotient 
if remainder, use quotient + 1 

f 1 :  element 0 
if 2: element 0 = 2 / 2 - 1
if 3: element 1  = 3 / 2 + 1
if 4: element 1 = 4 / 2 
if 5: element 2 = 5 / 2 + 1

if len is odd: index[len / 2]
if len is even: index[len / 2]

[0] [1] [2] [3] [4]
1   2   3   4   5

"""
def middle(sentence):
    if not sentence.split():
        return None
    
    words = sentence.split()
    return words[len(words) // 2]


def penultimate(sentence):
    return sentence.split()[-2]

# These examples should print True
# print(penultimate("last word") == "last")
# print(penultimate("Launch School is great!") == "is")

print(middle("John"))
print(middle("  John is  "))
print(middle("John is 40"))
print(middle("John is 40 yo"))
print(middle("John is 40 yo male"))