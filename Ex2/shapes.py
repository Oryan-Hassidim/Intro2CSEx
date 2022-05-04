#############################################################
# FILE : shapes.py
# WRITER : Oryan Hassidim , oryan.hassidim , 319131579
# EXERCISE : intro2cs2 Ex2 2022
# DESCRIPTION: Function that Takes from the user shape id and
#              its dimentions and returns the area of that
#              shape.
# STUDENTS I DISCUSSED THE EXERCISE WITH: --
# WEB PAGES I USED: --
# NOTES:
#############################################################

from math import sqrt, pi


def circle():
    """Semi function to circle input and calculation."""
    radius = float(input())
    if radius < 0:
        return None
    return pi * radius ** 2


def rect():
    """Semi function to rectangle input and calculation."""
    a, b = map(float, (input(), input()))
    if a < 0 or b < 0:
        return None
    return a * b


def triangle():
    """Semi function to triangle input and calculation."""
    side = float(input())
    if side < 0:
        return None
    return (sqrt(3) / 4) * side ** 2


# for performance - create a list and get the function by index
shapes = [circle, rect, triangle]

# 6
def shape_area():
    """Takes from the user shape id (1=circle, 2=rectangle,\
    3=triangle)
    and its dimentions and returns the area of that shape.
    for unknown id or negative dimention returns None."""
    print("Choose shape (1=circle, 2=rectangle, 3=triangle):", end=" ")
    selected_shape = int(input())
    if selected_shape > 3 or selected_shape < 1: # unknown id
        return None
    return shapes[selected_shape - 1]()
