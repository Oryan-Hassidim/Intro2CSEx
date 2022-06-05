from typing import Callable, List, Tuple, Optional

from model import Model, GameObject, Snake, Apple, Bomb


class Game:
    """
    class to create and manage the game with Model class.
    """

    def __init__(self, width: int, height: int,
                 get_random_apple_data: Callable[[], Tuple[int, int, int]],
                 get_random_bomb_data: Callable[[], Tuple[int, int, int, int]],
                 num_apples: int, num_bombs: int, snake_expand: int):
        self.width = width
        self.height = height
        self.get_random_apple_data = get_random_apple_data  # (x,y,score)
        self.get_random_bomb_data = get_random_bomb_data  # (x,y,radius,time)
        self.num_apples = num_apples
        self.num_bombs = num_bombs
        self.snake_expand = snake_expand
        self.cells = {(x, y) for x in range(width) for y in range(height)}

    def initial_model(self) -> Model:
        """
        returns the initial model of this game.
        """
        size = (self.width, self.height)
        x, y = self.width // 2, self.height // 2
        snake = Snake([(x, y-2), (x, y-1), (x, y)], Snake.UP)
        model = Model(size, 0, snake, [], [])
        for _ in range(self.num_bombs):
            model.new_bomb(self.__new_bomb(model))
        for _ in range(self.num_apples):
            new_apple = self.__new_apple(model)
            if new_apple:
                model.new_apple(new_apple)
        if len(model.apples) == 0:
            model.game_over = True
        return model

    def __new_apple(self, model: Model) -> Optional[Apple]:
        """
        Generate a new apple in an empty cell.
        """
        if sum(len(obj.cells()) for obj in model.get_objects()) == len(self.cells):
            return None
        apple = None
        while not apple:
            x, y, points = self.get_random_apple_data()
            if model.is_free(x, y):
                apple = Apple(x, y, points)
        return apple

    def __new_bomb(self, model: Model) -> Bomb:
        """
        Generate a new bomb in an empty cell.
        """
        bomb = None
        while not bomb:
            random_bomb_data = self.get_random_bomb_data()
            x, y, _, _ = random_bomb_data
            if model.is_free(x, y):
                bomb = Bomb(*random_bomb_data)
        return bomb

    def __handle_remove_and_create(self, model: Model,
                                   remove_lst: List[GameObject]):
        """
        Remove the objects in the remove_lst from the model and create new.
        """
        for obj in remove_lst:
            model.remove_object(obj)
            if isinstance(obj, Bomb):
                model.new_bomb(self.__new_bomb(model))
                continue
            # it is an apple
            new_apple = self.__new_apple(model)
            if new_apple:
                model.new_apple(new_apple)
            elif len(model.apples) == 0:
                model.game_over = True

    def __snake_collisions_check(self, model: Model) -> List[GameObject]:
        """
        Check collisions between the snake and the objects in the cells.
        """
        head = model.snake.cells()[0]
        x, y = head
        remove_lst = []
        if head not in self.cells:
            model.game_over = True
            return remove_lst
        contains = list(model.cell_content(x, y))
        snake_count = 0
        if len(contains) > 1:
            for obj in contains:
                if obj is model.snake:
                    snake_count += 1
                if snake_count > 1 or isinstance(obj, Bomb):
                    model.game_over = True
                elif isinstance(obj, Apple):
                    model.raise_score(obj.eat())
                    model.snake.expand(self.snake_expand)
                    remove_lst.append(obj)
        return remove_lst

    def __blast_collisions_check(self, model: Model, bomb: Bomb) -> List[GameObject]:
        """
        Check collisions between blast and snake or apple.
        """
        bomb_positions = bomb.cells()
        remove_lst = []
        for x, y in bomb_positions:
            contains = list(model.cell_content(x, y))
            if len(contains) > 1:
                for obj in contains:
                    if isinstance(obj, Snake):
                        model.game_over = True
                    elif isinstance(obj, Apple):
                        remove_lst.append(obj)
        return remove_lst

    def update(self, model: Model, key: Optional[str]) -> Model:
        """
        main function of the game! returns an updated model.
        """
        remove_lst = []
        model.snake.change_direction(key)
        model.snake.update()
        # Check collisions
        remove_lst.extend(self.__snake_collisions_check(model))
        # Maintain 3 living bombs and discard the dead ones. Update blast
        for bomb in model.bombs:
            if not model.game_over:
                bomb.update()
            bomb_status = bomb.status()
            if bomb_status == Bomb.DISPOSED:
                remove_lst.insert(0, bomb)
            elif bomb_status == Bomb.EXPLODED:
                remove_lst.extend(self.__blast_collisions_check(model, bomb))
            self.__handle_remove_and_create(model, remove_lst)
        return model
