#############################################################
# FILE : ex3.py
# WRITER : Oryan Hassidim , oryan.hassidim , 319131579
# EXERCISE : intro2cs2 Ex3 2022
# DESCRIPTION: Functions who used loops and lists.
# STUDENTS I DISCUSSED THE EXERCISE WITH: --
# WEB PAGES I USED:
# https://jakevdp.github.io/WhirlwindTourOfPython/04-semantics-operators.html
# NOTES:
#############################################################


from typing import Sequence


def input_list():
    """The function takes from the user list of numbers and returns
    list of the numbers and their sum."""
    lst = []
    lst_sum = 0
    current = input()
    while current != "":
        num = float(current)
        lst.append(num)
        lst_sum += num
        current = input()
    lst.append(lst_sum)
    return lst


def inner_product(vec_1, vec_2):
    """Function which takes two vectors as parameters and returns
    the value of their inner production.
    If the lengths of the functions is different, returns None."""
    count = len(vec_1)
    result = 0
    if count != len(vec_2):
        return None

    # We shouldn't use zip function, so we iterate by index.
    for i in range(count):
        result += vec_1[i] * vec_2[i]
    return result


def sequence_monotonicity(sequence):
    """Function which takes a list of numbers as parameter
    and returns a list with 4 elements:
       - result[0] := the sequence is monotonically increasing;
       - result[1] := the sequence is strictly increasing;
       - result[2] := the sequence is monotonically decreasing;
       - result[3] := the sequence is strictly decreasing"""

    # "No matter how large the list is, index lookup and assignment
    # take a constant amount of time and are thus O(1)."
    # https://bradfieldcs.com/algos/analysis/performance-of-python-types/
    # less CPU and time performance than 4 local variables,
    # but more simple and shorter code.

    # for saving the balance of performance, length of code and
    # simplicity we will check the list with only one loop, without
    # more functions.
    # The *and* and *or* keywords are optimized by defult and don't
    # evaluate the second argument if it is not needed.
    # There are more performant implementation!!! but I prefer this
    # implementation.

    result = [True, True, True, True]
    if len(sequence) == 0: return result
    last = sequence[0]

    for x in sequence[1:]:
        result[1] = result[1] and last < x
        result[0] = result[1] or (result[0] and last <= x)
        result[3] = result[3] and last > x
        result[2] = result[3] or (result[2] and last >= x)
        last = x

    return result


def monotonicity_inverse(def_bool):
    """The function takes a booleans list as parameter which define
    the monotonicity of sequence and returns a list for example.
       - def_bool[0] := the sequence is monotonically increasing;
       - def_bool[1] := the sequence is strictly increasing;
       - def_bool[2] := the sequence is monotonically decreasing;
       - def_bool[3] := the sequence is strictly decreasing"""

    # Classic PROLOG function

    if def_bool[1]:
        if def_bool[2] or def_bool[3] or not def_bool[0]:
            return None
        return [0, 1, 2, 3]

    if def_bool[3]:
        if def_bool[0] or def_bool[1] or not def_bool[2]:
            return None
        return [0, -1, -2, -3]

    if def_bool[0]:
        if def_bool[2]:
            return [0, 0, 0, 0]
        return [0, 1, 1, 2]

    if def_bool[2]:
        return [0, -1, -1, -2]

    return [0, 1, -1, 0]


# def monotonicity_inverse_test():
#    """Check monotonicity_inverse() function."""
#    for x in range(2 ** 4):
#        # trnsform the binary string of the number to bool list.
#        param = [True if i == "1" else False for i in "{0:04b}".format(x)]
#        sample = monotonicity_inverse(param)
#        if sample == None:
#            print(f"{param} -- None")
#        else:
#            test = sequence_monotonicity(sample)
#            print(f"{param} -- {sample} {'V' if test == param else 'X'}")
#    # OUTPUT:
#    # [False, False, False, False] -- [0, 1, -1, 0] V
#    # [False, False, False, True] -- None
#    # [False, False, True, False] -- [0, -1, -1, -2] V
#    # [False, False, True, True] -- [0, -1, -2, -3] V
#    # [False, True, False, False] -- None
#    # [False, True, False, True] -- None
#    # [False, True, True, False] -- None
#    # [False, True, True, True] -- None
#    # [True, False, False, False] -- [0, 1, 1, 2] V
#    # [True, False, False, True] -- None
#    # [True, False, True, False] -- [0, 0, 0, 0] V
#    # [True, False, True, True] -- None
#    # [True, True, False, False] -- [0, 1, 2, 3] V
#    # [True, True, False, True] -- None
#    # [True, True, True, False] -- None
#    # [True, True, True, True] -- None


def my_map(l, f):
    result = []
    for x in l:
        result.append(f(x))
    return result


def my_or(b1, b2):
    return b1 or b2


def my_and(b1, b2):
    return b1 and b2


def my_reduce(l, f, init):
    result = init
    for i in l:
        result = f(result, i)
    return result


def my_all(l, predicate):
    return my_reduce(my_map(l, predicate), my_and, True)


def my_any(l, predicate):
    return my_reduce(my_map(l, predicate), my_or, False)


def my_add(x, y):
    return x + y


def my_sum(l):
    return my_reduce(l, my_add, 0)


def min(x, y):
    if x < y:
        return x
    return y


# most efficient
primes_for_asafi__primes_cache = [2, 3, 5, 7]
primes_for_asafi__last_collect_cache = 3


def primes_for_asafi__creative(n):
    """Function which takes as argument number n and returns
    list of first n primes. Most creative I can."""

    # It's long function (34 lines of code), but I can't put part of the
    # code in another function because there are a lot local variables.

    # Rather than using lists, I using the binary representation of
    # numbers, when 0 in index (from right) is non-prime and 1 is prime.
    global primes_for_asafi__primes_cache
    global primes_for_asafi__last_collect_cache
    primes = primes_for_asafi__primes_cache
    last_collect = primes_for_asafi__last_collect_cache
    if n <= len(primes):
        return primes[:n]

    # we want to keep the results in cache and don't do twice the operation,
    # so I check n^2 first numbers for primes.
    # n2 = n^2
    n2 = n ** 2
    # whole is constant to other operations,
    # whole = 0b111...111 (n^2) times
    whole = (1 << (n2 + 1)) - 1
    # result is dynamic and here we keep the changes
    result = whole
    i = 0

    while i < n2:
        # i = 2 --> p = 5
        p = primes[i]
        # p_0b = 0b10000
        p_0b = 1 << (p - 1)

        # p_filter = 0b...10000_10000_10000_100000
        p_filter = 0
        for _ in range(n2 // p + 1):
            p_filter += 1
            p_filter = p_filter << p

        # p_filter = 0b...10000_10000_10000_10000
        p_filter = p_filter >> 1
        # p_filter = 0b...10000_10000_10000_00000
        p_filter -= p_0b

        # p_filter = 0b...01111_01111_01111_11111
        p_filter = whole ^ p_filter

        # result: 0b...11111_11111_11111_11111
        # 2:    & 0b...01010_10101_01010_10111
        # 3:    & 0b...11011_01101_10110_11111
        # 5:    & 0b...01111_01111_01111_11111
        #     --> 0b...01010_00101_00010_10111
        result = result & p_filter

        i += 1
        if len(primes) == i:
            current_state = result
            # push collected part
            current_state = current_state >> (last_collect ** 2)

            for j in range(last_collect ** 2, min(n ** 2, p ** 2)):
                # check if current index is prime
                if current_state & 1:
                    primes.append(j + 1)
                current_state = current_state >> 1

            last_collect = int(min(n, p))
            if n <= len(primes):
                # update the cache
                primes_for_asafi__primes_cache = primes
                primes_for_asafi__last_collect_cache = last_collect
                # return first n elements
                return primes[:n]


def primes_for_asafi__faster(n):
    # Check the cache
    global primes_for_asafi__primes_cache
    global primes_for_asafi__last_collect_cache
    primes = primes_for_asafi__primes_cache
    if n <= len(primes):
        return primes[:n]

    odd_numbers = [True, True, True] + [True] * int(n ** 1.3)  # 1,3,5...
    length = len(odd_numbers)
    primes = [2]
    for i in range(1, length):
        if odd_numbers[i]:
            number = 2 * i + 1
            primes.append(number)
            for j in range((number ** 2) // 2, length, number):
                odd_numbers[j] = False
        if len(primes) >= n:
            primes_for_asafi__primes_cache = primes
            primes_for_asafi__last_collect_cache = int(primes[-1] ** 0.5)
            return primes[:n]


def primes_for_asafi(n):
    """Function which takes as argument number n and returns
    list of first n primes. Most efficient I can."""

    # return primes_for_asafi__creative(n)
    return primes_for_asafi__faster(n)

# print(primes_for_asafi(100))
# OUTPUT: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541]
# WEB:     2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541

def add_vectors(vec1, vec2):
    """Takes 2 vectors as parameter and returns the sum of them
    (cordinate cordinate addition)."""
    result = []
    for i in range(len(vec1)):
        result.append(vec1[i] + vec2[i])
    return result


def sum_of_vectors(vec_lst):
    """Takes list of vectors as parameter and returns the sum of
    them (cordinate cordinate addition)."""
    if vec_lst == []:
        return None
    return my_reduce(vec_lst[1:], add_vectors, vec_lst[0].copy())


def num_of_orthogonal(vectors):
    """Takes list of vectors as parameter and returns the count of
    orthogonal pairs in the list."""
    length = len(vectors)
    result = 0
    for i in range(length):
        for j in range(i + 1, length):
            if inner_product(vectors[i], vectors[j]) == 0:
                result += 1
    return result
