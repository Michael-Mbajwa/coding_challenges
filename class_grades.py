from collections import defaultdict
import numpy as np

def class_grades(students):
    """
    I got this question for my coding test with NextGate Tech
    :param students: (list) Each element of the list is another list with the 
      following elements: Student name (string), class name (string), student grade (int).
    :returns: (list) Each element is a list with the following 
      elements: Class name (string), median grade for students in the class (float).
    """
    records = defaultdict(list)
    result = []
    for student, class_name, grade in students:
        records[class_name].append(grade)
    
    for key, value in records.items():
        result.append([key, np.median(value)])
    return result

students = [["Ana Stevens", "1a", 5], ["Mark Stevens", "1a", 4], ["Jon Jones", "1a", 2], ["Bob Kent", "1b", 4]]
print(class_grades(students))