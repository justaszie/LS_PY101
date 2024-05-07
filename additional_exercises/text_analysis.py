"""
 Write a function to find the most commonly occurring word that starts with a vowel in a large text. The function should ignore case and punctuation. Explain your approach.

 Input: string of text
 Output: The word that is most frequent in the text among the words that start with a vowel

 Requirements:
    - Vowels: a, e, i, o, u, y
    - Counting frequency should be case insensitive. Word appearing in different case should count as occurence
    - Words are separated by one of the following: space, punctuation (.,;:!?)
    - If multiple words have the same frequency, one will be chosen randomly. 

Examples:
Input: 
"Hello World! Welcome to OpenAI's playground. Here, you can explore AI, machine learning, and more. Don't forget: success is 90% hard work and 10% inspiration. Keep striving!"

Output: 
And (frequency = 2 )


Data structures:
- String for input
- List of elligible words 
- Dictionary for words and their frequencies 


Algorithm:
1. Get the list of words from the text
2. Filter the words to only keep the ones that start with a vowel
3. Count occurence of each word.
4. Find the most frequent word and return it with its frequency 

Detailed logic:
Step 1: (Input text)
    1. set current word to empty string
    2. Iterate over each character in the text. For each character:
        - If it's a letter or apostrophe or hyphen or underscore (for technical text):
            - add letter to the current word 
        - If it's not a letter OR if it's a letter but last character:
            - add current word to the list of words, in lower case
            - set current word to '' 
    3. Return the list of words 
 
Step 2: (Input list of words)
    1. Set result list to empty list
    2. Iterate over the list of words in input. For each word:
        - If the word starts with a vowel, add it to result list 
    3. Return the result list 
 
 
 Step 3: (Input list of words)
    1. Create a result dictionary of frequencies
    2. Create a set of unique words from the list
    3. Iterate over each word. For each word
        - Calculate the frequency in the input list
        - Store the word and its frequency in the result dictionary 
    4. Return the result dictionary 

Step 4: (Input dictionary of frequencies)
    1. Create a list of tuples where element 1 = the key of the input dictionary and element 2 = the frequency
    2. Sort the list of tuples using the 2nd element of the tuple in descending order
    3. Return the 1st element of the list of tuples 
 """

def get_words(text):
    words = []
    current_word = ''
    for idx, char in enumerate(text):
        # If not a letter or apostrophe(considered part of word) 
        # or it's the last character in the text, we end the word
        if not char.isalpha() and not char in ["'", "-","_"] or idx == len(text) - 1: 
            if current_word != '':
                words.append(current_word.lower())
            current_word = ''
        else:
            current_word += char
        
    return words

def filter_vowel_words(words_list):
    filtered_words = []
    # str.startswith method can use a tuple of substrings
    vowels = ('a', 'e', 'i', 'o', 'u', 'y')

    for word in words_list:
        if word.startswith(vowels):
            filtered_words.append(word)

    return filtered_words

def get_word_frequencies(words_list):
    counts = {}
    unique_words = set(words_list)

    for word in unique_words:
        count = words_list.count(word)
        counts[word] = count
            
    return counts

def get_most_frequent_word(frequencies):
    result = max(frequencies.items(), key=lambda x: x[1])
    # frequency_tuples = list(frequencies.items())
    # frequency_tuples.sort(key=lambda x: x[1], reverse=True)
    return result


text = "Hello World! Welcome to OpenAI's playground. Here, you can explore AI, machine learning, and more. Don't forget: success is 90% hard work and 10% inspiration. Keep striving!"

words = get_words(text)

words = filter_vowel_words(words)

word_counts = get_word_frequencies(words)

(word, frequency) = get_most_frequent_word(word_counts)
print(f'Most frequent word: "{word}" (mentioned {frequency} times)')
