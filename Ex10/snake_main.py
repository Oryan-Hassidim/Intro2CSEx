import game_parameters
from game_display import GameDisplay

from game import Game
from view import View

NUM_APPLES_INIT = 3
NUM_BOMBS_INIT = 1
SNAKE_EXPAND_INIT = 3


#def getCurrentMemoryUsage():
#    '''Memory usage in MB'''
#    import os
#    import psutil
#    return psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2


def main_loop(gd: GameDisplay) -> None:
    game = Game(game_parameters.WIDTH,
                game_parameters.HEIGHT,
                game_parameters.get_random_apple_data,
                game_parameters.get_random_bomb_data,
                NUM_APPLES_INIT,
                NUM_BOMBS_INIT,
                SNAKE_EXPAND_INIT)
    model_to_view = View()

    model = game.initial_model()

    while True:
        view = model_to_view.get_view(model)
        for (x, y), color in view.cells.items():
            gd.draw_cell(x, y, color)
        gd.show_score(view.score)

        gd.end_round()

        if view.game_over:
            return
        key_clicked = gd.get_key_clicked()
        model = game.update(model, key_clicked)
