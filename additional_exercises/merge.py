"""
Develop a function that merges two dictionaries. 
If the same key exists in both, sum the values if they are integers or concatenate them if they are strings. 
Test your function with examples.

Input: 2 dictionaries
Output: dictionary which is the result of merge of the 2 input dictionaries

Implicit Requirements:
    - Empty dictionary(-ies): 
        if 1 is empty, the output will be the other one. 
        If both are empty, the result will be empty dict
    - If the same key exists in both, sum the values if they are integers or concatenate them if they are strings. 
    - If a key is only present in one of the dicts, add that key and its value to the result dictionary
    - Only string, list, integer and float values are accepted for values. Otherwise, raise exception

Algorithm:
1. Set result to empty dict 
2. Iterate through the key-value pairs of the first dictionary. For each key:
    If the value is not within accepted types, raise exception.
    Else, continue
    If the key is present in the dict2, set result dictionary value for the current key to [value1 + value2]
    Else: set result dictionary value for the current key as [value]
3. Iterate through the key-value paris of the 2nd dictionary. For each key:
    If the key is not already in the result dictionary:
        If the key value is not within accepted types, raise exception.
        Else, set result dictionary value for the current key as [value]
"""

def is_valid_value_type(value):
    return isinstance(value, (list, str, int, float, set))

def merge_dicts(dict1, dict2):
    result = {}
    for key, value in dict1.items():
        if not is_valid_value_type(value):
            raise TypeError(f"dictionary1[{key}]={value} - which can't be concatenated")
        
        if key in dict2:
            result[key] = value + dict2[key]
        else:
            result[key] = value

    for key,value in dict2.items():
        if key not in result:
            if not is_valid_value_type(value):
                raise TypeError(f"dictionary1[{key}]={value} - which can't be concatenated")
            
            result[key] = value

    return result


dict1 = {'apple': 10, 'banana': 5, 'cherry': 'red'}
dict2 = {'apple': 3, 'banana': 2, 'cherry': ' and yellow'}

# print(merge_dicts(dict1, dict2))

# Expected output: {'apple': 13, 'banana': 7, 'cherry': 'red and yellow'}

dict3 = {'apple': 10, 'banana': 5}
dict4 = {'orange': 7, 'apple': 3, 'grapes': 'green'}

# print(merge_dicts(dict3, dict4))

# Expected output: {'apple': 10, 'banana': 5, 'orange': 7, 'grapes': 'green'}

dict5 = {'apple': 10, 'orange': 'big'}
dict6 = {'apple': ' apples', 'orange': 2}

# print(merge_dicts(dict5, dict6))

# Expected output: This case requires decision on handling mismatched types:
# Possible output (if concatenating strings with integers is allowed):
# {'apple': '10 apples', 'orange': 'big2'}
# Or consider raising an error or skipping the merge for mismatched types.

dict7 = {'apple': 10, 'details': {'color': 'red', 'size': 'medium'}}
dict8 = {'apple': 5, 'details': {'origin': 'USA', 'type': 'Fuji'}}

# Expected output: Depends on whether the function handles nested dictionary merging:
# Possible output if merging recursively:
# {'apple': 15, 'details': {'color': 'red', 'size': 'medium', 'origin': 'USA', 'type': 'Fuji'}}
# Or consider raising an error or not merging nested dictionaries.

# print(merge_dicts(dict7, dict8))

dict9 = {'apple': [1, 2, 3], 'banana': [4, 5]}
dict10 = {'apple': [4, 5], 'banana': [6, 7]}

# Expected output: {'apple': [1, 2, 3, 4, 5], 'banana': [4, 5, 6, 7]}
print(merge_dicts(dict9, dict10))
