from dataclasses import dataclass
from typing import List, Optional, Dict, Tuple

from model import Model, GameObject, Snake, Apple, Bomb


@dataclass
class _View:
    cells: Dict[Tuple[int, int], str]
    score: int
    game_over: bool


class View:
    """
    class to transform model to view.
    """

    def __init__(self):
        self._view = _View(cells={}, score=0, game_over=False)

    @staticmethod
    def _less_than(vec1: Tuple[int, int], vec2: Tuple[int, int]) -> bool:
        """
        returns true if vec1 is less than vec2
        """
        return vec1[0] < vec2[0] and vec1[1] < vec2[1]

    @staticmethod
    def object_layer(object: GameObject) -> int:
        """
        Return the layer of the object.
        """
        if isinstance(object, Snake):
            return 2
        if isinstance(object, Apple):
            return 1
        if isinstance(object, Bomb):
            return 3
        return 0

    @staticmethod
    def map_color(object: GameObject) -> Optional[str]:
        """
        Return the color of the object.
        """
        if isinstance(object, Snake):
            return "black"
        if isinstance(object, Apple):
            return "green"
        if isinstance(object, Bomb):
            return "red" if object.status() == Bomb.LIVE else "orange"
        return None

    def get_view(self, model: Model) -> _View:
        """
        takes a model as parameter and returns a view.
        """
        cells = self._view.cells
        cells.clear()
        for cell, obj in model.cells():
            if not (View._less_than(cell, model.size) and View._less_than((-1, -1), cell)):
                continue
            if cell in cells:
                cells[cell] = max(cells[cell], obj, key=View.object_layer)
            else:
                cells[cell] = obj
        for cell in cells:
            cells[cell] = View.map_color(cells[cell])
        self._view.score = model.score
        self._view.game_over = model.game_over
        return self._view
