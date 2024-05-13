"""
Create a simple madlib program that prompts for a noun, a verb, an adverb, and an adjective, and injects them into a story that you create

PROBLEM 
Input (user inputs):
    - noun
    - verb
    - adverb
    - adjective.

Output:
    - Story text. It includes:
        - a template with placeholders for input words
        - words from user input

Requirements:
    - Nothing specific

Alogirthm:
START
1. Get user's inputs:
    - noun
    - verb
    - adjective
    - adverb
3. Create a string with template and user's inputs
4. print the created string
STOP

EXAMPLES
Enter a noun: dog
Enter a verb: walk
Enter an adjective: blue
Enter an adverb: quickly

Do you walk your blue dog quickly? That's hilarious!
The blue dog walks quickly over the lazy dog.
The dog quickly walks up to Joe's blue turtle.

"""

def get_noun():
    prompt = 'Enter a noun: '
    return input(prompt)


def get_verb():
    prompt = 'Enter a verb: '
    return input(prompt)


def get_adjective():
    prompt = 'Enter an adjective: '
    return input(prompt)


def get_adverb():
    prompt = 'Enter an adverb: '
    return input(prompt)

noun = get_noun()
verb = get_verb()
adjective = get_adjective()
adverb = get_adverb()


story1 = f"Do you {verb} your {adjective} {noun} {adverb}? That's hilarious!"
story2 = f"The {adjective} {noun} {verb} {adverb} over the lazy {noun}."
story3 = f"The {noun} {adverb} {verb} up to Joe's blue turtle."

print(story1)
print(story2)
print(story3)