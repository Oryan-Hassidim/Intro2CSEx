####################################################################
# Oryan Hassidim
# Oryan.Hassidim@mail.huji.ac.il
# last update: 02/05/2022  22:40
####################################################################


from random import randint, random, choice, randrange
import sys
import traceback
import subprocess
from typing import Set

from puzzle_solver import (
    max_seen_cells,
    min_seen_cells,
    check_constraints,
    solve_puzzle,
    how_many_solutions,
    generate_puzzle,
)


B = 0  # black
W = 1  # white


def test_max_seen_cells():
    picture = [[-1, 0, 1, -1],
               [0, 1, -1, 1],
               [1, 0, 1, 0]]
    assert max_seen_cells(picture, 0, 0) == 1
    assert max_seen_cells(picture, 1, 0) == 0
    assert max_seen_cells(picture, 1, 2) == 5
    assert max_seen_cells(picture, 1, 1) == 3


def test_min_seen_cells():
    picture = [[-1, 0, 1, -1],
               [0, 1, -1, 1],
               [1, 0, 1, 0]]
    assert min_seen_cells(picture, 0, 0) == 0
    assert min_seen_cells(picture, 1, 0) == 0
    assert min_seen_cells(picture, 1, 2) == 0
    assert min_seen_cells(picture, 1, 1) == 1


def test_check_constraints():
    picture1 = [[-1, 0, 1, -1], [0, 1, -1, 1], [1, 0, 1, 0]]
    picture2 = [[0, 0, 1, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
    assert check_constraints(picture1, {(0, 3, 5), (1, 2, 5), (2, 0, 1)}) == 0
    assert check_constraints(picture2, {(0, 3, 3), (1, 2, 5), (2, 0, 1)}) == 1
    assert check_constraints(picture1, {(0, 3, 3), (1, 2, 5), (2, 0, 1)}) == 2


def test_solve_puzzle():
    assert solve_puzzle({(0, 3, 3), (1, 2, 5), (2, 0, 1), (0, 0, 0)}, 3, 4) == [
        [0, 0, 1, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
    assert solve_puzzle(
        {(0, 3, 3), (1, 2, 5), (2, 0, 1), (2, 3, 5)}, 3, 4) == None
    assert solve_puzzle({(0, 2, 3), (1, 1, 4), (2, 2, 5)}, 3, 3) in [
        [[0, 0, 1], [1, 1, 1], [1, 1, 1]], [[1, 0, 1], [1, 1, 1], [1, 1, 1]]]


def test_how_many_solutions():
    assert how_many_solutions(
        {(0, 3, 3), (1, 2, 5), (2, 0, 1), (0, 0, 0)}, 3, 4) == 1
    assert how_many_solutions(
        {(0, 3, 3), (1, 2, 5), (2, 0, 1), (2, 3, 5)}, 3, 4) == 0
    assert how_many_solutions({(0, 2, 3), (1, 1, 4), (2, 2, 5)}, 3, 3) == 2
    assert how_many_solutions(
        {(0, 3, 3), (1, 2, 5), (2, 0, 1), (0, 0, 1)}, 3, 4) == 1
    assert how_many_solutions({(0, 2, 3), (1, 1, 4), (2, 2, 5)}, 3, 3) == 2
    assert how_many_solutions({(i, j, 0) for i in range(3)
                              for j in range(3)}, 3, 3) == 1
    assert how_many_solutions(set(), 2, 2) == 16
    assert how_many_solutions({(0, 3, 3), (2, 0, 1)}, 3, 4) == 64


def picture_to_str(picture):
    #s = chr(9607) * 2
    #b = "\033[30m" + s
    #w = "\033[37m" + s
    s = " " * 2
    b = "\033[40m" + s
    w = "\033[47m" + s
    return "\n".join(["".join([b if c == B else w for c in row] + ["\033[49m"]) for row in picture])


def print_picture(picture):
    print(picture_to_str(picture), end="\033[0m\n")


mys = """
WWWWWBBBBBBWWWWW
WWWWBWWWWWWBWWWW
WWWBWWWWWWWWBWWW
WWBWWWBWWBWWWBWW
WBWWWWBWWBWWWWBW
BWWWWWWWWWWWWWWB
BWWWWWWWWWWWWWWB
BWWWWWWWWWWWWWWB
WBWWWBWWWWBWWWBW
WWBWWWBBBBWWWBWW
WWWBWWWWWWWWBWWW
WWWWBWWWWWWBWWWW
WWWWWBBBBBBWWWWW
"""
lst = mys.split("\n")[1:-1]
[[0 if c == "B" else 1 for c in row] for row in lst]

def test_generate_puzzle():
    for i in range(40):
        print(f"\033[4m\033[1m{i+1}:\033[24m\033[22m")
        height = randint(1, 7)
        width = randint(1, 7)
        picture = [[choice([B, W]) for _ in range(height)]
                   for _ in range(width)]
        print("picture:", picture)
        print_picture(picture)
        puzzle = generate_puzzle(picture)
        print("puzzle:", puzzle)
        assert how_many_solutions(puzzle, len(picture), len(picture[0])) == 1
        sol = solve_puzzle(puzzle, len(picture), len(picture[0]))
        print("sol:", sol)
        print_picture(sol)
        print()
        assert sol == picture
    s = [[1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1], [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1], 
         [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1], [1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1],
         [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
         [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0], 
         [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1], [1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1], 
         [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1], [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1], 
         [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]]

    print_picture(s)


def run_test(name, func):
    try:
        func()
        print(f"\033[1;32m{name} test PASSED")
        print("\033[0m", end="")
        return 1
    except Exception as e:
        print(f"\033[1;31m{name} test FAILED\n\t{type(e).__name__}: {e}")
        print(traceback.format_exc())
    print("\033[0m", end="")
    return 0


def main():
    tests = [
        "max_seen_cells",
        "min_seen_cells",
        "check_constraints",
        "solve_puzzle",
        "how_many_solutions",
        "generate_puzzle",
    ]
    count = 0
    for test in tests:
        count += run_test(test, globals()["test_" + test])
    print()
    if count == len(tests):
        print("\033[1;32m==============All OK==============")
    else:
        print(f"\033[1;31m========={count}/{len(tests)} tests passed=========")
    print("\033[0m")


if __name__ == "__main__":
    sys.exit(int(main() or 0))
