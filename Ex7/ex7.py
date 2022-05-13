#################################################################################
# FILE: ex7.py
# WRITER: Oryan Hassidim , oryan.hassidim , 319131579
# EXERCISE: Intro2cs2 ex7 2021-2022
# DESCRIPTION: Simple function which use recursion.
# NOTES:
#################################################################################
from typing import Any, List
from ex7_helper import add, append_to_end, is_odd, subtract_1, divide_by_2


def mult(x: float, y: int) -> float:
    """
    Takes a number and an integer as parameters,
    and returns their production.
    :param x: a number
    :param y: an integer of times
    :return: the result of multiply x by y
    """
    if y == 0:
        return 0
    return add(x, mult(x, subtract_1(y)))


def is_even(n: int) -> bool:
    """
    Takes a number as parameter and returns True if it is even,
    and False otherwise.
    :param n: a number
    :return: True if n is even, False otherwise
    """
    if n == 0:
        return True
    return not is_even(subtract_1(n))


def log_mult(x: float, y: int) -> float:
    """
    Takes a number and an integer as parameters,
    and returns their production.
    :param x: a number
    :param y: an integer of times
    :return: the result of multiply x by y
    """
    if y == 0:
        return 0
    half = log_mult(x, divide_by_2(y))
    res = add(half, half)
    if is_odd(y):
        res = add(x, res)
    return res


def is_power_core(b: int, x: int, so_far: int=-1) -> bool:
    """
    Takes two numbers as parameters and returns True if the second is a power
    of the first, and False otherwise.
    :param b: a number
    :param x: a number
    :param so_far: recursion parameter
    :return: True if x is a power of b, False otherwise
    """

    # initialize the recursion, and check bound values
    if so_far == -1:
        if x == 1:
            return True
        if b == 0:
            return x == 0
        if b == 1:
            return x == 1
        if x == 0:
            return False
        if is_odd(b) != is_odd(x):
            return False
        so_far = b

    # check if the power is a power of the base
    if so_far == x:
        return True
    if so_far > x:
        return False
    # production in O(log(x)), and the log_mult is O(log(b))
    return is_power_core(b, x, int(log_mult(so_far, b)))


def is_power(b: int, x: int) -> bool:
    """
    Takes two numbers as parameters and returns True if the second is a power
    of the first, and False otherwise.
    :param b: a number
    :param x: a number
    :param so_far: recursion parameter
    :return: True if x is a power of b, False otherwise
    """
    return is_power_core(b, x)


def reverse_core(s: str, i: int=0) -> str:
    """
    Takes a string as parameter and returns its reverse.
    :param s: a string
    :return: the reverse of s
    """
    if i == len(s):
        return ""
    return append_to_end(reverse_core(s, i + 1), s[i])


def reverse(s: str) -> str:
    """
    Takes a string as parameter and returns its reverse.
    :param s: a string
    :return: the reverse of s
    """
    return reverse_core(s)

    # another way *with* slicing:
    # if s == "": return ""
    # return append_to_end(s[1:]), s[0])

def play_hanoi(Hanoi: Any, n: int, src: Any, dst: Any, temp: Any) -> None:
    """
    Takes a Hanoi object, an integer, three towers, and returns nothing.
    :param Hanoi: a Hanoi game object
    :param n: an integer
    :param src: a tower
    :param dst: a tower
    :param temp: a tower
    :return: nothing
    """

    # In the ex7.pdf from the site, there is a link to:
    # https://he.wikipedia.org/wiki/%D7%9E%D7%92%D7%93%D7%9C%D7%99_%D7%94%D7%90%D7%A0%D7%95%D7%99
    # which explains the game and give a full code in python...
    # I almost copied the algorithm, and I didn't copy the code.
    # I updated the algorithm to adapt to the requirements.
    if n == 0:
        return
    play_hanoi(Hanoi, n - 1, src, temp, dst)
    Hanoi.move(src, dst)
    play_hanoi(Hanoi, n - 1, temp, dst, src)


def number_of_ones_core(n: int) -> int:
    """
    Takes a number as parameter and returns the number of ones in it.
    :param n: a number
    :return: the number of ones in n
    """
    if n == 0:
        return 0
    return (1 if n % 10 == 1 else 0) + number_of_ones_core(n // 10)


def number_of_ones(n: int) -> int:
    """
    Takes a number as parameter and returns the number of ones in all
    numbers from 0 until itself.
    :param n: a number
    :return: the number of ones in n
    """
    if n == 0:
        return 0
    return number_of_ones_core(n) + number_of_ones(n - 1)


def compare_lists_rec(l1: List[int], l2: List[int], i: int=0) -> bool:
    """
    Takes two lists of integers of same length as parameters
    and returns True if they are equal, and False otherwise.
    :param l1: a list
    :param l2: a list
    :param i: current recursive index
    :return: True if l1 and l2 are equal, False otherwise
    """
    if i == len(l1):
        return True
    if l1[i] != l2[i]:
        return False
    return compare_lists_rec(l1, l2, i + 1)


def compare_lists(l1: List[int], l2: List[int]) -> bool:
    """
    Takes two lists of integers as parameters and returns True if they are equal,
    and False otherwise.
    :param l1: a list
    :param l2: a list
    :return: True if l1 and l2 are equal, False otherwise
    """
    # equality of numbers
    if id(l1) == id(l2):
        return True
    if len(l1) != len(l2):
        return False
    return compare_lists_rec(l1, l2)


def compare_2d_lists_rec(l1: List[List[int]], l2: List[List[int]], i: int=0) -> bool:
    """
    Takes two 2D lists of integers of same length as parameters
    and returns True if they are equal, and False otherwise.
    :param l1: a 2D list
    :param l2: a 2D list
    :param i: current recursive index
    :return: True if l1 and l2 are equal, False otherwise
    """
    if i == len(l1):
        return True
    if not compare_lists(l1[i], l2[i]):
        return False
    return compare_2d_lists_rec(l1, l2, i + 1)


def compare_2d_lists(l1: List[List[int]], l2: List[List[int]]) -> bool:
    """
    Takes two 2D lists of integers as parameters and returns True if they are equal,
    and False otherwise.
    :param l1: a 2D list
    :param l2: a 2D list
    :return: True if l1 and l2 are equal, False otherwise
    """
    # equality of numbers
    if id(l1) == id(l2):
        return True
    if len(l1) != len(l2):
        return False
    return compare_2d_lists_rec(l1, l2)


def magic_list(n: int) -> List[Any]:
    """
    Takes an integer as parameter and returns the n'th of magic list.
    :param n: an integer
    :return: a list of n lists
    """
    if n == 0:
        return []
    res = magic_list(n - 1)
    res.append(magic_list(n - 1))
    return res
