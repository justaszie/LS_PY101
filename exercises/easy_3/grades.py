"""

Write a function that determines the mean (average) of the three scores passed to it, and returns the letter associated with that grade.

PROBLEM
    - Inputs: 3 numbers (scores)
    - Outputs: A letter representing the grade, corresponding to the mean score. 
    - Rules Requirements:
        -  Score to grade mapping
            90 <= score <= 100: 'A'
            80 <= score < 90: 'B'
            70 <= score < 80: 'C'
            60 <= score < 70: 'D'
            0 <= score < 60: 'F'
        - There is no need to check for negative values or values greater than 100. 
        - Input must be int or float.

EXAMPLES:
print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True

DATA:
    - String for grade
    - Dictionary for score to grade mapping. Key = grade, value = tuple(range_start, end_range)
    - Floats for grades. 

    
ALGORITHM 
1. Start
2. Calculate mean of the 3 scores
3. Compare the mean score with the defined set of intervals and return corresponding grade letter.
4. End


"""

def get_grade(score1, score2, score3):
    mean_score = (score1 + score2 + score3) / 3
    # if mean_score >= 90 and mean_score <= 100:
    #     return 'A'
    # elif mean_score >= 80:
    #     return 'B'
    # elif mean_score >= 70:
    #     return 'C'
    # elif mean_score >= 60:
    #     return 'D'
    # else:
    #     return 'F'
    
    mapping = {'A': (90, 100),
               'B': (80, 89),
               'C': (70, 79),
               'D': (60, 69),
               'F': (0, 59)
    }

    for grade, interval in mapping.items():
        if mean_score >= interval[0] and mean_score <= interval[1]:
            return grade

print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(81, 81, 82) == "B")      # True
print(get_grade(72, 75, 69) == "C")      # True
print(get_grade(61, 72, 60) == "D")      # True
print(get_grade(1, 2, 49) == "F")      # True
