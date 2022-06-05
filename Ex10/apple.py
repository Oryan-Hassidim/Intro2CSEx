from typing import List, Tuple


class Apple:

    def __init__(self, x, y, points):
        self.position = x, y
        self.points = points
        self.__cells = [(x, y)]

    def update(self):
        pass

    def eat(self):
        return self.points

    def cells(self) -> List[Tuple[int, int]]:
        return self.__cells

    def __repr__(self):
        return f'Apple({self.position}, {self.points})'
