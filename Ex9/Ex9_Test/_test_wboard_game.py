import sys
import tempfile
import json
import os
from pathlib import Path
from subprocess import Popen, PIPE


class Helper:
    def __init__(self, log=False):
        self._game_py = str(Helper.__find_game_py())
        self._python = sys.executable
        if log:
            print()
            print(f"Using game.py at {self._game_py}")
            print(f"Using python executable at {self._python}")
            print()

    def _run_game_process(self, json_file, input_txt):
        args = [self._python, self._game_py, json_file]
        _, err = Popen(args, universal_newlines=True, stdin=PIPE,
                       stderr=PIPE).communicate(input_txt)

        # check for other errors(e.g compilation errors, type errors) that aren't
        # related to whether the program has finished successfully or not.
        if len(err) > 0 and "EOF" not in err:
            raise Exception(f"There was an unexpected error while running this test:\n"
                            f"Error message from your executing your program:\n\n{err}\n"
                            f"(this is a problem with your code)")
        return err

    def finishes_with_exact_moves(self, car_cfg, moves):

        # first I check that the given moves result in the program finishing
        # successfully
        moves_st = "\n".join(moves)
        err = self._run_game_process(car_cfg, moves_st)
        assert len(err) == 0, "The game should've terminated successfully after being given " \
                              "all valid moves, but instead it expected for more input."

        # Since the process library doesn't know if all standard input has been consumed/processed, I make another
        # test to ensure that we don't win when given less than the needed moves to win.
        if len(moves) == 0:
            return

        not_enough_moves_st = "\n".join(moves[:-1])
        err = self._run_game_process(car_cfg, not_enough_moves_st)
        assert "EOF" in err, "When providing less than the exact moves for victory, the game should've " \
                             "errored(as it should expect for more input), but it has terminated successfully " \
                             "as if we have won."

    def fails_with_given_moves(self, car_cfg, moves):
        moves_st = "\n".join(moves)
        err = self._run_game_process(car_cfg, moves_st)
        # we expect an EOF error as we interrupted the process while it should've
        # waited for more input()
        assert "EOF" in err, "The game has terminated successfully despite not giving "\
                             "it enough moves to win! It should've expected more input"

    @staticmethod
    def __find_game_py():
        return "game.py"


def test_ensure_tests_configured_corrrectly():
    _test_helper = Helper(log=True)


def create_car_config(cars_dict):
    with tempfile.NamedTemporaryFile(delete=False) as file:
        file.write(bytes(json.dumps(cars_dict), 'UTF-8'))
        return file.name


def test_valid_simple():
    source_path = Path(__file__).resolve()
    source_dir = source_path.parent
    if os.getcwd() != source_dir:
        os.chdir(source_dir)
    cars = {
        "R": [2, [0, 1], 1],
        "Y": [2, [2, 2], 0]
    }

    cfg_file = create_car_config(cars)
    test_helper = Helper()

    test_helper.finishes_with_exact_moves(
        cfg_file, ["R,l", "O,u"] + ["R,r"] * 3)
    test_helper.fails_with_given_moves(cfg_file, ["O,u"] + ["R,r"] * 1)
    # automatic win
    cars = {
        "R": [4, [0, 1], 1]
    }
    cfg_file = create_car_config(cars)
    test_helper.finishes_with_exact_moves(cfg_file, [])
