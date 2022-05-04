from autotest import TestSet

import testrunners

import sys
from importlib import import_module
from io import StringIO

from hangman_helper import *


def setup_runner(modulename, fname, args=[], kwargs={}, options={}, tname=''):
    try:
        module = import_module(modulename)
        func = getattr(module, fname)
        _stdout = sys.stdout
        tmpout = StringIO()
        sys.stdout = tmpout
        if 'setup' in options:
            setupopt = options.pop('setup')
            import hangman_helper
            game_obj, word_chioce = setupopt
            hangman_helper._game = game_obj
            hangman_helper._wordchoice = word_chioce
            hangman_helper._word_place = -1

        retval = func(*args, **kwargs)
        if 'output' in options:
            if options['output'] and retval is not None:
                return "wrong", 'return value should be None'
            else:
                return None, tmpout.getvalue()
        else:
            return None, retval

    finally:
        sys.stdout = _stdout


defaults = {'modulename': 'hangman',
            'runner': testrunners.functionname_runner,
            'ans': [True],
            }

words_list = ['abc', 'aef', 'ggg']

gameseqout = '''F
R
('___', [], 2)
('a__', [], 2)
('a_c', [], 2)
('abc', [], 2)
P
R
('___', [], 2)
('___', ['a'], 1)
('___', ['a', 'c'], 0)
P
'''

cases = {'updatepattern': {'fname': 'update_word_pattern',
                           },
         'singlegame': {'fname': 'run_single_game',
                        },
         'main': {'fname': 'main',
                  'runner': setup_runner,
                  'options': {'setup': 3},
                  'args': [],
                  'ans': [gameseqout],
                  },
         'filter': {'fname': 'filter_words_list',
                    },
         }

update_word_pattern_cases = {
    'update_word_pattern_' + name: {
        'fname': 'update_word_pattern',
        'runner': setup_runner,
        'args': args,
        'ans': [ans]
    } for name, (args, ans) in {
        'single_letter': (['abc', '___', 'a'], 'a__'),
        'multiple_letters': (['abcabcabc', '_________', 'a'], 'a__a__a__'),
        'complete_word': (['abc', 'a_c', 'b'], 'abc'),
        'wrong_letter': (['abc', '___', 'd'], '___'),
    }.items()
}

filter_words_list_cases = {
    'filter_words_list_' + name: {
        'fname': 'filter_words_list',
        'runner': setup_runner,
        'args': args,
        'ans': [ans]
    } for name, (args, ans) in {
        'length': ([['a', 'ab', '', 'ac', 'abc'], '__', []], ['ab', 'ac']),
        'pattern_letters': ([['abc', 'abd', 'bcd'], '_b_', []],
                            ['abc', 'abd']),
        'additional_pattern_letters': ([['abb', 'abc', 'abd'], '_b_', []],
                                       ['abc', 'abd']),
        'blacklist_letters': ([['abb', 'abc', 'dbd'], '_b_', ['a']],
                              ['dbd']),
    }.items()
}

run_single_game_outputs_cases = {
    'run_single_game_outputs_' + name: {
        'fname': 'run_single_game',
        'runner': setup_runner,
        'args': args,
        'ans': [ans],
        'options': {'setup': (game_obj, args[0]), 'output': None}
    } for name, (args, game_obj, ans) in {
        'capital_letter': (
            [['aaa'], 1],
            Game([(LETTER, 'G'), (LETTER, 'g')], 1),
            "(GET_RANDOM_WORD)\n"
            "(DISPLAY_STATE '___', [], 1)\n"
            "(DISPLAY_STATE '___', [], 1)\n"
            "(DISPLAY_STATE '___', ['g'], 0)\n"
        ),
        'other_char': (
            [['aaa'], 1],
            Game([(LETTER, '!'), (LETTER, 'g')], 1),
            "(GET_RANDOM_WORD)\n"
            "(DISPLAY_STATE '___', [], 1)\n"
            "(DISPLAY_STATE '___', [], 1)\n"
            "(DISPLAY_STATE '___', ['g'], 0)\n"
        ),
        'multiple_chars': (
            [['aaa'], 1],
            Game([(LETTER, 'gg'), (LETTER, 'g')], 1),
            "(GET_RANDOM_WORD)\n"
            "(DISPLAY_STATE '___', [], 1)\n"
            "(DISPLAY_STATE '___', [], 1)\n"
            "(DISPLAY_STATE '___', ['g'], 0)\n"
        ),
        'letter_again': (
            [['aaa'], 2],
            Game([(LETTER, 'g'), (LETTER, 'g'), (LETTER, 'h')], 1),
            "(GET_RANDOM_WORD)\n"
            "(DISPLAY_STATE '___', [], 2)\n"
            "(DISPLAY_STATE '___', ['g'], 1)\n"
            "(DISPLAY_STATE '___', ['g'], 1)\n"
            "(DISPLAY_STATE '___', ['g', 'h'], 0)\n"
        ),
        'wrong_letter': (
            [['aaa'], 1],
            Game([(LETTER, 'g')], 1),
            "(GET_RANDOM_WORD)\n"
            "(DISPLAY_STATE '___', [], 1)\n"
            "(DISPLAY_STATE '___', ['g'], 0)\n"
        ),
        'correct_letter': (
            [['abc'], 1],
            Game([(LETTER, 'a'), (LETTER, 'g')], 1),
            "(GET_RANDOM_WORD)\n"
            "(DISPLAY_STATE '___', [], 1)\n"
            "(DISPLAY_STATE 'a__', [], 1)\n"
            "(DISPLAY_STATE 'a__', ['g'], 0)\n"
        ),
        'correct_multi_letter': (
            [['aba'], 1],
            Game([(LETTER, 'a'),
                  (LETTER, 'g'),
                  (LETTER, 'h'),
                  (LETTER, 'i')], 1),
            "(GET_RANDOM_WORD)\n"
            "(DISPLAY_STATE '___', [], 1)\n"
            "(DISPLAY_STATE 'a_a', [], 3)\n"
            "(DISPLAY_STATE 'a_a', ['g'], 2)\n"
            "(DISPLAY_STATE 'a_a', ['g', 'h'], 1)\n"
            "(DISPLAY_STATE 'a_a', ['g', 'h', 'i'], 0)\n"
        ),
        'correct_multi_multi_letter': (
            [['abacdaefa'], 1],
            Game([(LETTER, 'a'),
                  (LETTER, 'g'),
                  (LETTER, 'h'),
                  (LETTER, 'i'),
                  (LETTER, 'j'),
                  (LETTER, 'k'),
                  (LETTER, 'l'),
                  (LETTER, 'm'),
                  (LETTER, 'n'),
                  (LETTER, 'o'),
                  (LETTER, 'p')], 1),
            "(GET_RANDOM_WORD)\n"
            "(DISPLAY_STATE '_________', [], 1)\n"
            "(DISPLAY_STATE 'a_a__a__a', [], 10)\n"
            "(DISPLAY_STATE 'a_a__a__a', ['g'], 9)\n"
            "(DISPLAY_STATE 'a_a__a__a', ['g', 'h'], 8)\n"
            "(DISPLAY_STATE 'a_a__a__a', ['g', 'h', 'i'], 7)\n"
            "(DISPLAY_STATE 'a_a__a__a', ['g', 'h', 'i', 'j'], 6)\n"
            "(DISPLAY_STATE 'a_a__a__a', ['g', 'h', 'i', 'j', 'k'], 5)\n"
            "(DISPLAY_STATE 'a_a__a__a', ['g', 'h', 'i', 'j', 'k', 'l'], 4)\n"
            "(DISPLAY_STATE 'a_a__a__a', ['g', 'h', 'i', 'j', 'k', 'l', 'm'], 3)\n"
            "(DISPLAY_STATE 'a_a__a__a', ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'], 2)\n"
            "(DISPLAY_STATE 'a_a__a__a', ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'], 1)\n"
            "(DISPLAY_STATE 'a_a__a__a', ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'], 0)\n"
        ),
        'correct_two_letters': (
            [['abc'], 1],
            Game([(LETTER, 'a'), (LETTER, 'c'), (LETTER, 'g')], 1),
            "(GET_RANDOM_WORD)\n"
            "(DISPLAY_STATE '___', [], 1)\n"
            "(DISPLAY_STATE 'a__', [], 1)\n"
            "(DISPLAY_STATE 'a_c', [], 1)\n"
            "(DISPLAY_STATE 'a_c', ['g'], 0)\n"
        ),
        'correct_word': (
            [['abc'], 1],
            Game([(WORD, 'abc')], 1),
            "(GET_RANDOM_WORD)\n"
            "(DISPLAY_STATE '___', [], 1)\n"
            "(DISPLAY_STATE 'abc', [], 6)\n"
        ),
        'correct_word_with_repeats': (
            [['abca'], 1],
            Game([(WORD, 'abca')], 1),
            "(GET_RANDOM_WORD)\n"
            "(DISPLAY_STATE '____', [], 1)\n"
            "(DISPLAY_STATE 'abca', [], 10)\n"
        ),
        'correct_word_with_letters': (
            [['abca'], 1],
            Game([(LETTER, 'a'), (WORD, 'abca')], 1),
            "(GET_RANDOM_WORD)\n"
            "(DISPLAY_STATE '____', [], 1)\n"
            "(DISPLAY_STATE 'a__a', [], 3)\n"
            "(DISPLAY_STATE 'abca', [], 5)\n"
        ),
        'wrong_word': (
            [['abc'], 1],
            Game([(WORD, 'aaa')], 1),
            "(GET_RANDOM_WORD)\n"
            "(DISPLAY_STATE '___', [], 1)\n"
            "(DISPLAY_STATE '___', [], 0)\n"
        ),
        'hint': (
            [['abc', 'aef', 'ggg'], 1],
            Game([(HINT, None)], 1),
            "(GET_RANDOM_WORD)\n"
            "(DISPLAY_STATE '___', [], 1)\n"
            "(SHOW_SUGGESTIONS ['abc', 'aef', 'ggg'])\n"
            "(DISPLAY_STATE '___', [], 0)\n"
        ),
        'hints_places': (
            [['abc', 'aef', 'ggg', 'bbc', 'bef', 'bgg', 'cbc', 'cef', 'cgg',
              'dbc', 'def', 'dgg', 'ebc', 'eef', 'egg'],
             1],
            Game([(HINT, None)], 1),
            "(GET_RANDOM_WORD)\n"
            "(DISPLAY_STATE '___', [], 1)\n"
            "(SHOW_SUGGESTIONS ['abc', 'bbc', 'cef', 'dgg'])\n"
            "(DISPLAY_STATE '___', [], 0)\n"
        ),
    }.items()
}

main_cases = {
    'main_' + name: {
        'fname': 'main',
        'runner': setup_runner,
        'ans': [ans],
        'options': {'setup': (game_obj, words_list), 'output': True}
    } for name, (words_list, game_obj, ans) in {
        'initial_points': (
            ['abc'],
            Game([(LETTER, 'g'), (LETTER, 'h')], 0),
            "(LOAD_WORDS)\n"
            "(GET_RANDOM_WORD)\n"
            "(DISPLAY_STATE '___', [], 2)\n"
            "(DISPLAY_STATE '___', ['g'], 1)\n"
            "(DISPLAY_STATE '___', ['g', 'h'], 0)\n"
            "(PLAY_AGAIN)\n"
        ),
        'win': (
            ['abc'],
            Game([(WORD, 'abc')], 0),
            "(LOAD_WORDS)\n"
            "(GET_RANDOM_WORD)\n"
            "(DISPLAY_STATE '___', [], 2)\n"
            "(DISPLAY_STATE 'abc', [], 7)\n"
            "(PLAY_AGAIN)\n"
        ),
        'wins': (
            ['abc', 'def'],
            Game([(WORD, 'abc'), (WORD, 'def')], 1),
            "(LOAD_WORDS)\n"
            "(GET_RANDOM_WORD)\n"
            "(DISPLAY_STATE '___', [], 2)\n"
            "(DISPLAY_STATE 'abc', [], 7)\n"
            "(PLAY_AGAIN)\n"
            "(GET_RANDOM_WORD)\n"
            "(DISPLAY_STATE '___', [], 7)\n"
            "(DISPLAY_STATE 'def', [], 12)\n"
            "(PLAY_AGAIN)\n"
        ),
        'lose': (
            ['abc', 'def', 'ghi'],
            Game([(WORD, 'abc'),
                  (LETTER, 'j'),
                  (LETTER, 'k'),
                  (LETTER, 'l'),
                  (LETTER, 'm'),
                  (LETTER, 'n'),
                  (LETTER, 'o'),
                  (LETTER, 'p'),
                  ], 1),
            "(LOAD_WORDS)\n"
            "(GET_RANDOM_WORD)\n"
            "(DISPLAY_STATE '___', [], 2)\n"
            "(DISPLAY_STATE 'abc', [], 7)\n"
            "(PLAY_AGAIN)\n"
            "(GET_RANDOM_WORD)\n"
            "(DISPLAY_STATE '___', [], 7)\n"
            "(DISPLAY_STATE '___', ['j'], 6)\n"
            "(DISPLAY_STATE '___', ['j', 'k'], 5)\n"
            "(DISPLAY_STATE '___', ['j', 'k', 'l'], 4)\n"
            "(DISPLAY_STATE '___', ['j', 'k', 'l', 'm'], 3)\n"
            "(DISPLAY_STATE '___', ['j', 'k', 'l', 'm', 'n'], 2)\n"
            "(DISPLAY_STATE '___', ['j', 'k', 'l', 'm', 'n', 'o'], 1)\n"
            "(DISPLAY_STATE '___', ['j', 'k', 'l', 'm', 'n', 'o', 'p'], 0)\n"
            "(PLAY_AGAIN)\n"
        ),
        'lose_twice': (
            ['abc', 'def', 'ghi'],
            Game([(LETTER, 'j'),
                  (LETTER, 'k'),
                  (LETTER, 'l'),
                  (LETTER, 'm'),
                  (LETTER, 'n'),
                  (LETTER, 'o'),
                  (LETTER, 'p'),
                  ], 1),
            "(LOAD_WORDS)\n"
            "(GET_RANDOM_WORD)\n"
            "(DISPLAY_STATE '___', [], 2)\n"
            "(DISPLAY_STATE '___', ['j'], 1)\n"
            "(DISPLAY_STATE '___', ['j', 'k'], 0)\n"
            "(PLAY_AGAIN)\n"
            "(GET_RANDOM_WORD)\n"
            "(DISPLAY_STATE '___', [], 2)\n"
            "(DISPLAY_STATE '___', ['l'], 1)\n"
            "(DISPLAY_STATE '___', ['l', 'm'], 0)\n"
            "(PLAY_AGAIN)\n"
        ),
    }.items()
}

cases = {}
cases.update(update_word_pattern_cases)
cases.update(filter_words_list_cases)
cases.update(run_single_game_outputs_cases)
cases.update(main_cases)

tsets = {'ex4': TestSet({}, cases)}
