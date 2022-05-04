import random
import sys

global _game
global _wordchoice
global _word_place
global _games_count
global _points

POINTS_INITIAL = 2
HINT_LENGTH = 4

LETTER = 11
WORD = 21
HINT = 31

ABC = 'abcdefghijklmnopqrstuvwxyz'

_rand = random.Random()
play_again_request = False


def set_seed(a=None):
    """
    Sets a new seed for the random generator. You don't have to use this function, but it may help you in debugging
    Search on Google for more details about the seed of random generator in python, if it interests you.
    :param a: a new seed for the random generator (an integer)
    :return: None
    """
    _rand.seed(a)


def load_words(file='words.txt'):
    print("(LOAD_WORDS)")
    global _games_count, _word_place
    _games_count = 1
    return _wordchoice


def get_random_word(words_list):
    print("(GET_RANDOM_WORD)")
    global _word_place
    _word_place += 1
    return _wordchoice[_word_place]


def get_input():
    return _game.get_input()


def display_state(pattern, wrong_guess_lst, points, msg):
    global _points
    _points = points
    if type(wrong_guess_lst) is list:
        try:
            wrong_guess_lst = sorted(wrong_guess_lst)
        except TypeError:
            pass
    print(f"(DISPLAY_STATE '{pattern}', {wrong_guess_lst}, {points})")
    if points == 0:
        assert _wordchoice[_word_place] in msg,\
            f"The hidden word {_wordchoice[_word_place]} should be " \
            f"displayed. Actual message is '{msg}'."


def show_suggestions(matches):
    print(f"(SHOW_SUGGESTIONS {matches})")


def play_again(msg):
    print("(PLAY_AGAIN)")
    assert str(_games_count) in msg, f"Games count {_games_count} should be " \
                                     f"displayed. Actual message is '{msg}'"
    assert _points == 0 or str(_points) in msg, f"Points state {_points} " \
                                              f"should be " \
                                f"displayed. Actual message is '{msg}'."
    return _game.newgame()


class Game(object):
    def __init__(self, inputs=[], nextgames=0):
        self.nextgames = nextgames
        self.inputs = inputs[::-1]
        self.errs = len(ABC)

    def newgame(self):
        self.nextgames -= 1
        global _games_count
        if _points:
            _games_count += 1
        else:
            _games_count = 1
        return self.nextgames >= 0

    def get_input(self):
        if self.inputs:
            return self.inputs.pop()
        elif self.errs > 0:
            print("(TOO_MANY_INPUTS)")
            self.errs -= 1
            return LETTER, ABC[self.errs]
        else:
            raise Exception('No inputs left. Game should be over already.')
