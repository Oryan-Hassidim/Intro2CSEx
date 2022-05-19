#################################################################################
# FILE: puzzle_solver.py
# WRITER: Oryan Hassidim , oryan.hassidim , 319131579
# EXERCISE: Intro2cs2 ex8 2021-2022
# DESCRIPTION: app for finding solutions for the puzzle.
# NOTES:
#################################################################################
from typing import List, Tuple, Set, Optional, Generator


# We define the types of a partial picture and a constraint (for type
# checking).
Picture = List[List[int]]
Constraint = Tuple[int, int, int]

B = 0  # black
W = 1  # white
U = -1  # unknown
KNOWN = {B, W}
DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

#################################################################################


def check_bounds(matrix, i, j):
    """
    Checks if the given index is in the bounds of the matrix.
    :param matrix: a matrix
    :param i: the row index
    :param j: the column index
    """
    return 0 <= i < len(matrix) and 0 <= j < len(matrix[i])


def seen_cells(picture: Picture, row: int, col: int, blocks_values: Set[int]) -> int:
    """
    Returns the number of cells that are seen by a white cell in the given row and column.
    :param picture: a picture
    :param row: the row of the cell
    :param col: the column of the cell
    :param blocks_values: blocks values
    """
    if picture[row][col] in blocks_values:
        return 0

    seen_cells = 1
    for di, dj in DIRECTIONS:
        i, j = row + di, col + dj
        while check_bounds(picture, i, j) and picture[i][j] not in blocks_values:
            seen_cells += 1
            i, j = i + di, j + dj
    return seen_cells


def max_seen_cells(picture: Picture, row: int, col: int) -> int:
    """
    Returns the maximum number of cells that can be seen by a white cell
    in the given row and column.
    :param picture: a picture
    :param row: the row of the cell
    :param col: the column of the cell
    """
    return seen_cells(picture, row, col, max_seen_cells.__blocks)


def min_seen_cells(picture: Picture, row: int, col: int) -> int:
    """
    Returns the maximum number of cells that can be seen by a white cell
    in the given row and column.
    :param picture: a picture
    :param row: the row of the cell
    :param col: the column of the cell
    """
    return seen_cells(picture, row, col, min_seen_cells.__blocks)

# single instance of the sets
max_seen_cells.__blocks = {B}
min_seen_cells.__blocks = {B, U}

#################################################################################


def check_constraint(picture: Picture, constraint: Constraint) -> int:
    """
    Checks if the given constraint is satisfied.
    :param picture: a picture
    :param constraint: a constraint
    :return: 1 if the constraint is satisfied exactly, 2 if may be satisfied, and else 0.
    """
    i, j, seen = constraint
    min_seen = min_seen_cells(picture, i, j)
    max_seen = max_seen_cells(picture, i, j)
    if max_seen == min_seen == seen:
        return 1
    if min_seen <= seen <= max_seen:
        return 2
    return 0


def check_constraints(picture: Picture, constraints_set: Set[Constraint]) -> int:
    """
    Checks if the given picture satisfies all the constraints in the set.
    :param picture: a picture
    :param constraints_set: a set of constraints
    :return: 1 if the constraints is satisfied exactly, 2 if may be satisfied, and else 0.
    """
    res = set()
    for constraint in constraints_set:
        res.add(check_constraint(picture, constraint))
        if 0 in res:
            return 0
    if 2 in res:
        return 2
    return 1


def check_constraints_on_cell(picture, constraints_set, width, ij) -> int:
    """
    Checks if the given picture satisfies all the constraints in the set.
    Starts with the given cell.
    :param picture: a picture
    :param constraints_set: a set of constraints
    :param width: the width of the picture
    :param ij: the index of the cell from the start
    :return: 1 if the constraints is satisfied exactly, 2 if may be satisfied, and else 0.
    """
    if ij == -1:
        return check_constraints(picture, constraints_set)

    row, col = ij // width, ij % width
    constraints = {(i, j, seen)
                   for i, j, seen in constraints_set if i == row or j == col}
    check_val_c = check_constraints(picture, constraints)
    if check_val_c in {0, 2}:
        return check_val_c
    rest = check_constraints(picture, constraints_set - constraints)
    return max(check_val_c, rest)

#################################################################################


def fill(picture, constraints_set, size, width, ij=0):
    """
    Generates all the possible pictures that can be obtained by filling the given picture.
    :param picture: a picture
    :param constraints_set: a set of constraints
    :param size: the size of the picture
    :param width: the width of the picture
    :param ij: the index of the cell from the start
    :return: generator of solutions
    """
    if ij == size:
        # assert check_constraints(picture, constraints_set) == 1
        yield picture
        return

    i, j = ij // width, ij % width
    original = picture[i][j]
    for fill_option in (KNOWN if original == U else {original}):
        picture[i][j] = fill_option
        yield from fill(picture, constraints_set, size, width, ij + 1)
    picture[i][j] = original


def find_solutions_core(picture, constraints_set, size, width, ij=0):
    """
    Finds all solutions to the puzzle using backtracking.
    :param picture: a picture
    :param constraints_set: a set of constraints
    :param size: the size of the picture
    :param width: the width of the picture
    :param ij: the index of the cell from the start
    :param check: True if checking for this cell is needed, else False
    :return: generator of solutions
    """
    if ij == size:  # the image is full
        if check_constraints_on_cell(picture, constraints_set, width, ij - 1) == 1:
            yield picture
        return

    check_val = check_constraints_on_cell(
        picture, constraints_set, width, ij - 1)

    if check_val == 0:
        return

    if check_val == 1:
        yield from fill(picture, constraints_set, size, width, ij)
        return

    while picture[ij // width][ij % width] in KNOWN:
        ij += 1

    i, j = ij // width, ij % width
    original = picture[i][j]
    for option in KNOWN:
        picture[i][j] = option
        yield from find_solutions_core(picture, constraints_set, size, width, ij + 1)
    picture[i][j] = original


def find_solutions(constraints_set: Set[Constraint], n: int, m: int) -> Generator[Picture, None, None]:
    """
    Finds all solutions to the puzzle using backtracking.
    :param constraints_set: a set of constraints
    :param n: the number of rows
    :param m: the number of columns
    :return: generator of solutions
    """
    picture = [[U] * m for _ in range(n)]
    for i, j, seen in constraints_set:
        if seen == 0:
            picture[i][j] = B
        else:
            picture[i][j] = W
    yield from find_solutions_core(picture, constraints_set, n * m, m)

#################################################################################


def solve_puzzle(constraints_set: Set[Constraint], n: int, m: int) -> Optional[Picture]:
    """
    Solves the puzzle using backtracking.
    :param constraints_set: a set of constraints
    :param n: the number of rows
    :param m: the number of columns
    :return: the solution if it exists, else None
    """
    for sol in find_solutions(constraints_set, n, m):
        return sol
    return None


def how_many_solutions(constraints_set: Set[Constraint], n: int, m: int) -> int:
    """
    Counts the number of solutions to the puzzle.
    :param constraints_set: a set of constraints
    :param n: the number of rows
    :param m: the number of columns
    :return: the number of solutions
    """
    # generator count - the list is many references to the *same* image.
    return len(list(find_solutions(constraints_set, n, m)))

#################################################################################


def excactly_1_sol(constraints_set: Set[Constraint], n: int, m: int):
    """
    Checks if the given constraints has exactly one solution.
    """
    i = 0
    for _ in find_solutions(constraints_set, n, m):
        if i == 1:
            return False
        i += 1
    return i == 1


def find_puzzles_core(constraints, picture) -> Generator[Set[Constraint], None, None]:
    """
    Finds all the possible puzzles *with repetitions* that can be obtained by filling the given picture.
    :param constraints: a set of constraints
    :param picture: a picture
    :return: generator of constraints set which define the picture
    """
    if not excactly_1_sol(constraints, len(picture), len(picture[0])):
        return

    flag = True
    for constraint in constraints:
        constraints.remove(constraint)
        for puzzle in find_puzzles_core(constraints, picture):
            yield puzzle
            flag = False
        constraints.add(constraint)
    if flag:
        yield constraints


def find_puzzles(picture: Picture) -> Generator[Set[Constraint], None, None]:
    """
    Generates all the possible puzzles *with repetitions* that can be obtained by filling the given picture.
    :param picture: a picture
    :return: generator of constraints set which define the picture
    """
    constraints = set()
    for i, row in enumerate(picture):
        for j, _ in enumerate(row):
            constraints.add((i, j, min_seen_cells(picture, i, j)))
    yield from find_puzzles_core(constraints, picture)


def generate_puzzle(picture: Picture) -> Set[Constraint]:
    """
    Generates a puzzle that can be obtained by filling the given picture.
    :param picture: a picture
    :return: a puzzle which define the picture exactly
    """
    for puzzle in find_puzzles(picture):
        return puzzle

#################################################################################


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
