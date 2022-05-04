#############################################################
# FILE : quadratic_equation.py
# WRITER : Oryan Hassidim , oryan.hassidim , 319131579
# EXERCISE : intro2cs2 Ex2 2022
# DESCRIPTION: Functions to calculate quadratic_equation
#              roots.
# STUDENTS I DISCUSSED THE EXERCISE WITH: --
# WEB PAGES I USED: --
# NOTES:
#############################################################


from math import sqrt

# 4
def quadratic_equation(a, b, c):
    """Takes the coefficients  a, b and c of quadratic equation
    and returns its tuple of its roots.
    - if there is only one - the second part of the tuple is None.
    - if ther are no roots - return (None, None)."""
    root = b ** 2 - 4 * a * c
    if root < 0:
        return None, None
    elif root == 0:
        return -b / (2 * a), None
    root = sqrt(root)
    return (-b + root) / (2 * a), (-b - root) / (2 * a)


# 5
def quadratic_equation_user_input():
    """Takes the coefficients  a, b and c of quadratic equation
    from the user, and prints the roots of thart equation."""
    params = input("Insert coefficients a, b, and c: ")
    a, b, c = map(float, params.split(" "))
    if a == 0:
        print("The parameter 'a' may not equal 0")
        return
    root1, root2 = quadratic_equation(a, b, c)
    if (root1, root2) == (None, None):
        print("The equation has no solutions")
        return
    if root2 == None:
        print(f"The equation has 1 solution: {root1}")
        return
    print(f"The equation has 2 solutions: {root1} and {root2}")
