from board import Board
from car import Car

VERTICAL = 0
HORIZONTAL = 1
MOVE_UP = "u"
MOVE_DOWN = "d"
MOVE_LEFT = "l"
MOVE_RIGHT = "r"


def test_initial_works():
    board = Board()
    # ensure target_location is as expected
    assert (3, 7) == board.target_location()

    # ensure cell_list begins empty
    assert 7*7+1 == len(board.cell_list())
    for row, col in board.cell_list():
        assert board.cell_content((row, col)) is None

    # no moves without cars
    assert board.possible_moves() == []


def test_add_car():
    board = Board()
    car1 = Car("R", 5, (0, 0), HORIZONTAL)
    assert board.add_car(car1)

    # can't add same car instance twice
    assert not board.add_car(car1)
    # can't add car with same name
    assert not board.add_car(Car("R", 2, (5,5), VERTICAL))

    # can't add car out of bounds
    assert not board.add_car(Car("Y", 1, (0, -1), VERTICAL))
    assert not board.add_car(Car("Y", 1, (-1, 0), HORIZONTAL))
    # can't add car with length that makes it go out of bounds
    assert not board.add_car(Car("Y", 8, (2, 0), HORIZONTAL))
    assert not board.add_car(Car("Y", 7, (1, 4), VERTICAL))
    # can't add car that might collide with car1
    assert not board.add_car(Car("Y", 1, (0, 4), HORIZONTAL))

    # the board isn't aware of limits regarding car names, so this is valid
    car2 = Car("ZO", 2, (5, 5), VERTICAL)
    assert board.add_car(car2)

    # can't add a car that collides with car2
    assert not board.add_car(Car("B", 1, (6, 5), HORIZONTAL))
    assert not board.add_car(Car("B", 2, (4, 5), VERTICAL))

    # ensure none of the cars that should've failed to be added, were added somehow
    # so we should only have have 7 occupied cells(5 from 'R', 2 from 'ZO').
    assert 7 == sum(1 for coord in board.cell_list() if board.cell_content(coord) if coord is not None)


def test_board_str_different_representations():
    # here, we ensure that each operation that changes the board's state to a
    # new one generates a DIFFERENT string (even though we don't know how said string looks like)
    board = Board()
    board_strs = {str(board)}

    assert board.add_car(Car("R", 2, (0, 0), HORIZONTAL))
    board_strs.add(str(board))
    assert board.move_car("R", MOVE_RIGHT)
    board_strs.add(str(board))

    # we performed 3 operations that changed the board(to 3 different states)
    # so we should've seen 3 different strings
    assert 3 == len(board_strs)


def test_cell_content_works():
    board = Board()
    car1 = Car("R", 2, (0,0), HORIZONTAL)
    car2 = Car("Y", 2, (1,1), VERTICAL)
    assert board.add_car(car1)
    assert board.add_car(car2)

    assert "R" == board.cell_content((0, 0))
    assert "R" == board.cell_content((0, 1))
    assert "Y" == board.cell_content((1, 1))
    assert "Y" == board.cell_content((2, 1))

    # the destination (3,7) is considered part of the board:
    winning_car = Car("O", 3, (3,4), HORIZONTAL)
    assert board.add_car(winning_car)
    assert board.move_car("O", MOVE_RIGHT)
    assert "O" == board.cell_content(board.target_location())

    # a horizontal car at (3,6) doesn't necessarily mean it's at (3,7) too
    another_board = Board()
    not_a_winning_car = Car("R", 1, (3, 6), HORIZONTAL)
    assert another_board.add_car(not_a_winning_car)
    assert another_board.cell_content(board.target_location()) is None


def test_possible_moves_works():
    board = Board()

    def car_moves(car_name):
        return sorted(move for name, move, _desc in board.possible_moves() if car_name == name)

    car1 = Car("R", 2, (1, 2), HORIZONTAL)
    car2 = Car("Y", 2, (3, 3), VERTICAL)
    assert board.add_car(car1)
    assert board.add_car(car2)
    assert sorted([MOVE_LEFT, MOVE_RIGHT]) == car_moves("R")
    assert sorted([MOVE_UP, MOVE_DOWN]) == car_moves("Y")

    blocking_r_from_left = Car("O", 2, (1, 0), HORIZONTAL)
    assert board.add_car(blocking_r_from_left)
    assert sorted([MOVE_RIGHT]) == car_moves("R")
    assert [] == car_moves("O")

    blocking_y_from_down = Car("Wut", 1, (5, 3), HORIZONTAL)
    assert board.add_car(blocking_y_from_down)
    assert sorted([MOVE_UP]) == car_moves("Y")
    assert sorted([MOVE_LEFT, MOVE_RIGHT]) == car_moves("Wut")


def test_move_car():
    board = Board()

    def get_car_cords(car_name):
        return sorted(coord for coord in board.cell_list() if board.cell_content(coord) == car_name)

    car1 = Car("R", 2, (0, 0), HORIZONTAL)
    car2 = Car("Y", 2, (1, 0), VERTICAL)
    assert board.add_car(car1)
    assert board.add_car(car2)

    assert sorted([(0,0), (0, 1)]) == get_car_cords("R")
    assert sorted([(1, 0), (2, 0)]) == get_car_cords("Y")

    # can't move left as car1 is blocked by the board's bounds
    assert not board.move_car("R", MOVE_LEFT)
    assert sorted([(0, 0), (0, 1)]) == get_car_cords("R")

    # can't move car2 up as it's blocked by car1
    assert not board.move_car("Y", MOVE_UP)
    assert sorted([(1, 0), (2, 0)]) == get_car_cords("Y")