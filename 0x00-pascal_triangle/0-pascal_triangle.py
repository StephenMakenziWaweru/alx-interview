#!/usr/bin/python3
"""
Returns a list of lists of integers representing the Pascals triangle
"""
from math import factorial
def pascal_triangle(n):
    """returns pascal's triangle ints"""
    if n <= 0:
        return []
    pascal = []
    for i in range(n):
        pascal_temp = []
        for j in range(i + 1):
            pascal_temp.append(factorial(i)//(factorial(j)*factorial(i-j)))
        pascal.append(pascal_temp)
    return pascal
