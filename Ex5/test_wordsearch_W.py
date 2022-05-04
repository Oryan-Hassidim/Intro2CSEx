###############################################
# updated by Oryan Hassidim
# Oryan.Hassidim@mail.huji.ac.il
# last updated 28/04/2022  20:20
###############################################

import os
import sys
import tempfile
import inspect
from time import perf_counter

import wordsearch
from wordsearch import *

EX_DIR = 'Ex5-Examples'
OUTPUT_FILE = 'output.txt'

    
def test_read_wordlist(capsys):
    words_dict = {
        ("agsgsa", "AGDSR4", "!$#WDS"): "read_wordlist sanity failed.",
        ('123',): "read_wordlist with one line failed.",
        tuple(): "read_wordlist with no lines failed."
    }
    for words, message in words_dict.items():
        words = list(words)
        content = ''.join(map(lambda r: r + '\n', words))
        fd, words_file = tempfile.mkstemp()
        open(words_file, 'w').write(content)
        words2 = read_wordlist(words_file)
        os.close(fd)
        assert words == words2, message + f"\nExpected: " \
                                          f"{words}.\nActual: {words2}."

    captured = capsys.readouterr()
    assert not captured.out and not captured.err, (f"No prints allowed!\nGot: "
                                                   f"out: {captured.out}\n"
                                                   f"err: {captured.err}\n")


def test_read_matrix(capsys):
    words_dict = {
        ("agsgsa", "AGDSR4", "!$#WDS"): "read_matrix sanity failed.",
        ('123',): "read_matrix with one line failed.",
        ('1', '2', '3'): "read_matrix with one letter in line failed.",
        tuple(): "read_matrix with no lines failed."
    }
    for words, message in words_dict.items():
        words = list(map(list, words))
        content = ''.join(map(lambda r: ','.join(r) + '\n', words))
        fd, words_file = tempfile.mkstemp()
        open(words_file, 'w').write(content)
        words2 = read_matrix(words_file)
        os.close(fd)
        assert words == words2, message + f"\nExpected: " \
                                          f"{words}.\nActual: {words2}."

    captured = capsys.readouterr()
    assert not captured.out and not captured.err, (f"No prints allowed!\nGot: "
                                                   f"out: {captured.out}\n"
                                                   f"err: {captured.err}\n")


def test_find_words_wide(capsys):
    start = perf_counter()
    for suffix in ['', '0', 'R', 'C', 'Z']:
        _find_words_wide(suffix)

    captured = capsys.readouterr()
    assert not captured.out and not captured.err, (f"No prints allowed!\nGot: "
                                                   f"out: {captured.out}\n"
                                                   f"err: {captured.err}\n")
    print(f"Time: {perf_counter() - start}")


def test_write_output(capsys):
    for result in [[('a', 2), ('b', 3)], [('a', 2)], []]:
        fd, filename = tempfile.mkstemp()
        write_output(result, filename)
        content = open(filename).read()
        expected = ''.join([','.join(map(str, i)) + '\n' for i in result])
        os.close(fd)
        assert content == expected, f"write_output failed!\n" \
                                    f"Actual: {content}\n" \
                                    f"Expected: {expected}"

    try:
        fd, filename = tempfile.mkstemp()

        result = [('a', 2), ('b', 3)]
        write_output(result, filename)
        content = open(filename).read()
        expected = ''.join([','.join(map(str, i)) + '\n' for i in result])
        assert content == expected, f"write_output failed!\n" \
                                    f"Actual: {content}\n" \
                                    f"Expected: {expected}"

        result = [('a', 3), ('b', 4)]
        write_output(result, filename)
        content = open(filename).read()
        expected = ''.join([','.join(map(str, i)) + '\n' for i in result])
        assert content == expected, f"write_output failed!\n" \
                                    f"Actual: {content}\n" \
                                    f"Expected: {expected}"
    finally:
        os.close(fd)

    captured = capsys.readouterr()
    assert not captured.out and not captured.err, (f"No prints allowed!\nGot: "
                                                   f"out: {captured.out}\n"
                                                   f"err: {captured.err}\n")


def _find_words_wide(suffix):
    directions = [filename[4:-4] for filename
                  in os.listdir(EX_DIR) if
                  filename.startswith('out_')]
    words = read_wordlist(os.path.join(EX_DIR, f'words{suffix}.txt'))
    matrix = read_matrix(os.path.join(EX_DIR, f'matrix{suffix}.txt'))
    for direction in set(directions):
        pairs = find_words(words, matrix, direction)
        actual = sorted(pairs)
        content = open(os.path.join(EX_DIR,
                                    f'out{suffix}_{direction}.txt'),
                       'r').read()
        expected = content[:-1].split('\n') if content else []
        expected = [i.split(',') for i in expected]
        expected = [(i[0], int(i[1])) for i in expected]
        expected = sorted(expected)
        assert actual == expected, f"SUFFIX: {suffix}\n" \
                                   f"words: {words}\n" \
                                   f"matrix: {matrix}\n" \
                                   f"DIRECTION: {direction}\n" \
                                   f"ACTUAL {actual}\n" \
                                   f"EXPECTED: {expected}"
    for direction1 in directions:
        for direction2 in directions:
            for direction3 in directions:
                direction_str = ''.join(set(
                    direction1 + direction2 + direction3))
                pairs = find_words(words, matrix, direction_str)
                actual = sorted(pairs)
                expected_dict = {}
                for direction in direction_str:
                    content = open(
                        os.path.join(EX_DIR, f'out{suffix}_{direction}.txt'
                                     ), 'r').read()
                    partial_exp = content[:-1].split('\n') if content else []
                    for word_count in partial_exp:
                        word, count = word_count.split(',')
                        if word in expected_dict:
                            expected_dict[word] += int(count)
                        else:
                            expected_dict[word] = int(count)
                expected = sorted([(word, count) for word, count in
                                   expected_dict.items()])
                assert actual == expected, f"SUFFIX: {suffix}\n" \
                                           f"words: {words}\n" \
                                           f"matrix: {matrix}\n" \
                                           f"DIRECTION: {direction_str}\n" \
                                           f"ACTUAL {actual}\n" \
                                           f"EXPECTED: {expected}"


def test_main_wide(capsys):
    start = perf_counter()
    directions = [filename[4:-4] for filename
                  in os.listdir(EX_DIR) if
                  filename.startswith('out_')]
    script = inspect.getsource(wordsearch)
    original_argv = sys.argv.copy()
    for direction in directions:
        sys.argv.clear()
        sys.argv.extend([original_argv[0],
                         os.path.join(EX_DIR, "words.txt"),
                         os.path.join(EX_DIR, "matrix.txt"),
                         OUTPUT_FILE,
                         direction])
        __name__ = '__main__'
        ret = exec(script)
        assert not ret, f"Return value of program is {ret} instead "
        f"of 0"
        actual = sorted(open(OUTPUT_FILE).read().split('\n'))
        expected = sorted(open(
            os.path.join(EX_DIR, f'out_{direction}.txt'),
            'r').read().split('\n'))
        assert actual == expected, f"DIRECTION: {direction}\n"\
            f"args: {sys.argv}\n" \
            f"ACTUAL {actual}\n"\
            f"EXPECTED: {expected}"
    for direction1 in directions:
        for direction2 in directions:
            for direction3 in directions:
                direction_str = direction1 + direction2 + direction3
                sys.argv.clear()
                sys.argv.extend([original_argv[0],
                                 os.path.join(EX_DIR, "words.txt"),
                                 os.path.join(EX_DIR, "matrix.txt"),
                                 OUTPUT_FILE,
                                 direction_str])
                __name__ = '__main__'
                ret = exec(script)
                assert not ret, f"Return value of program is {ret} instead "
                f"of 0"
                actual = sorted(open(OUTPUT_FILE).read().split('\n'))
                expected_dict = {}
                for direction in set(direction_str):
                    content = open(
                        os.path.join(EX_DIR, f'out_{direction}.txt'), 'r'
                    ).read()
                    partial_exp = content[:-1].split('\n') if content else []
                    for word_count in partial_exp:
                        word, count = word_count.split(',')
                        if word in expected_dict:
                            expected_dict[word] += int(count)
                        else:
                            expected_dict[word] = int(count)
                expected = sorted([f'{word},{count}' for word, count in
                                   expected_dict.items()] + [''])
                assert actual == expected, f"DIRECTION: {direction_str}\n"
                f"args: {sys.argv}\n"
                f"ACTUAL {actual}\n"
                f"EXPECTED: {expected}"
    sys.argv.clear()
    sys.argv.extend(original_argv)

    captured = capsys.readouterr()
    assert not captured.out and not captured.err, (f"No prints allowed!\nGot: "
                                                   f"out: {captured.out}\n"
                                                   f"err: {captured.err}\n")
    print(f"Time: {perf_counter() - start}")
