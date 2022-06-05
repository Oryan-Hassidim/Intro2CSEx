from typing import Set, List, Tuple
from fifo_queue import Queue


class Snake:
    """
    A snake is a list of tuples representing the positions of its body.
    """
    
    UP = 'Up'
    DOWN = 'Down'
    LEFT = 'Left'
    RIGHT = 'Right'
    Directions = {
        UP: (0, 1),
        DOWN: (0, -1),
        LEFT: (-1, 0),
        RIGHT: (1, 0)
    }

    @staticmethod
    def __add_vectors(vector1, vector2):
        """
        Adds two vectors.
        """
        x1, y1 = vector1
        x2, y2 = vector2
        return x1 + x2, y1 + y2

    def __init__(self, cells, direction):
        """
        Initializes a snake with the given cells and length.
        """
        self.direction = direction
        self.__expand = 0
        self.__cells = Queue(cells)

    def expand(self, count):
        """
        Expands the snake by the given count.
        """
        self.__expand += count

    def __allowed_directions(self) -> Set[str]:
        """
        Returns the allowed directions for the current state of the snake.
        """
        if self.direction in {Snake.UP, Snake.DOWN}:
            return {Snake.LEFT, Snake.RIGHT}
        return {Snake.UP, Snake.DOWN}

    def change_direction(self, direction):
        """
        Changes the direction of the snake.
        """
        if direction in self.__allowed_directions():
            self.direction = direction

    def update(self):
        """
        Updates the snake with one step.
        """
        head = Snake.__add_vectors(self.__cells[0],
                                   Snake.Directions[self.direction])
        self.__cells.add(head)
        if self.__expand > 0:
            self.__expand -= 1
        else:
            self.__cells.pop()

    def cells(self) -> List[Tuple[int, int]]:
        """
        Returns the cells of the snake.
        """
        return self.__cells

    def __repr__(self):
        """
        Returns a string representation of the snake.
        """
        return f"Snake({repr(self.__cells)}, {repr(self.direction)})"
