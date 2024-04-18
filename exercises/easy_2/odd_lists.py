"""
Input: list of elements of any type
Ouput: return every other element of the list (indexes: 0, 2, ...)

Requirements: 
- Use list slicing to solve the problem 
- Empty list input should return empty list

"""

def oddities(list_argument):
    return list_argument[::2]

def evenities(list_argument):
    result_list = []
    for index in range(1,len(list_argument), 2):
        result_list.append(list_argument[index])

    return result_list

# print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
# print(oddities([1, 2, 3, 4]) == [1, 3])        # True
# print(oddities(["abc", "def"]) == ['abc'])     # True
# print(oddities([123]) == [123])                # True
# print(oddities([]) == [])                      # True

print(evenities([2, 3, 4, 5, 6]) == [3, 5])  # True
print(evenities([1, 2, 3, 4]) == [2, 4])        # True
print(evenities(["abc", "def"]) == ['def'])     # True
print(not evenities([123]))                # True
print(evenities([]) == [])                      # True

print(evenities([2, 3, 4, 5, 6]))
print(evenities(["abc", "def"]))