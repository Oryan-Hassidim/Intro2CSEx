# FILE : Ex.py
# WRITER : Oryan Hassidim , oryan.hassidim , 319131579
# EXERCISE : intro2cs2 Ex1 2022
# DESCRIPTION: A simple Program that prints to the console
#              math functions.
# STUDENTS I DISCUSSED THE EXERCISE WITH: --
# WEB PAGES I USED:
# NOTES: --
#############################################################

from math import *
import math


def golden_ratio():
    """Prints the golden ratio.
    For more information:
    https://en.wikipedia.org/wiki/Golden_ratio"""
    print((1 + sqrt(5)) / 2)


def six_squared():
    """Prints the evaluation of 6 square (6²)."""
    print(pow(6, 2))


def hypotenuse():
    """Prints te length of excess of right-angled
    triangle with sides length: 12, 5."""
    print(hypot(12, 5))


def pi():
    """Prints the constant value Pi (π)."""
    print(math.pi)


def e():
    """Prints the constant value e."""
    print(math.e)


def squares_area():
    """Prints the area of squares with side lenght betwwen
    1 to 10."""
    squares = [i**2 for i in range(1, 11)]
    print(*squares)


if __name__ == "__main__":
    golden_ratio()
    six_squared()
    hypotenuse()
    pi()
    e()
    squares_area()
