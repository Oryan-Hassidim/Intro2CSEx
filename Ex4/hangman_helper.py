import random

POINTS_INITIAL = 10
HINT_LENGTH = 3

LETTER = 1
WORD = 2
HINT = 3

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
    """
    Loads a list of 58110 words from words.txt file
    :param file: The file of words
    :return: A list containing all the words from the file
    """
    words = []
    f_words = open(file)
    for line in f_words:
        word = line.strip()
        if(word.isalpha()):
            words.append(line.strip())
    f_words.close()
    return words


def get_random_word(words_list):
    """
    Gets a random word out of the given list of words
    :param words_list: A list of words
    :return: Some random word from the list
    """
    return _rand.choice(words_list)


def get_input():
    """
    Asks the player for his input. He can guess a letter, a word of asks for a hint.
    :return: a tuple of 2 values:
              if the player guesses a letter, returns (LETTER, letter)
              if the player guesses a word, returns (WORD, word)
              if the player asks for a hint, returns (HINT, None)
    """
    choice = input("Enter '!*' to guess a word (replace '*' with your guess), enter '?' to ask for a hint: ")
    if choice == '?':
        return HINT, None
    elif choice and choice[0]=='!':
        return WORD, choice[1:]
    return LETTER, choice


def display_state(pattern, wrong_guess_lst, points, msg):
    """
    Prints the current state of the game to the player
    :param pattern: the current pattern
    :param wrong_guess_lst: the current list of wrongs guesses
    :param points: the current amount of points the player have
    :param msg: some additional message to the player
    :return: None
    """
    print('Wrong guesses:',wrong_guess_lst)
    print('Current pattern:', " ".join(pattern))
    print('Current points:',points)
    print(msg)


def show_suggestions(matches):
    """
    Prints a list of suggestions to the player
    :param matches: a list of words
    :return: None
    """
    print('Some possible words are:')
    print(matches)


def play_again(msg):
    """
    Prints the message to the player, and gets input from him if she wants to play again.
    :param msg: The message printed to the player
    :return: True if she wants to play again, False otherwise
    """
    print(msg)
    print("Enter 'Y' or 'y' for YES, 'N' or 'n' for NO:")
    while True:
        choice = input()
        if choice and choice[0] in 'yY':
            return True
        if choice and choice[0] in 'nN':
            return False
