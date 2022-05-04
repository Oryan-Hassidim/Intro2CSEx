#############################################################
# FILE : calculate_mathematical_expression.py
# WRITER : Oryan Hassidim , oryan.hassidim , 319131579
# EXERCISE : intro2cs2 Ex2 2022
# DESCRIPTION: Functions to calculate simple math operations.
# STUDENTS I DISCUSSED THE EXERCISE WITH: --
# WEB PAGES I USED: --
# NOTES: 
#############################################################

# Dictionary for better performance - O(1)
opers = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    ":": lambda x, y: x / y,
}

# 1
def calculate_mathematical_expression(arg1, arg2, oper):
    """Takes two arguments (numbers) and operations ('+', '-', 
    '*' or ':') and returns the evaluations. if there is an erorr,
    returns None."""
    if len(oper) != 1 or (oper not in "+-*:"):
        return None
    if (arg2, oper) == (0, ":"):
        return None
    return opers[oper](arg1, arg2)

#2
def calculate_from_string(calc):
    """Takes a string of simple calculation of template "x + y"
    and returns the evaluation."""
    if calc.count(' ') != 2:
        return None
    # By the instructions, we can suppose that
    s1, oper, s2 = str.split(calc, ' ')
    arg1, arg2 = float(s1), float(s2)
    return calculate_mathematical_expression(arg1, arg2, oper)
