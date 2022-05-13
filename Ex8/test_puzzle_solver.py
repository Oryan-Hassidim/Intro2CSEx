####################################################################
# Oryan Hassidim
# Oryan.Hassidim@mail.huji.ac.il
# last update: 09/05/2022  23:45
####################################################################


from random import randint, choice
import sys
import traceback

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
    picture1 = [[-1, 0, 1, -1],
                [0, 1, -1, 1],
                [1, 0, 1, 0]]
    picture2 = [[0, 0, 1, 1],
                [0, 1, 1, 1],
                [1, 0, 1, 0]]
    assert check_constraints(picture1, {(0, 3, 5), (1, 2, 5), (2, 0, 1)}) == 0
    assert check_constraints(picture2, {(0, 3, 3), (1, 2, 5), (2, 0, 1)}) == 1
    assert check_constraints(picture1, {(0, 3, 3), (1, 2, 5), (2, 0, 1)}) == 2


def test_solve_puzzle():
    assert solve_puzzle({(0, 3, 3), (1, 2, 5), (2, 0, 1), (0, 0, 0)}, 3, 4) == [
        [0, 0, 1, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
    assert solve_puzzle({(3, 0, 3), (2, 1, 5), (0, 2, 1), (0, 0, 0)}, 4, 3) == [
        [0, 0, 1], [0, 1, 0], [1, 1, 1], [1, 1, 0]]
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


def test_puzzles():
    picture = [[1], [1], [1], [1], [1]]
    puzzle = {(1, 0, 5)}
    assert solve_puzzle(puzzle, 5, 1) == picture
    assert how_many_solutions(puzzle, 5, 1) == 1
    picture = [[1, 1, 0, 0, 1]]
    puzzle = {(0, 4, 1), (0, 0, 2)}
    assert solve_puzzle(puzzle, 1, 5) == picture
    assert how_many_solutions(puzzle, 1, 5) == 1
    picture = [[0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [1, 1], [0, 0]]
    puzzle = {(1, 0, 1), (2, 1, 0), (3, 0, 0), (0, 1, 0), (3, 1, 0),
              (5, 1, 2), (6, 0, 0), (4, 0, 0), (4, 1, 0), (6, 1, 0)}
    assert solve_puzzle(puzzle, 7, 2) == picture
    assert how_many_solutions(puzzle, 7, 2) == 1
    picture = [[1, 0, 1, 1], [0, 1, 1, 0]]
    puzzle = {(0, 3, 2), (1, 1, 2), (0, 0, 1)}
    assert solve_puzzle(puzzle, 2, 4) == picture
    assert how_many_solutions(puzzle, 2, 4) == 1
    picture = [[1, 1, 0, 1], [1, 0, 0, 1], [0, 0, 0, 0]]
    puzzle = {(1, 0, 2), (0, 0, 3), (1, 2, 0), (2, 1, 0), (0, 3, 2), (2, 2, 0)}
    assert solve_puzzle(puzzle, 3, 4) == picture
    assert how_many_solutions(puzzle, 3, 4) == 1
    picture = [[0, 0, 0, 0, 0, 1], [1, 0, 1, 0, 0, 0],
               [1, 0, 1, 1, 0, 1], [0, 1, 0, 0, 1, 1]]
    puzzle = {(0, 1, 0), (0, 3, 0), (0, 5, 1), (3, 1, 1), (0, 0, 0),
              (2, 3, 2), (2, 2, 3), (2, 5, 2), (1, 4, 0), (3, 4, 2), (1, 0, 2)}
    assert solve_puzzle(puzzle, 4, 6) == picture
    assert how_many_solutions(puzzle, 4, 6) == 1
    picture = [[0, 0], [0, 1], [1, 1], [1, 1], [1, 0], [0, 1], [0, 1]]
    puzzle = {(6, 0, 0), (0, 0, 0), (5, 1, 2), (3, 0, 4),
              (4, 0, 3), (5, 0, 0), (2, 1, 4)}
    assert solve_puzzle(puzzle, 7, 2) == picture
    assert how_many_solutions(puzzle, 7, 2) == 1
    picture = [[1, 0, 1, 0], [0, 0, 0, 0]]
    puzzle = {(0, 2, 1), (1, 1, 0), (1, 3, 0), (0, 0, 1)}
    assert solve_puzzle(puzzle, 2, 4) == picture
    assert how_many_solutions(puzzle, 2, 4) == 1
    picture = [[1, 1], [1, 0], [0, 1], [0, 1]]
    puzzle = {(2, 1, 2), (3, 1, 2), (0, 1, 2), (1, 0, 2)}
    assert solve_puzzle(puzzle, 4, 2) == picture
    assert how_many_solutions(puzzle, 4, 2) == 1
    picture = [[0, 1, 0, 0, 0, 1, 0], [0, 1, 1, 0, 0, 1, 1], [1, 0, 0, 1, 0, 0, 0], [
        1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1, 0]]
    puzzle = {(0, 3, 0), (5, 3, 0), (1, 1, 3), (1, 5, 3), (3, 2, 6), (0, 0, 0), (0, 2, 0), (4, 1, 4), (0, 5, 2),
              (2, 0, 3), (4, 0, 5), (4, 6, 2), (3, 1, 0), (1, 4, 0), (5, 5, 1), (3, 3, 6), (3, 4, 5), (4, 3, 0)}
    assert solve_puzzle(puzzle, 6, 7) == picture
    assert how_many_solutions(puzzle, 6, 7) == 1
    picture = [[1], [1], [1], [1]]
    puzzle = {(1, 0, 4)}
    assert solve_puzzle(puzzle, 4, 1) == picture
    assert how_many_solutions(puzzle, 4, 1) == 1
    picture = [[0, 0, 0, 1, 0, 0, 1], [0, 1, 1, 1, 0, 0, 1], [1, 0, 1, 1, 0, 1, 0], [
        1, 1, 1, 1, 0, 0, 0], [0, 0, 1, 1, 0, 1, 1], [1, 1, 0, 1, 0, 0, 0], [0, 0, 0, 1, 1, 0, 1]]
    puzzle = {(0, 6, 2), (2, 5, 1), (6, 6, 1), (1, 1, 3), (5, 1, 2), (1, 6, 2), (4, 5, 2), (3, 3, 10),
              (0, 0, 0), (6, 4, 2), (2, 3, 8), (3, 0, 5), (0, 3, 7), (1, 2, 6), (5, 0, 2), (4, 6, 2)}
    assert solve_puzzle(puzzle, 7, 7) == picture
    assert how_many_solutions(puzzle, 7, 7) == 1
    picture = [[0, 0, 0], [1, 1, 1], [0, 0, 1]]
    puzzle = {(0, 2, 0), (1, 1, 3), (1, 0, 3), (1, 2, 4)}
    assert solve_puzzle(puzzle, 3, 3) == picture
    assert how_many_solutions(puzzle, 3, 3) == 1
    picture = [[0, 1, 1], [1, 1, 1], [0, 1, 0], [0, 1, 1]]
    puzzle = {(3, 2, 2), (0, 1, 5), (1, 2, 4), (2, 1, 4)}
    assert solve_puzzle(puzzle, 4, 3) == picture
    assert how_many_solutions(puzzle, 4, 3) == 1
    picture = [[0, 1, 1, 0], [1, 1, 0, 1]]
    puzzle = {(1, 3, 1), (0, 2, 2), (1, 0, 2)}
    assert solve_puzzle(puzzle, 2, 4) == picture
    assert how_many_solutions(puzzle, 2, 4) == 1
    picture = [[1, 1, 1, 0, 0, 0]]
    puzzle = {(0, 5, 0), (0, 3, 0), (0, 2, 3), (0, 4, 0)}
    assert solve_puzzle(puzzle, 1, 6) == picture
    assert how_many_solutions(puzzle, 1, 6) == 1
    picture = [[0, 0, 1, 1], [1, 1, 1, 1]]
    puzzle = {(0, 0, 0), (0, 3, 3), (1, 2, 5)}
    assert solve_puzzle(puzzle, 2, 4) == picture
    assert how_many_solutions(puzzle, 2, 4) == 1
    picture = [[1, 0, 1, 0, 0], [1, 0, 0, 1, 1], [0, 0, 1, 0, 0], [
        0, 0, 1, 0, 0], [1, 0, 0, 1, 0], [0, 1, 1, 0, 0], [1, 0, 1, 1, 1]]
    puzzle = {(2, 1, 0), (4, 0, 1), (2, 3, 0), (0, 2, 1), (5, 2, 3), (1, 3, 2), (3, 4, 0), (4, 3, 1),
              (0, 4, 0), (5, 4, 0), (6, 0, 1), (3, 2, 2), (3, 1, 0), (2, 4, 0), (6, 2, 4), (0, 0, 2), (1, 0, 2)}
    assert solve_puzzle(puzzle, 7, 5) == picture
    assert how_many_solutions(puzzle, 7, 5) == 1
    picture = [[1, 0, 1], [1, 1, 0], [1, 0, 1],
               [1, 1, 0], [1, 1, 0], [1, 0, 1]]
    puzzle = {(0, 2, 1), (1, 1, 2), (5, 2, 1), (2, 2, 1), (4, 1, 3), (2, 0, 6)}
    assert solve_puzzle(puzzle, 6, 3) == picture
    assert how_many_solutions(puzzle, 6, 3) == 1
    picture = [[1, 0, 1, 1]]
    puzzle = {(0, 0, 1), (0, 3, 2)}
    assert solve_puzzle(puzzle, 1, 4) == picture
    assert how_many_solutions(puzzle, 1, 4) == 1
    picture = [[0, 1, 0], [1, 0, 0], [0, 0, 1],
               [0, 1, 1], [0, 0, 1], [0, 0, 1]]
    puzzle = {(1, 0, 1), (1, 2, 0), (0, 1, 1), (4, 0, 0),
              (2, 2, 4), (3, 1, 2), (5, 0, 0), (5, 1, 0)}
    assert solve_puzzle(puzzle, 6, 3) == picture
    assert how_many_solutions(puzzle, 6, 3) == 1
    picture = [[1, 1, 1, 0], [0, 1, 1, 1], [1, 0, 0, 0]]
    puzzle = {(0, 0, 3), (2, 0, 1), (2, 2, 0), (1, 2, 4), (2, 3, 0)}
    assert solve_puzzle(puzzle, 3, 4) == picture
    assert how_many_solutions(puzzle, 3, 4) == 1
    picture = [[0, 0, 1], [1, 0, 0], [0, 0, 0], [1, 1, 0], [0, 1, 1]]
    puzzle = {(0, 2, 1), (1, 0, 1), (4, 2, 2), (3, 0, 2), (4, 1, 3), (2, 2, 0)}
    assert solve_puzzle(puzzle, 5, 3) == picture
    assert how_many_solutions(puzzle, 5, 3) == 1
    picture = [[0, 1, 0]]
    puzzle = {(0, 1, 1)}
    assert solve_puzzle(puzzle, 1, 3) == picture
    assert how_many_solutions(puzzle, 1, 3) == 1
    picture = [[1, 1], [0, 0], [1, 0], [0, 1], [1, 0], [0, 1]]
    puzzle = {(4, 0, 1), (2, 0, 1), (5, 1, 1), (0, 0, 2), (0, 1, 2), (3, 1, 1)}
    assert solve_puzzle(puzzle, 6, 2) == picture
    assert how_many_solutions(puzzle, 6, 2) == 1
    picture = [[0, 0, 1, 1, 1, 1, 1], [
        1, 0, 0, 0, 0, 1, 1], [0, 1, 1, 0, 1, 1, 0]]
    puzzle = {(2, 5, 4), (1, 0, 1), (2, 1, 2), (0, 3, 5),
              (0, 6, 6), (0, 2, 5), (0, 4, 5)}
    assert solve_puzzle(puzzle, 3, 7) == picture
    assert how_many_solutions(puzzle, 3, 7) == 1
    picture = [[0], [1]]
    puzzle = {(1, 0, 1)}
    assert solve_puzzle(puzzle, 2, 1) == picture
    assert how_many_solutions(puzzle, 2, 1) == 1
    picture = [[1, 1, 0]]
    puzzle = {(0, 0, 2)}
    assert solve_puzzle(puzzle, 1, 3) == picture
    assert how_many_solutions(puzzle, 1, 3) == 1
    picture = [[1, 0, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 1, 0], [0, 0, 1, 1, 1, 0, 1], [
        0, 0, 0, 1, 1, 0, 1], [1, 0, 1, 0, 1, 0, 0], [1, 1, 0, 0, 0, 0, 1], [1, 0, 1, 1, 0, 0, 0]]
    puzzle = {(4, 2, 1), (0, 0, 1), (2, 4, 5), (3, 0, 0), (5, 1, 2), (5, 6, 1), (4, 0, 3), (4, 4, 3),
              (6, 2, 2), (2, 0, 0), (1, 5, 2), (0, 3, 7), (6, 5, 0), (1, 2, 3), (3, 1, 0), (3, 6, 2), (5, 3, 0)}
    assert solve_puzzle(puzzle, 7, 7) == picture
    assert how_many_solutions(puzzle, 7, 7) == 1
    picture = [[0, 0, 0, 1, 1, 0, 1], [1, 0, 1, 1, 0, 0, 1], [
        1, 0, 1, 0, 1, 0, 1], [1, 1, 0, 0, 0, 0, 1], [0, 0, 0, 1, 0, 1, 0]]
    puzzle = {(0, 1, 0), (2, 6, 4), (4, 3, 1), (2, 4, 1), (1, 0, 3), (1, 6, 4),
              (2, 0, 3), (4, 5, 1), (1, 2, 3), (4, 1, 0), (0, 4, 2), (3, 0, 4)}
    assert solve_puzzle(puzzle, 5, 7) == picture
    assert how_many_solutions(puzzle, 5, 7) == 1
    picture = [[0, 1, 1, 0, 1], [1, 1, 0, 0, 1], [0, 0, 1, 0, 1],
               [0, 0, 0, 1, 1], [1, 0, 1, 1, 1], [0, 0, 1, 0, 0]]
    puzzle = {(4, 0, 1), (1, 4, 5), (0, 2, 2), (2, 2, 1), (2, 0, 0),
              (5, 2, 2), (3, 1, 0), (3, 3, 3), (5, 1, 0), (1, 0, 2), (0, 4, 5)}
    assert solve_puzzle(puzzle, 6, 5) == picture
    assert how_many_solutions(puzzle, 6, 5) == 1
    picture = [[1, 1, 1, 0, 0], [1, 1, 0, 1, 1]]
    puzzle = {(0, 2, 3), (0, 4, 0), (1, 0, 3), (1, 4, 2)}
    assert solve_puzzle(puzzle, 2, 5) == picture
    assert how_many_solutions(puzzle, 2, 5) == 1
    picture = [[0, 0, 1], [1, 1, 1]]
    puzzle = {(1, 0, 3), (0, 2, 2)}
    assert solve_puzzle(puzzle, 2, 3) == picture
    assert how_many_solutions(puzzle, 2, 3) == 1
    picture = [[0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    puzzle = {(0, 5, 0), (1, 2, 0), (0, 3, 0), (1, 4, 0), (0, 4, 0),
              (1, 5, 0), (1, 0, 0), (1, 3, 0), (0, 1, 1)}
    assert solve_puzzle(puzzle, 2, 6) == picture
    assert how_many_solutions(puzzle, 2, 6) == 1
    picture = [[0, 0, 1, 1, 0], [1, 0, 0, 0, 0], [0, 1, 0, 0, 1],
               [0, 1, 1, 1, 1], [1, 1, 0, 0, 1], [0, 1, 1, 1, 1]]
    puzzle = {(1, 0, 1), (0, 3, 2), (3, 3, 4), (2, 4, 4), (5, 3, 4),
              (4, 0, 2), (2, 1, 4), (4, 3, 0), (0, 2, 2)}
    assert solve_puzzle(puzzle, 6, 5) == picture
    assert how_many_solutions(puzzle, 6, 5) == 1
    picture = [[1, 1, 1, 1, 1, 1, 1], [1, 0, 1, 0, 1, 1, 1]]
    puzzle = {(1, 6, 4), (1, 2, 2), (0, 0, 8)}
    assert solve_puzzle(puzzle, 2, 7) == picture
    assert how_many_solutions(puzzle, 2, 7) == 1
    picture = [[0, 1, 1, 1], [1, 0, 1, 1], [0, 1, 0, 0], [
        1, 1, 0, 1], [0, 0, 0, 1], [1, 1, 1, 1], [0, 0, 0, 1]]
    puzzle = {(5, 0, 4), (1, 0, 1), (6, 3, 4), (4, 3, 4), (3, 0, 2),
              (5, 3, 7), (6, 1, 0), (0, 3, 4), (3, 1, 3), (1, 2, 3)}
    assert solve_puzzle(puzzle, 7, 4) == picture
    assert how_many_solutions(puzzle, 7, 4) == 1
    picture = [[0]]
    puzzle = {(0, 0, 0)}
    assert solve_puzzle(puzzle, 1, 1) == picture
    assert how_many_solutions(puzzle, 1, 1) == 1
    picture = [[0, 1, 0, 0, 0]]
    puzzle = {(0, 3, 0), (0, 4, 0), (0, 1, 1)}
    assert solve_puzzle(puzzle, 1, 5) == picture
    assert how_many_solutions(puzzle, 1, 5) == 1
    picture = [[1, 0, 1, 0, 1, 1, 1], [0, 1, 1, 0, 0, 0, 1], [1, 1, 1, 1, 1, 0, 0], [
        1, 1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 1, 1]]
    puzzle = {(5, 5, 0), (0, 0, 1), (4, 3, 2), (0, 6, 4), (1, 5, 0), (3, 5, 2), (6, 0, 2), (0, 2, 6), (5, 4, 0),
              (5, 6, 0), (6, 3, 0), (2, 1, 7), (6, 6, 2), (1, 4, 0), (5, 2, 8), (3, 6, 2), (1, 1, 4), (3, 0, 4)}
    assert solve_puzzle(puzzle, 7, 7) == picture
    assert how_many_solutions(puzzle, 7, 7) == 1


def picture_to_str(picture):
    s = " " * 2
    b = "\033[40m" + s
    w = "\033[47m" + s
    return "\n".join(["".join([b if c == B else w for c in row] + ["\033[49m"]) for row in picture])


def print_picture(picture):
    print(picture_to_str(picture), end="\033[0m\n")


def print_picture_2(picture, constraints):
    cons = {(i, j): k for i, j, k in constraints}
    for i, row in enumerate(picture):
        for j, cell in enumerate(row):
            if cell == B:
                print("\033[40m\033[39m", end="")
            else:
                print("\033[47m\033[30m", end="")
            if (i, j) in cons:
                print(f"{cons[i,j]:<2}", end="")
            else:
                print("  ", end="")
        print("\033[0m")


def test_generate_puzzle():
    for i in range(40):
        print(f"\033[4m\033[1m{i+1}:\033[24m\033[22m")
        height = randint(1, 7)
        width = randint(1, 7)
        picture = [[choice([B, W]) for _ in range(width)]
                   for _ in range(height)]
        print("picture:", picture)
        puzzle = generate_puzzle(picture)
        print("puzzle:", puzzle)
        assert how_many_solutions(puzzle, height, width) == 1
        for cons in puzzle:
            assert how_many_solutions(puzzle - {cons}, height, width) > 1, \
                f"minimal constraints needed!!\nunnecessary constraint: {cons}"
        sol = solve_puzzle(puzzle, height, width)
        assert check_constraints(sol, puzzle) == 1
        print_picture_2(sol, puzzle)
        print()
        assert sol == picture


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
        "puzzles",
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
