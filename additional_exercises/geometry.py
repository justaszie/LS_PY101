"""
Write a set of functions to handle the dimensions of a box (length, width, height) 
and perform operations such as adding dimensions of two boxes and comparing their volumes. 
Assume the dimensions of a box can be represented as a tuple (length, width, height).

Requirements:
- Function to Add Dimensions: Create a function that takes two tuples, each representing the dimensions of a box, 
and returns a new tuple representing the combined dimensions (each dimension is summed).

- Function to Calculate Volume: Develop a function that takes a tuple
 representing the dimensions of a box and returns its volume (calculated as length * width * height).

- Function to Compare Volumes: Write a function that takes two tuples,
 each representing the dimensions of a box, and returns True if the first box has a larger volume than the second, and False otherwise.



---- FUNCTION 1 ---
Problem: 
    - Input: 2 tuples. each tuple represents dimensions of a box. 
    - Output: tuple with sums of dimensions

    - Requirements:
        - Validate that each input tuple has 3 dimensions
        - Validate the data type of the 3 members of both tuples - should be int or float (can be converted to float)
        - Validate that each dimension is positive number
        - Assuming cm unit
        - 

---- FUNCTION 2 ---- 
Problem: 
    - Input: Tuple with dimensions of a box 
    - Output: Return the volume of the box (a * b *c)

    - Requirement: validate dimensions

Algorithm:
- SUBPROCESS Validate the box dimensions
- calculate volume (a * b * c)

---- FUNCTION 3 ----
Problem:
    - Input: 2 tuples, each tuple representing dimensions of a box
    - Output: True if volume(box1) > volume(box2), False otherwise

Algorithm:
- SUBPROCESS validate the dimensions of both boxes
- SUBPROCESS calculate volume of box 1
- SUBPROCESS calculate volume of box 2
- If volume 1 > volume 2: return True
     Else: return False

"""




def is_valid_dimension(dimension):
    if not isinstance(dimension, (int, float)):
        return False
    return dimension > 0
    
def is_valid_box(dimensions_tuple):
    if len(dimensions_tuple) < 3:
        # print('One of the boxes does not have 3 dimensions')
        return False
    
    for dimension in dimensions_tuple:
        if not is_valid_dimension(dimension):
            # print('One of the dimensions has invalid type.')
            return False 
    
    return True

def add_dimensions(box1, box2):
    if is_valid_box(box1) and is_valid_box(box2):
        length = box1[0] + box2[0]
        width = box1[1] + box2[1]
        height = box1[2] + box2[2]

        return (float(length), float(width), float(height))


def calculate_volume(box):
    if is_valid_box(box):
        return box[0] * box[1] * box[2]
    

def greater_volume(box1, box2):
    if is_valid_box(box1) and is_valid_box(box2):
        print(f"Box 1: {calculate_volume(box1)}. | Box 2: {calculate_volume(box2)}")
        return calculate_volume(box1) > calculate_volume(box2)


box1 = (2, 2, 2.5)
box2 = (2, 2, 2.5)

print(greater_volume(box1, box2))