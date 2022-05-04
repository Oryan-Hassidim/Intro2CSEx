#############################################################
# FILE : largest_and_smallest.py
# WRITER : Oryan Hassidim , oryan.hassidim , 319131579
# EXERCISE : intro2cs2 Ex2 2022
# DESCRIPTION: Function to get the largest and smallest
#              number from 3 numbers, and chek this function.
# STUDENTS I DISCUSSED THE EXERCISE WITH: --
# WEB PAGES I USED: --
# NOTES: randoms => check for random numbers and negatives.
#        0,float('0.'+'0'*100+'1'),float('-0.'+'0'*100+'1')
#        => chek very small change.
#############################################################

from random import randint, random

# 3
def largest_and_smallest(a, b, c):
    """Gets 3 numbers, and return tuple of two numbers 
    - the largest one (first) and the smallest one (second)"""
    l = (a, b, c)
    small, large = a, a
    for x in l:
        if x > large:
            large = x
        elif x < small:
            small = x
    return large, small


# 8
def check_largest_and_smallest():
    """Checks the largest_and_smallest() function on some
    inputs"""

    if largest_and_smallest(17, 1, 6) != (17, 1):
        return False
    
    if largest_and_smallest(1, 17, 6) != (17, 1):
        return False
    
    if largest_and_smallest(1, 1, 2) != (2, 1):
        return False
    
    a, b, c = randint(-200, 200), randint(-200, 200), randint(-200, 200)
    l,s = largest_and_smallest(-a,-b,-c)
    if largest_and_smallest(a,b,c) != (-s,-l):
        return False
    
    if largest_and_smallest(
        0, float("0." + "0" * 100 + "1"), float("-0." + "0" * 100 + "1")
    ) != (10 ** -101, -(10 ** -101)):
        return False

    return True
