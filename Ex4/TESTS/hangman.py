#############################################################
# FILE : hangman.py
# WRITER : Oryan Hassidim , oryan.hassidim , 319131579
# EXERCISE : intro2cs2 Ex4 2022
# DESCRIPTION: Hangman Game.
# STUDENTS I DISCUSSED THE EXERCISE WITH: --
# WEB PAGES I USED:
# NOTES:
#############################################################

from re import match
from hangman_helper import *


WELCOME_MESSAGE = "Welcome to Hangman!"
WIN_MESSAGE = """You won! Your score is {}.

WIN     WIN     WIN    WIN    WIN     WIN
 WIN   WIWIN   WIN     WIN    WININ   WIN
  WIN WIN WIN WIN      WIN    WIN WIN WIN
   WININ   WININ       WIN    WIN   WIWIN
    WIN     WIN        WIN    WIN     WIN
"""
LOSE_MESSAGE = "You lost! The word was: {}"
SINGLE_LETTER_MESSAGE = "You must enter a single letter."
ALREADY_GUESSED_MESSAGE = "You have already guessed this letter."
CORRECT_LETTER_GUESS_MESSAGE = "Correct Guess!, {} times in the word."
WRONG_GUESS_MESSAGE = "Wrong Guess!"
HINT_OK_MESSAGE = "What now?"
HINT_NOT_OK_MESSAGE = "Why did you do that?"
PLAY_AGAIN_MESSAGE = """You played {} games.
You have now {} scores.
Do you want to play again?"""
GAME_OVER_MESSAGE = """You played {} games.
You have now {} scores.
GAME OVER!
Do you want start round again?"""


def update_word_pattern(word, pattern, letter):
    """
    Takes in a word, a pattern and a letter.
    Returns a new pattern with the letter in the word
    in the right place.
    """
    new_pattern = ""
    for i, l in enumerate(word):
        if l == letter:
            new_pattern += letter
        else:
            new_pattern += pattern[i]
    return new_pattern


def filter_words_list(words, pattern, wrong_guess_lst):
    """
    Takes in a list of words and a pattern.
    Returns a list of words that match the pattern.
    """
    regex_pattern = "".join(wrong_guess_lst + list(set(pattern.replace("_", ""))))
    regex_pattern = f"[^{regex_pattern}]" if regex_pattern != "" else "."
    regex_pattern = pattern.replace("_", regex_pattern)
    return [
        word
        for word in words
        if len(word) == len(pattern) and match(regex_pattern, word)
    ]


def run_single_game(words_list, score):
    """
    Takes in a list of words and a score.
    Returns the score of the game.
    """

    whole_word = get_random_word(words_list)
    pattern = "_" * len(whole_word)
    wronk_letters = []

    def letter(value):
        nonlocal score
        nonlocal pattern
        nonlocal wronk_letters
        nonlocal whole_word

        if len(value) != 1 or not "a" <= value <= "z":
            return SINGLE_LETTER_MESSAGE
        if value in wronk_letters or value in pattern:
            return ALREADY_GUESSED_MESSAGE
        score -= 1
        if value in whole_word:
            pattern = update_word_pattern(whole_word, pattern, value)
            instances = whole_word.count(value)
            score += (instances * (instances + 1)) // 2
            return CORRECT_LETTER_GUESS_MESSAGE.format(instances)
        wronk_letters.append(value)
        return WRONG_GUESS_MESSAGE

    def word(value):
        nonlocal score
        nonlocal pattern
        nonlocal whole_word

        score -= 1
        if value == whole_word:
            additional_letters = pattern.count("_")
            score += (additional_letters * (additional_letters + 1)) // 2
            pattern = whole_word
            return WIN_MESSAGE
        return WRONG_GUESS_MESSAGE

    def hint(_):
        nonlocal score
        nonlocal pattern
        nonlocal wronk_letters
        nonlocal whole_word

        score -= 1

        all_hints = filter_words_list(words_list, pattern, wronk_letters)
        n = len(all_hints)

        hints = []

        if n > HINT_LENGTH:
            for i in range(HINT_LENGTH):
                hints.append(all_hints[(i * n) // HINT_LENGTH])
        else:
            hints = all_hints
        show_suggestions(hints)
        return HINT_OK_MESSAGE if score > 0 else HINT_NOT_OK_MESSAGE

    options = {LETTER: letter, WORD: word, HINT: hint}

    message = WELCOME_MESSAGE

    while score > 0 and pattern != whole_word:
        display_state(pattern, wronk_letters, score, message)
        option, value = get_input()
        message = options[option](value)

    if pattern == whole_word:
        display_state(pattern, wronk_letters, score, WIN_MESSAGE.format(score))
    else:
        display_state(pattern, wronk_letters, score, LOSE_MESSAGE.format(whole_word))

    return score


def main():
    """
    Runs the game until the player wants to quit.
    """

    words = load_words()
    games = 0
    score = POINTS_INITIAL

    while score > 0:
        games += 1
        score = run_single_game(words, score)

        if score > 0 and not play_again(PLAY_AGAIN_MESSAGE.format(games, score)):
            score = 0
        elif score == 0 and play_again(GAME_OVER_MESSAGE.format(games, score)):
            games = 0
            score = POINTS_INITIAL


if __name__ == "__main__":
    print(filter_words_list(["abc", "aef", "ggg"], "___", []))
    main()
