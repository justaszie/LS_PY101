"""
input: 2 arguments of any type 
output: boolean True or False value

requirements:
    - return value should return:
        - True if one of the 2 arguments is truthy but not both
        - False if both arguments are falsy or both arguments are true 
    - We assument that both arguments are provided - no validation of missing arguments

Algorithm:    
1. START
2. if first argument is truthy and second argment is falsy OR 
    first argument is falsy and second argument is truthy: return True
    else: return False
3. END

"""

def xor(value1, value2):
    # Below doesn't work because in case of value1 being falsy and value2 being truthy, it will return the actual truthy valuye    
    # return value1 and not value2 or not value1 and value2  
    # if (value1 and not value2) or (not value1 and value2):
    #     return True
    # else:
    #     return False
    
    # Alternatively, we can use bool():
    return bool((not value1 and value2) or (value1 and not value2))

# print(xor(5, 0) == True)
# print(xor(0, 5) == True)
# print(xor(False, True) == True)
# print(xor(1, 1) == False)
# print(xor(True, True) == False)

print(xor(1, 0))
