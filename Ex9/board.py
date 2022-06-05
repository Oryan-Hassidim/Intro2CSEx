#################################################################################
# FILE: board.py
# WRITER: Oryan Hassidim , oryan.hassidim , 319131579
# EXERCISE: Intro2cs2 ex9 2021-2022
# DESCRIPTION: Board class for rush-hour game.
# NOTES:
#################################################################################

from typing import Tuple, List, Optional, Dict, Any

Coordinates = Tuple[int, int]
Orientation = int  # Literal[0, 1]
Movekey = str  # Literal['u', 'd', 'r', 'l']


class Board:
    """
    Game object of single board for rush-hour game.
    """
    EMPTY_STR = "\033[47m- \033[0m"
    TARGET_STR = "\033[47;90m**\033[0m"
    TARGET_CELL = 3, 7
    # console colors for windows console.
    # https://docs.microsoft.com/en-us/windows/console/console-virtual-terminal-sequences#text-formatting
    COLORS = {
        'Y': "\033[103;30mY \033[0m",
        'B': "\033[44;37mB \033[0m",
        'O': "\033[43;30mO \033[0m",
        'W': "\033[107;30mW \033[0m",
        'G': "\033[42;30mG \033[0m",
        'R': "\033[41;30mR \033[0m"
    }

    def __init__(self):
        # implement your code and erase the "pass"
        # Note that this function is required in your Board implementation.
        # However, is not part of the API for general board types.
        board = {}
        for i in range(7):
            for j in range(7):
                board[i, j] = None
        board[Board.TARGET_CELL] = None
        self.__board = board
        self.__cars = {}

    def __format_cell(self, i, j):
        """
        Return the formatted string representation of the cell at coordinates (i, j).
        """
        cell = self.__board[i, j]
        if cell is None:
            return Board.TARGET_STR if (i, j) == self.target_location() else Board.EMPTY_STR
        else:
            return Board.COLORS.get(cell.get_name(), f"{cell.get_name():<2}")

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        res = ""
        res += "\n".join("".join(self.__format_cell(i, j)
                                 for j in range(7))
                         for i in range(4))
        res += (self.__format_cell(3, 7)) + "\n"
        res += "\n".join("".join(self.__format_cell(i, j)
                                 for j in range(7))
                         for i in range(4, 7))
        return res

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        # In this board, returns a list containing the cells in the square
        # from (0,0) to (6,6) and the target cell (3,7)
        return list(self.__board.keys())

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name, movekey, description) 
                 representing legal moves
        """
        # From the provided example car_config.json file, the return value could be
        #[('O','d',"some description"),('R','r',"some description"),('O','u',"some description")]
        board = self.__board
        return [(car.get_name(), movkey, description)
                for car in self.__cars.values()
                for movkey, description in car.possible_moves().items()
                if all((i, j) in board
                       and board[i, j] is None
                       for i, j in car.movement_requirements(movkey))]

    def target_location(self):
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """
        # In this board, returns (3,7)
        return Board.TARGET_CELL

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        # implement your code and erase the "pass"
        if coordinate in self.__board and self.__board[coordinate] is not None:
            return self.__board[coordinate].get_name()
        return None

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        # Remember to consider all the reasons adding a car can fail.
        # You may assume the car is a legal car object following the API.
        # implement your code and erase the "pass"
        board = self.__board
        name = car.get_name()
        if name in self.__cars:
            return False
        if not all(coor in board
                   and board[coor] is None
                   for coor in car.car_coordinates()):
            return False
        self.__cars[name] = car
        for coor in car.car_coordinates():
            board[coor] = car
        return True

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        # implement your code and erase the "pass"
        if name not in self.__cars:
            return False
        car = self.__cars[name]
        if movekey not in car.possible_moves():
            return False
        if not all(coor in self.__board
                   and self.__board[coor] is None
                   for coor in car.movement_requirements(movekey)):
            return False
        for coor in car.car_coordinates():
            self.__board[coor] = None
        res = car.move(movekey)
        for coor in car.car_coordinates():
            self.__board[coor] = car
        return res

    def __repr__(self):
        return f"Board({self.__cars.values()})"
