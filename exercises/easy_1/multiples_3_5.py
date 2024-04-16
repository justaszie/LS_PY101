def multisum(end_number):
    multiples = [num for num in range(1, end_number + 1)
                 if num % 3 == 0 or num % 5 == 0]
    
    return sum(multiples)

# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)