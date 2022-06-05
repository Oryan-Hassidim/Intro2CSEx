from typing import List, Tuple, Generator


class Bomb:

    LIVE = 0b1
    EXPLODED = 0b10
    DISPOSED = 0b100

    @staticmethod
    def __calculate_blast(
        r: int, position: Tuple[int, int]
    ) -> Generator[Tuple[int, int], None, None]:
        if r == 0:
            yield position
            return
        x, y = position
        for i in range(r):
            j = r - i
            yield x + i, y + j
            yield x + j, y - i
            yield x - i, y - j
            yield x - j, y + i

    def __init__(self, x, y, radius, life):
        self.position = x, y
        self.life = life
        self.radius = radius
        self.__cells = []

    def status(self):
        if self.life < -self.radius:
            return Bomb.DISPOSED
        if self.life <= 0:
            return Bomb.EXPLODED
        return self.LIVE

    def update(self):
        self.life -= 1

    def cells(self):
        if self.status() == Bomb.LIVE:
            if len(self.__cells) != 1:
                self.__cells.clear()
                self.__cells.append(self.position)
            return self.__cells
        # If Bomb exploded, calculate and return blast
        if self.status() == Bomb.EXPLODED:
            r = -self.life  # Blast Radius
            if len(self.__cells) < max(1, 4*r):
                self.__cells.clear()
                self.__cells.extend(Bomb.__calculate_blast(r, self.position))
            return self.__cells
        return []

    def __repr__(self):
        return f'Bomb({self.position}, {self.life}, {self.radius})'
