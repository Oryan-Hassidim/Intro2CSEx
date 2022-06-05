from typing import Generator, Iterable, Union, Tuple, List

from snake import Snake
from apple import Apple
from bomb import Bomb

GameObject = Union[Snake, Apple, Bomb]


class Model:
    def __init__(self, size: Tuple[int, int], score: int,
                 snake: Snake, apples: List[Apple], bombs: List[Bomb]):
        self.size = size
        self.score = score
        self.snake = snake
        self.apples = apples
        self.bombs = bombs
        self.game_over = False

    def new_apple(self, apple: Apple):
        self.apples.append(apple)

    def new_bomb(self, bomb: Bomb):
        self.bombs.append(bomb)

    def remove_object(self, obj: GameObject):
        if isinstance(obj, Bomb):
            self.bombs.remove(obj)
        elif isinstance(obj, Apple):
            self.apples.remove(obj)

    def raise_score(self, score: int):
        self.score += score

    def get_objects(self):
        yield self.snake
        yield from self.apples
        yield from self.bombs

    def cells(self):
        yield from (((x, y), obj)
                    for obj in self.get_objects()
                    for x, y in obj.cells())

    def cell_content(self, x, y) -> Generator[GameObject, None, None]:
        yield from (obj
                    for obj in self.get_objects()
                    for i, j in obj.cells()
                    if (i, j) == (x, y))

    def is_free(self, x, y):
        for _ in self.cell_content(x, y):
            return False
        return True

    def game_over(self):
        self.game_over = True

    def __repr__(self):
        return f'score: {self.score} snake: {repr(self.snake)} apples: ' \
               f'{repr(self.apples)} bombs: {repr(self.bombs)} '
