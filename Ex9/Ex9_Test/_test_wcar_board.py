from board import Board
from car import Car

VERTICAL = 0
HORIZONTAL = 1
MOVE_UP = "u"
MOVE_DOWN = "d"
MOVE_LEFT = "l"
MOVE_RIGHT = "r"


def test_wierd_car():
    board = Board()
    car1 = Car("RR", 2, (0, 0), HORIZONTAL)
    assert board.add_car(car1)

    # can't add same car instance twice
    assert not board.add_car(car1)
    # can't add car with same name
    assert not board.add_car(Car("RR", 2, (5, 5), VERTICAL))

    assert board.cell_content((0, 0)) == "RR"
    assert board.cell_content((0, 1)) == "RR"
    assert board.cell_content((5, 5)) is None

    assert board.possible_moves() == [("RR", "r", "two steps right")]
    assert board.move_car("RR", "r")
    assert board.cell_content((0, 0)) is None
    assert board.cell_content((0, 1)) is None
    assert board.cell_content((0, 2)) == "RR"
    assert board.cell_content((0, 3)) == "RR"
    
    assert board.add_car(Car("P",2,(0,5), HORIZONTAL))
    assert board.possible_moves() == []
    assert not board.move_car("RR", "r")
    assert not board.move_car("P", "r")
    assert not board.move_car("P", "l")
