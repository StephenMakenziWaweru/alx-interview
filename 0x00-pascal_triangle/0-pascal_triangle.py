#!/usr/bin/python3
"""
Returns a list of lists of integers representing the Pascals triangle
"""

def pascal_triangle(n):
    """returns pascal's triangle ints"""
    if n <= 0:
        return []

