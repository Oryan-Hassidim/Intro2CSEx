#############################################################
# FILE : temperature.py
# WRITER : Oryan Hassidim , oryan.hassidim , 319131579
# EXERCISE : intro2cs2 Ex2 2022
# DESCRIPTION: Function to check if 2 of 3 numbers larger
#              than a given number.
# STUDENTS I DISCUSSED THE EXERCISE WITH: --
# WEB PAGES I USED: --
# NOTES: Using style specs of clean code -- if-return than
#        than if-elif.
#############################################################

# 7
# better: is_vormir_safe(min, *temps)
def is_vormir_safe(min, temp1, temp2, temp3): 
    """Takes the minimum and three numbers to checks if 2 from 
    the 3 are greater than the minimum.
    if there are - returns True, else - returns False."""
    if temp1 > min:
        return temp2 > min or temp3 > min
    return temp2 > min and temp3 > min
