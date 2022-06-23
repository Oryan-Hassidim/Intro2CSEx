from ex12_utils import *
import os

TEST_DICT_ROOT = "test-dicts"


# noinspection Duplicates
def file_path(name):
    return os.path.join(name)


# class TestLoadWordsDict:
#
#     def test_basic(self):
#         expected = {"dog": True, "cat": True, "meow": True}
#         assert load_words_dict(file_path("alpha.txt")) == expected
#
#     def test_non_alpha(self):
#         expected = {"123": True, "!@#": True, "***": True}
#         assert load_words_dict(file_path("non-alpha.txt")) == expected
#
#     def test_spaces(self):
#         expected = {"a a": True, "b b": True}
#         assert load_words_dict(file_path("spaces.txt")) == expected
#
#     def test_empty_line(self):
#         expected = {"bob": True, "": True, "cat": True}
#         assert load_words_dict(file_path("empty-line.txt")) == expected


# noinspection Duplicates
class TestIsValidPath:

    def test_basic_row(self):
        board = [['C', 'A', 'T', 'Q'],
                 ['D', 'O', 'G', 'Q'],
                 ['B', 'I', 'T', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'CAT': True, 'DOG': True, 'BIT': True}
        path = [(0, 0), (0, 1), (0, 2)]
        print(is_valid_path(board, path, word_dict))
        assert is_valid_path(board, path, word_dict) == "CAT"

    def test_basic_col(self):
        board = [['C', 'D', 'B', 'Q'],
                 ['A', 'O', 'I', 'Q'],
                 ['T', 'G', 'T', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'CAT': True, 'DOG': True, 'BIT': True}
        path = [(0, 0), (1, 0), (2, 0)]
        assert is_valid_path(board, path, word_dict) == "CAT"

    def test_basic_diag_1(self):
        board = [['D', 'Q', 'Q', 'Q'],
                 ['Q', 'O', 'Q', 'Q'],
                 ['Q', 'Q', 'G', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'CAT': True, 'DOG': True, 'BOT': True}
        path = [(0, 0), (1, 1), (2, 2)]
        assert is_valid_path(board, path, word_dict) == "DOG"

    def test_changed_direction(self):
        board = [['A', 'T', 'R', 'Q'],
                 ['Q', 'L', 'E', 'Q'],
                 ['Q', 'Q', 'B', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'ALBERT': True}
        path = [(0, 0), (1, 1), (2, 2), (1, 2), (0, 2), (0, 1)]
        assert is_valid_path(board, path, word_dict) == "ALBERT"

    def test_valid_path_word_not_in_dict(self):
        board = [['C', 'A', 'T', 'Q'],
                 ['D', 'O', 'G', 'Q'],
                 ['B', 'I', 'T', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'DOG': True, 'BIT': True}
        path = [(0, 0), (0, 1), (0, 2)]
        assert is_valid_path(board, path, word_dict) is None

    def test_valid_path_word_shorter_than_in_dict(self):
        board = [['C', 'A', 'T', 'Q'],
                 ['D', 'O', 'G', 'Q'],
                 ['B', 'I', 'T', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'CAT': True, 'DOG': True, 'BIT': True}
        path = [(0, 0), (0, 1)]
        assert is_valid_path(board, path, word_dict) is None

    def test_valid_path_word_longer_than_in_dict(self):
        board = [['C', 'A', 'T', 'Q'],
                 ['D', 'O', 'G', 'Q'],
                 ['B', 'I', 'T', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'CAT': True, 'DOG': True, 'BIT': True}
        path = [(0, 0), (0, 1), (0, 2), (0, 3)]
        assert is_valid_path(board, path, word_dict) is None

    def test_path_exits_board(self):
        board = [['C', 'A', 'T', 'Q'],
                 ['D', 'O', 'G', 'Q'],
                 ['B', 'I', 'T', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'CAT': True, 'DOG': True, 'BIT': True}
        path = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]
        assert is_valid_path(board, path, word_dict) is None

    def test_path_starts_outside_board(self):
        board = [['C', 'A', 'T', 'Q'],
                 ['D', 'O', 'G', 'Q'],
                 ['B', 'I', 'T', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'CAT': True, 'DOG': True, 'BIT': True}
        path = [(0, 4), (0, 3), (0, 2)]
        assert is_valid_path(board, path, word_dict) is None

    def test_same_point_twice_in_path(self):
        board = [['C', 'A', 'T', 'Q'],
                 ['D', 'O', 'G', 'Q'],
                 ['B', 'I', 'T', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'CAT': True, 'DOG': True, 'BIT': True}
        path = [(0, 0), (0, 1), (0, 0)]
        assert is_valid_path(board, path, word_dict) is None

    def test_not_adjacent_coordinates(self):
        board = [['C', 'A', 'T', 'Q'],
                 ['D', 'O', 'G', 'Q'],
                 ['B', 'I', 'T', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'CAT': True, 'DOG': True, 'BIT': True}
        path = [(0, 0), (0, 1), (2, 2)]
        assert is_valid_path(board, path, word_dict) is None

    def test_negative_coordinates(self):
        board = [['C', 'A', 'T', 'Q'],
                 ['D', 'O', 'G', 'Q'],
                 ['B', 'I', 'T', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'CAT': True, 'DOG': True, 'BIT': True}
        path = [(0, -2), (0, -1), (0, 0)]
        assert is_valid_path(board, path, word_dict) is None

    def test_empty_path(self):
        board = [['C', 'A', 'T', 'Q'],
                 ['D', 'O', 'G', 'Q'],
                 ['B', 'I', 'T', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'CAT': True, 'DOG': True, 'BIT': True}
        path = []
        assert is_valid_path(board, path, word_dict) is None

    def test_one_letter_in_dict(self):
        board = [['C', 'A', 'T', 'Q'],
                 ['D', 'O', 'G', 'Q'],
                 ['B', 'I', 'T', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'C': True, 'DOG': True, 'BIT': True}
        path = [(0, 0)]
        assert is_valid_path(board, path, word_dict) == "C"

    def test_one_letter_not_in_dict(self):
        board = [['C', 'A', 'T', 'Q'],
                 ['D', 'O', 'G', 'Q'],
                 ['B', 'I', 'T', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'P': True, 'DOG': True, 'BIT': True}
        path = [(0, 0)]
        assert is_valid_path(board, path, word_dict) is None

    def test_multi_letter_cells(self):
        board = [['Q', 'Q', 'Q', 'Q'],
                 ['DO', 'GS', 'Q', 'Q'],
                 ['Q', 'Q', 'Q', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'DOGS': True}
        path = [(1, 0), (1, 1)]
        assert is_valid_path(board, path, word_dict) == "DOGS"


def load_words_dict(file):
    milon = open(file)
    lines = set(line.strip() for line in milon.readlines())
    milon.close()
    return lines


# noinspection Duplicates
class TestFindWords:

    # Regular cases

    def test_basic_rows(self):
        board = [['C', 'A', 'T', 'Q'],
                 ['D', 'O', 'G', 'Q'],
                 ['B', 'I', 'T', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'CAT': True, 'DOG': True, 'BIT': True}
        expected = [[(0, 0), (0, 1), (0, 2)],
                    [(1, 0), (1, 1), (1, 2)],
                    [(2, 0), (2, 1), (2, 2)]]
        assert sorted(find_length_n_words(3, board, word_dict)) == \
               sorted(expected)

    def test_basic_cols(self):
        board = [['C', 'D', 'B', 'Q'],
                 ['A', 'O', 'I', 'Q'],
                 ['T', 'G', 'T', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'CAT': True, 'DOG': True, 'BIT': True}
        expected = [[(0, 0), (1, 0), (2, 0)],
                    [(0, 1), (1, 1), (2, 1)],
                    [(0, 2), (1, 2), (2, 2)]]
        assert sorted(find_length_n_words(3, board, word_dict)) == \
               sorted(expected)

    def test_basic_diag_1(self):
        board = [['D', 'Q', 'Q', 'Q'],
                 ['Q', 'O', 'Q', 'Q'],
                 ['Q', 'Q', 'G', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'CAT': True, 'DOG': True, 'BOT': True}
        expected = [[(0, 0), (1, 1), (2, 2)]]
        assert find_length_n_words(3, board, word_dict) == expected

    def test_basic_diag_2(self):
        board = [['Q', 'Q', 'D', 'Q'],
                 ['Q', 'O', 'Q', 'Q'],
                 ['G', 'Q', 'Q', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'CAT': True, 'DOG': True, 'BOT': True}
        expected = [[(0, 2), (1, 1), (2, 0)]]
        assert find_length_n_words(3, board, word_dict) == expected

    def test_shared_letters(self):
        board = [['D', 'O', 'T', 'Q'],
                 ['O', 'Q', 'O', 'Q'],
                 ['G', 'Q', 'B', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'DOT': True, 'DOG': True, 'BOT': True}
        expected = [[(0, 0), (1, 0), (2, 0)],
                    [(0, 0), (0, 1), (0, 2)],
                    [(2, 2), (1, 2), (0, 2)]]
        assert sorted(find_length_n_words(3, board, word_dict)) == \
               sorted(expected)

    def test_changed_direction(self):
        board = [['A', 'T', 'R', 'Q'],
                 ['Q', 'L', 'E', 'Q'],
                 ['Q', 'Q', 'B', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'ALBERT': True}
        expected = [[(0, 0), (1, 1), (2, 2), (1, 2), (0, 2),
                                (0, 1)]]
        assert find_length_n_words(6, board, word_dict) == expected

    # Special cases

    def test_not_use_same_letter_twice(self):
        board = [['A', 'T', 'R', 'Q'],
                 ['Q', 'L', 'E', 'Q'],
                 ['Q', 'Q', 'B', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'ALBERTA': True}
        expected = []
        assert find_length_n_words(7, board, word_dict) == expected

    def test_words_not_in_board(self):
        board = [['Q', 'Q', 'Q', 'Q'],
                 ['Q', 'Q', 'Q', 'Q'],
                 ['Q', 'Q', 'B', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'DOT': True, 'DOG': True, 'BOT': True}
        expected = []
        assert find_length_n_words(3, board, word_dict) == expected

    def test_no_words_in_length_n_1(self):
        board = [['C', 'A', 'T', 'Q'],
                 ['D', 'O', 'G', 'Q'],
                 ['B', 'O', 'T', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'CAT': True, 'DOG': True, 'BOT': True}
        expected = []
        assert find_length_n_words(2, board, word_dict) == expected

    def test_no_words_in_length_n_2(self):
        board = [['C', 'A', 'T', 'Q'],
                 ['D', 'O', 'G', 'Q'],
                 ['B', 'O', 'T', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'CATH': True, 'DOGH': True, 'BOTH': True}
        expected = []
        assert find_length_n_words(3, board, word_dict) == expected

    def test_n_in_too_big(self):
        board = [['C', 'A', 'T', 'Q'],
                 ['D', 'O', 'G', 'Q'],
                 ['B', 'O', 'T', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'CAT': True, 'DOG': True, 'BOT': True}
        expected = []
        assert find_length_n_words(1000, board, word_dict) == expected

    def test_finds_correct_length_1(self):
        board = [['Q', 'Q', 'Q', 'Q'],
                 ['D', 'O', 'G', 'Q'],
                 ['Q', 'Q', 'I', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'DOG': True, 'DOGI': True}
        expected = [[(1, 0), (1, 1), (1, 2)]]
        assert find_length_n_words(3, board, word_dict) == expected

    def test_finds_correct_length_2(self):
        board = [['Q', 'Q', 'Q', 'Q'],
                 ['D', 'O', 'G', 'Q'],
                 ['Q', 'Q', 'I', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'DOG': True, 'DOGI': True}
        expected = [[(1, 0), (1, 1), (1, 2), (2, 2)]]
        assert find_length_n_words(4, board, word_dict) == expected

    def test_multiple_options(self):
        board = [['Q', 'O', 'Q', 'Q'],
                 ['D', 'O', 'G', 'Q'],
                 ['Q', 'O', 'Q', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'DOG': True}
        expected_1 = [[(1, 0), (1, 1), (1, 2)]]
        expected_2 = [[(1, 0), (0, 1), (1, 2)]]
        expected_3 = [[(1, 0), (2, 1), (1, 2)]]
        actual = find_length_n_words(3, board, word_dict)
        assert sorted(actual) == sorted(expected_1 + expected_2 + expected_3)

    def test_palindrome(self):
        board = [['Q', 'Q', 'Q', 'Q'],
                 ['B', 'O', 'B', 'Q'],
                 ['Q', 'Q', 'Q', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'BOB': True}
        expected_1 = [[(1, 0), (1, 1), (1, 2)]]
        expected_2 = [[(1, 2), (1, 1), (1, 0)]]
        actual = find_length_n_paths(3, board, word_dict)
        assert sorted(actual) == sorted(expected_1 + expected_2)

    def test_single_letter_word(self):
        board = [['Q', 'Q', 'Q', 'Q'],
                 ['D', 'O', 'G', 'Q'],
                 ['Q', 'Q', 'Q', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'D': True, 'O': True, 'G': True}
        expected = [[(1, 0)], [(1, 1)], [(1, 2)]]
        assert sorted(find_length_n_paths(1, board, word_dict)) == \
               sorted(expected)

    def test_n_is_0(self):
        board = [['Q', 'Q', 'Q', 'Q'],
                 ['D', 'O', 'G', 'Q'],
                 ['Q', 'Q', 'Q', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'D': True, 'O': True, 'G': True}
        expected = []
        assert find_length_n_words(0, board, word_dict) == expected

    def test_multi_letter_cells(self):
        board = [['Q', 'Q', 'Q', 'Q'],
                 ['DO', 'G', 'S', 'Q'],
                 ['Q', 'Q', 'Q', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'DOGS': True}
        expected = [[(1, 0), (1, 1),(1,2)]]
        assert find_length_n_paths(3, board, word_dict) == expected

    def test_does_not_split_cells(self):
        board = [['Q', 'Q', 'Q', 'Q'],
                 ['DO', 'GS', 'Q', 'Q'],
                 ['Q', 'Q', 'Q', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'DOG': True}
        expected = []
        assert find_length_n_words(2, board, word_dict) == expected

    def test_long_dict(self):
        board = [['C', 'A', 'T', 'Q'],
                 ['D', 'O', 'G', 'Q'],
                 ['B', 'I', 'T', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = load_words_dict(file_path("boggle_dict.txt"))
        expected = [[(0, 1), (1, 0), (1, 1)],
                    [(0, 1), (1, 2), (1, 1)],
                    [(2, 0), (2, 1), (1, 0)],
                    [(2, 0), (2, 1), (1, 2)],
                    [(2, 0), (2, 1), (1, 1)],
                    [(2, 0), (2, 1), (2, 2)],
                    [(2, 0), (1, 1), (0, 1)],
                    [(2, 0), (1, 1), (1, 0)],
                    [(2, 0), (1, 1), (1, 2)],
                    [(2, 0), (1, 1), (2, 1)],
                    [(2, 0), (1, 1), (0, 2)],
                    [(2, 0), (1, 1), (2, 2)],
                    [(0, 0), (0, 1), (1, 0)],
                    [(0, 0), (0, 1), (1, 2)],
                    [(0, 0), (0, 1), (0, 2)],
                    [(0, 0), (1, 1), (2, 0)],
                    [(0, 0), (1, 1), (1, 0)],
                    [(0, 0), (1, 1), (1, 2)],
                    [(0, 0), (1, 1), (0, 2)],
                    [(0, 0), (1, 1), (2, 2)],
                    [(1, 0), (0, 1), (1, 2)],
                    [(1, 0), (2, 1), (2, 0)],
                    [(1, 0), (2, 1), (1, 2)],
                    [(1, 0), (2, 1), (2, 2)],
                    [(1, 0), (1, 1), (2, 0)],
                    [(1, 0), (1, 1), (0, 0)],
                    [(1, 0), (1, 1), (1, 2)],
                    [(1, 0), (1, 1), (0, 2)],
                    [(1, 0), (1, 1), (2, 2)],
                    [(1, 2), (0, 1), (1, 0)],
                    [(1, 2), (0, 1), (0, 2)],
                    [(1, 2), (2, 1), (2, 0)],
                    [(1, 2), (2, 1), (1, 0)],
                    [(1, 2), (2, 1), (1, 1)],
                    [(1, 2), (2, 1), (2, 2)],
                    [(1, 2), (1, 1), (0, 1)],
                    [(1, 2), (1, 1), (2, 0)],
                    [(1, 2), (1, 1), (1, 0)],
                    [(1, 2), (1, 1), (0, 2)],
                    [(1, 2), (1, 1), (2, 2)],
                    [(1, 1), (0, 1), (0, 2)],
                    [(1, 1), (2, 0), (2, 1)],
                    [(1, 1), (0, 0), (0, 1)],
                    [(1, 1), (1, 0), (0, 1)],
                    [(0, 2), (0, 1), (1, 0)],
                    [(0, 2), (0, 1), (1, 2)],
                    [(0, 2), (0, 1), (1, 1)],
                    [(2, 2), (2, 1), (1, 0)],
                    [(2, 2), (2, 1), (1, 2)],
                    [(0, 2), (1, 1), (0, 0)],
                    [(2, 2), (1, 1), (0, 0)],
                    [(0, 2), (1, 1), (1, 0)],
                    [(2, 2), (1, 1), (1, 0)],
                    [(0, 2), (1, 1), (1, 2)],
                    [(2, 2), (1, 1), (1, 2)],
                    [(0, 2), (1, 1), (2, 2)],
                    [(2, 2), (1, 1), (0, 2)]]
        assert sorted(find_length_n_words(3, board, word_dict)) == sorted(expected)

    def test_full_dict_random_board(self):
        board = [['T', 'G', 'O', 'T'],
                 ['R', 'D', 'B', 'F'],
                 ['H', 'N', 'U', 'P'],
                 ['N', 'A', 'S', 'N']]
        word_dict = load_words_dict(file_path("boggle_dict.txt"))
        expected_3 = [[(3, 1), (2, 1), (1, 1)],
                      [(3, 1), (2, 1), (3, 0)],
                      [(3, 1), (3, 0), (2, 1)],
                      [(3, 1), (2, 1), (3, 2)],
                      [(3, 1), (3, 2), (2, 3)],
                      [(3, 1), (2, 2), (1, 3)],
                      [(1, 2), (0, 2), (1, 1)],
                      [(1, 2), (0, 2), (0, 1)],
                      [(1, 2), (0, 2), (0, 3)],
                      [(1, 2), (2, 2), (1, 1)],
                      [(1, 2), (2, 2), (2, 1)],
                      [(1, 2), (2, 2), (3, 3)],
                      [(1, 2), (2, 2), (3, 2)],
                      [(1, 1), (0, 2), (1, 2)],
                      [(1, 1), (0, 2), (1, 3)],
                      [(1, 1), (0, 2), (0, 1)],
                      [(1, 1), (0, 2), (0, 3)],
                      [(1, 1), (2, 2), (1, 2)],
                      [(1, 1), (2, 2), (2, 1)],
                      [(1, 1), (2, 2), (3, 3)],
                      [(1, 1), (2, 2), (2, 3)],
                      [(1, 3), (0, 2), (1, 2)],
                      [(1, 3), (0, 2), (0, 1)],
                      [(1, 3), (2, 2), (1, 2)],
                      [(1, 3), (2, 2), (1, 1)],
                      [(1, 3), (2, 2), (2, 1)],
                      [(1, 3), (2, 2), (3, 3)],
                      [(0, 1), (0, 2), (1, 2)],
                      [(0, 1), (0, 2), (1, 1)],
                      [(0, 1), (0, 2), (0, 3)],
                      [(2, 0), (3, 1), (2, 1)],
                      [(2, 0), (3, 1), (3, 0)],
                      [(2, 0), (3, 1), (3, 2)],
                      [(2, 1), (3, 1), (2, 0)],
                      [(3, 0), (3, 1), (2, 0)],
                      [(2, 1), (3, 1), (3, 0)],
                      [(3, 0), (3, 1), (2, 1)],
                      [(2, 1), (3, 1), (3, 2)],
                      [(3, 0), (3, 1), (3, 2)],
                      [(2, 1), (2, 2), (1, 2)],
                      [(3, 3), (2, 2), (1, 2)],
                      [(2, 1), (2, 2), (3, 3)],
                      [(3, 3), (2, 2), (2, 1)],
                      [(2, 1), (2, 2), (3, 2)],
                      [(3, 3), (2, 2), (3, 2)],
                      [(0, 2), (1, 3), (0, 3)],
                      [(2, 3), (2, 2), (1, 2)],
                      [(2, 3), (2, 2), (1, 1)],
                      [(2, 3), (2, 2), (2, 1)],
                      [(2, 3), (2, 2), (3, 3)],
                      [(2, 3), (2, 2), (3, 2)],
                      [(3, 2), (3, 1), (2, 1)],
                      [(3, 2), (3, 1), (3, 0)],
                      [(3, 2), (3, 1), (2, 2)],
                      [(3, 2), (2, 2), (1, 2)],
                      [(3, 2), (2, 2), (1, 1)],
                      [(3, 2), (2, 2), (2, 1)],
                      [(3, 2), (2, 2), (3, 3)],
                      [(3, 2), (2, 2), (2, 3)],
                      [(0, 3), (0, 2), (1, 1)],
                      [(0, 3), (0, 2), (0, 1)],
                      [(2, 2), (1, 1), (0, 2)],
                      [(2, 2), (1, 3), (0, 2)],
                      [(2, 2), (2, 1), (3, 2)],
                      [(2, 2), (3, 3), (3, 2)],
                      [(2, 2), (2, 3), (3, 2)]]
        expected_4 = [[(3, 1), (3, 0), (2, 1), (3, 2)],
                      [(3, 1), (2, 1), (2, 2), (3, 2)],
                      [(1, 2), (2, 2), (1, 1), (0, 2)],
                      [(1, 2), (2, 2), (1, 3), (0, 2)],
                      [(1, 2), (2, 2), (2, 1), (3, 1)],
                      [(1, 2), (2, 2), (2, 1), (1, 1)],
                      [(1, 2), (2, 2), (2, 1), (3, 0)],
                      [(1, 2), (2, 2), (2, 1), (3, 2)],
                      [(1, 2), (2, 2), (3, 3), (3, 2)],
                      [(1, 1), (2, 2), (3, 1), (2, 1)],
                      [(1, 1), (2, 2), (3, 1), (3, 0)],
                      [(1, 1), (2, 2), (2, 1), (3, 2)],
                      [(1, 1), (2, 2), (3, 3), (3, 2)],
                      [(1, 1), (2, 2), (2, 3), (3, 2)],
                      [(1, 3), (2, 2), (2, 1), (1, 1)],
                      [(1, 3), (2, 2), (2, 1), (3, 2)],
                      [(1, 3), (2, 2), (3, 3), (3, 2)],
                      [(2, 0), (3, 1), (2, 1), (1, 1)],
                      [(2, 0), (3, 1), (3, 2), (2, 3)],
                      [(2, 0), (3, 1), (2, 2), (1, 1)],
                      [(2, 0), (3, 1), (2, 2), (1, 3)],
                      [(2, 0), (3, 1), (2, 2), (2, 1)],
                      [(2, 0), (3, 1), (2, 2), (3, 3)],
                      [(3, 0), (3, 1), (2, 1), (3, 2)],
                      [(2, 1), (2, 2), (3, 3), (3, 2)],
                      [(3, 3), (2, 2), (2, 1), (3, 2)],
                      [(2, 3), (2, 2), (2, 1), (3, 1)],
                      [(2, 3), (2, 2), (2, 1), (3, 2)],
                      [(2, 3), (2, 2), (3, 3), (3, 2)],
                      [(3, 2), (3, 1), (2, 1), (1, 1)],
                      [(3, 2), (2, 1), (2, 2), (1, 2)],
                      [(3, 2), (3, 3), (2, 2), (1, 2)],
                      [(3, 2), (2, 3), (2, 2), (1, 1)],
                      [(3, 2), (2, 3), (2, 2), (2, 1)],
                      [(3, 2), (2, 3), (2, 2), (3, 3)],
                      [(3, 2), (2, 2), (2, 1), (3, 0)],
                      [(0, 3), (0, 2), (1, 3), (2, 2)],
                      [(2, 2), (2, 1), (1, 1), (0, 2)]]
        expected_5 = [ [(1, 2), (2, 2), (2, 1), (3, 1), (3, 2)],
                       [(1, 2), (2, 2), (2, 1), (1, 1), (2, 0)],
                       [(1, 2), (2, 2), (2, 1), (1, 1), (0, 0)],
                       [(1, 1), (2, 2), (3, 1), (2, 1), (3, 2)],
                       [(2, 0), (3, 1), (2, 2), (2, 1), (3, 2)],
                       [(2, 0), (3, 1), (2, 2), (3, 3), (3, 2)],
                       [(3, 0), (3, 1), (2, 1), (1, 1), (2, 2)],
                       [(2, 3), (2, 2), (2, 1), (3, 1), (3, 2)],
                       [(3, 2), (2, 2), (2, 1), (3, 0), (3, 1)],
                       [(0, 3), (0, 2), (1, 3), (2, 2), (3, 2)]]
        expected_6 = [
            [(3, 0), (3, 1), (2, 1), (1, 1), (2, 2), (3, 2)],
            [(3, 0), (2, 0), (3, 1), (2, 1), (1, 1), (2, 2)],
            [(3, 2), (3, 1), (3, 0), (2, 1), (2, 2), (2, 3)],
            [(3, 2), (2, 2), (2, 1), (1, 1), (0, 2), (0, 1)],
            [(3, 2), (2, 2), (2, 1), (3, 0), (3, 1), (2, 0)],
            [(2, 2), (2, 1), (2, 0), (3, 1), (3, 2), (2, 3)]]
        assert sorted(find_length_n_words(3, board, word_dict)) == sorted(expected_3)
        assert sorted(find_length_n_words(4, board, word_dict)) == sorted(expected_4)
        assert sorted(find_length_n_words(5, board, word_dict)) == sorted(expected_5)
        assert sorted(find_length_n_words(6, board, word_dict)) == sorted(expected_6)

    def test_max_score_paths(self):
        board = [[
            # Normal board
            ['A', 'I', 'P', 'H'],
            ['I', 'R', 'S', 'S'],
            ['A', 'E', 'E', 'T'],
            ['T', 'H', 'E', 'R']],
            [
                # Board with doubles
                ['E', 'M', 'AB', 'O'],
                ['IN', 'ON', 'AN', 'M'],
                ['ST', 'R', 'U', 'TH'],
                ['Y', 'ST', 'R', 'W']],
            [
                # Board with doubles
                ['W', 'E', 'AI', 'G'],
                ['S', 'N', 'AO', 'A'],
                ['TH', 'N', 'O', 'IN'],
                ['W', 'D', 'D', 'M']],
            [
                ['W', 'S', 'E', 'E'],
                ['Y', 'TH', 'H', 'AE'],
                ['M', 'I', 'Y', 'A'],
                ['T', 'W', 'H', 'C']]]

        expected = [[('AIR', 9), ('AIRS', 16), ('AIRIEST', 49), ('AIREST', 36),
                     ('AIRER', 25), ('AIS', 9), ('AIA', 9), ('ARS', 9),
                     ('ARSE', 16), ('ARSES', 25), ('ARIS', 16), ('ARISH', 25),
                     ('ARISE', 25), ('ARISES', 36), ('ARIA', 16), ('ARE', 9),
                     ('ARES', 16), ('AREA', 16), ('ARET', 16), ('ARETS', 25),
                     ('ARETE', 25), ('ARERE', 25), ('IRE', 9), ('IRES', 16),
                     ('IRATE', 25), ('IRATEST', 49), ('ISH', 9), ('PIA', 9),
                     ('PIR', 9), ('PIRS', 16), ('PIRAI', 25), ('PIRATE', 36),
                     ('PIRATES', 49), ('PIS', 9), ('PISS', 16), ('PISSER', 36),
                     ('PISH', 16), ('PISE', 16), ('PISES', 25), ('PISTE', 25),
                     ('PISTES', 36), ('PSST', 16), ('PSI', 9), ('PST', 9),
                     ('PRISS', 25), ('PRISE', 25), ('PRISES', 36),
                     ('PRISER', 36), ('PRISERE', 49), ('PRAISE', 36),
                     ('PRAISES', 49), ('PRAISER', 49), ('PRIES', 25),
                     ('PRIEST', 36), ('PRIESTS', 49), ('PRE', 9), ('PREE', 16),
                     ('PREES', 25), ('PRESS', 25), ('PRESSER', 49),
                     ('PRESE', 25), ('PRESET', 36), ('PRESETS', 49),
                     ('PRESES', 36), ('PREST', 25), ('PRESTS', 36),
                     ('PRESTER', 49), ('PRAESES', 49), ('PRAT', 16),
                     ('PRATE', 25), ('PRATES', 36), ('PREHEAT', 49),
                     ('IRIS', 16), ('IRISES', 36), ('RIP', 9), ('RIPS', 16),
                     ('RIA', 9), ('RISP', 16), ('RISPS', 25), ('RISE', 16),
                     ('RISES', 25), ('RISER', 25), ('RAI', 9), ('RAIS', 16),
                     ('RAISE', 25), ('RAISES', 36), ('RAISER', 36),
                     ('RAIA', 16), ('REE', 9), ('REES', 16), ('REEST', 25),
                     ('REESTS', 36), ('RES', 9), ('RESH', 16), ('RESET', 25),
                     ('RESETS', 36), ('RESES', 25), ('RESEE', 25),
                     ('REST', 16), ('RESTS', 25), ('RESTER', 36), ('REI', 9),
                     ('REH', 9), ('RET', 9), ('RAT', 9), ('RATH', 16),
                     ('RATHE', 25), ('RATHER', 36), ('RATHEREST', 81),
                     ('RATHEST', 49), ('RATE', 16), ('RATES', 25), ('RAH', 9),
                     ('RETS', 16), ('RETREE', 36), ('RETREES', 49),
                     ('RETE', 16), ('RESEAT', 36), ('REHEAT', 36),
                     ('SPIRE', 25), ('SPIREA', 36), ('SPIRES', 36),
                     ('SPREE', 25), ('SPREES', 36), ('SPREATHE', 64),
                     ('SPREATHES', 81), ('SPRAT', 25), ('SPREETHE', 64),
                     ('SIP', 9), ('SIPS', 16), ('SIR', 9), ('SIRI', 16),
                     ('SIRE', 16), ('SIREE', 25), ('SIREES', 36),
                     ('SIRES', 25), ('SRI', 9), ('SET', 9), ('SETS', 16),
                     ('SESH', 16), ('SER', 9), ('SERIPH', 36), ('SERIPHS', 49),
                     ('SERA', 16), ('SERAI', 25), ('SERIATE', 49),
                     ('SERE', 16), ('SEE', 9), ('SEER', 16), ('SEETHE', 36),
                     ('SEETHER', 49), ('SEES', 16), ('SERES', 25),
                     ('SEREST', 36), ('SERER', 25), ('SEI', 9), ('SEIR', 16),
                     ('SEA', 9), ('SEAR', 16), ('SEARE', 25), ('SEAREST', 49),
                     ('SEARER', 36), ('SEAT', 16), ('SETA', 16), ('STERE', 25),
                     ('STEER', 25), ('STREET', 36), ('STERES', 36),
                     ('STEERER', 49), ('SPIRIEST', 64), ('SPRIEST', 49),
                     ('STEERS', 36),
                     ('STEERIES', 64), ('SESE', 16), ('SERS', 16),
                     ('SERAIS', 36), ('SERIATES', 64), ('SERIES', 36),
                     ('SEERS', 25), ('AESIR', 25), ('AETHER', 36),
                     ('AETHERS', 49), ('ARAISE', 36), ('ARAISES', 49),
                     ('ATE', 9), ('ATES', 16), ('ESS', 9), ('ESSE', 16),
                     ('ESES', 16), ('EST', 9), ('ESTS', 16), ('ESTER', 25),
                     ('ERS', 9), ('ERSES', 25), ('ERST', 16), ('ERA', 9),
                     ('ERE', 9), ('ERES', 16), ('EAR', 9), ('EARS', 16),
                     ('EARST', 25), ('EAT', 9), ('EATH', 16), ('EATHE', 25),
                     ('ETH', 9), ('ETHE', 16), ('ETHER', 25), ('ETHERS', 36),
                     ('ETHERISH', 64), ('ETHERIST', 64), ('ETHERISTS', 81),
                     ('ETA', 9), ('TES', 9), ('TESSERA', 49), ('TERSE', 25),
                     ('TERAI', 25), ('TERAIS', 36), ('TERES', 25), ('TEE', 9),
                     ('TEES', 16), ('TEER', 16), ('TEERS', 25), ('TEETH', 25),
                     ('TEETHE', 36), ('TEETHER', 49), ('TRES', 16),
                     ('TRESS', 25), ('TREE', 16), ('TREES', 25),
                     ('TEETHES', 49), ('TEETHERS', 64), ('THE', 9),
                     ('THERE', 25), ('THERES', 36), ('THETE', 25),
                     ('THETES', 36), ('THEE', 16), ('THEES', 25),
                     ('THESP', 25), ('THESPS', 36), ('THESE', 25),
                     ('THESES', 36), ('THEIR', 25), ('THEIRS', 36),
                     ('THAE', 16), ('THAR', 16), ('THARS', 25), ('TEETER', 36),
                     ('TEST', 16), ('TESTS', 25), ('TESTE', 25),
                     ('TESTES', 36), ('TESTER', 36), ('TESTEE', 36),
                     ('TESTEES', 49), ('TERSEST', 49), ('TERSER', 36),
                     ('TERETE', 36), ('TEA', 9), ('TEAR', 16), ('TEARS', 25),
                     ('TEARER', 36), ('TEETERS', 49), ('TAE', 9), ('TAES', 16),
                     ('TAR', 9), ('TARS', 16), ('TARSI', 25), ('TARSIA', 36),
                     ('TARP', 16), ('TARPS', 25), ('TARA', 16), ('TARE', 16),
                     ('TARES', 25), ('TAI', 9), ('TAIRA', 25), ('HER', 9),
                     ('HERE', 16), ('HERES', 25), ('HET', 9), ('HETS', 16),
                     ('HETE', 16), ('HETES', 25), ('HES', 9), ('HESP', 16),
                     ('HESPS', 25), ('HEST', 16), ('HESTS', 25), ('HERS', 16),
                     ('HERSE', 25), ('HERIES', 36), ('HEREAT', 36),
                     ('HERSES', 36), ('HERISSE', 49), ('HEIR', 16),
                     ('HEIRS', 25), ('HEIRESS', 49), ('HEAR', 16),
                     ('HEARS', 25), ('HEARSE', 36), ('HEARSES', 49),
                     ('HEARE', 25), ('HEARES', 36), ('HEARER', 36),
                     ('HEAT', 16), ('HETAIRIA', 64), ('HETAIRIST', 81),
                     ('HETAIRISTS', 100), ('HETAIRA', 49), ('HETAIRAI', 64),
                     ('HAE', 9), ('HAES', 16), ('HAERES', 36), ('HAET', 16),
                     ('HARSH', 25), ('HARP', 16), ('HARPIST', 49),
                     ('HARPISTS', 64), ('HARPS', 25), ('HARISH', 36),
                     ('HARE', 16), ('HARES', 25), ('HAIR', 16), ('HAIRS', 25),
                     ('HAIRST', 36), ('HAIRSTS', 49), ('HAT', 9), ('HATE', 16),
                     ('HATES', 25), ('HATER', 25), ('HATERS', 36),
                     ('EERIE', 25), ('EERIEST', 49), ('RESPIRE', 49),
                     ('RESPIRES', 64), ('RERISE', 36), ('RERAISE', 49),
                     ('REHEAR', 36), ('REHEARS', 49), ('REHEARSE', 64),
                     ('REHEARSES', 81)],
                    [('EON', 4), ('MEIN', 9), ('MON', 4), ('MINE', 9),
                     ('MANO', 9), ('MAN', 4), ('ABO', 4), ('ONE', 4),
                     ('ONST', 4), ('ANON', 4), ('MOAN', 9), ('MURINE', 25),
                     ('MURR', 16), ('MURRINE', 36), ('MURRIN', 25),
                     ('MURRY', 25), ('MUON', 9), ('MUSTY', 16), ('MUST', 9),
                     ('STY', 4), ('STRUM', 16), ('STRINE', 16), ('STONE', 9),
                     ('RONIN', 9), ('RONE', 9), ('RUTH', 9), ('RUM', 9),
                     ('RUSTY', 16), ('RUST', 9), ('RINE', 9), ('RIN', 4),
                     ('RAN', 4), ('URINE', 16), ('THAN', 4), ('THRUM', 16),
                     ('THRUST', 16), ('THRU', 9), ('STUM', 9), ('WURST', 16)],
                    [('WENS', 16), ('WEN', 9), ('ENS', 9), ('AIGA', 9),
                     ('AINE', 9), ('AINS', 9), ('AIN', 4), ('AIA', 4),
                     ('GAINS', 16), ('GAIN', 9), ('SNOD', 16), ('SEWN', 16),
                     ('SEW', 9), ('SEN', 9), ('NEWS', 16), ('NEW', 9),
                     ('NTH', 4), ('NON', 9), ('NOD', 9), ('NOMINA', 25),
                     ('NOM', 9), ('AGAIN', 16), ('NONES', 25), ('NONE', 16),
                     ('ONS', 9), ('ODD', 9), ('ONES', 16), ('ONE', 9),
                     ('DONNES', 36), ('DONNE', 25), ('DONS', 16), ('DON', 9),
                     ('DOD', 9), ('DONE', 16), ('DOM', 9), ('DINO', 9),
                     ('DIN', 4), ('MINA', 9), ('MINO', 9), ('MIND', 9),
                     ('MONTHS', 25), ('MONTH', 16), ('MONS', 16), ('MON', 9),
                     ('MOD', 9), ('MOA', 9)],
                    [('SWY', 9), ('SEE', 9), ('SYTHE', 16), ('SHE', 9),
                     ('SHY', 9), ('SHIM', 16), ('SHIT', 16), ('SHAY', 16),
                     ('SHAH', 16), ('SHA', 9), ('EHS', 9), ('ETHS', 9),
                     ('ETH', 4), ('THYMI', 16), ('THY', 4), ('THEE', 9),
                     ('THE', 4), ('HES', 9), ('HETHS', 16), ('HETH', 9),
                     ('HYTHES', 25), ('HYTHE', 16), ('HAE', 4), ('HITHES', 25),
                     ('HITHE', 16), ('HIM', 9), ('HIYA', 16), ('HIT', 9),
                     ('HAY', 9), ('HAH', 9), ('MYTHS', 16), ('MYTHI', 16),
                     ('MYTHY', 16), ('MYTH', 9), ('MIHA', 16), ('YAHS', 16),
                     ('YAH', 9), ('YAE', 4), ('ACHY', 16), ('ACH', 9),
                     ('AHS', 9), ('AHI', 9), ('TITHES', 25), ('TITHE', 16),
                     ('WITHS', 16), ('WITHY', 16), ('WITHES', 25),
                     ('WITHE', 16), ('WITH', 9), ('WIT', 9), ('WHY', 9),
                     ('WHIM', 16), ('WHIT', 16), ('WHA', 9), ('WYCH', 16),
                     ('HAHS', 16), ('CAY', 9), ('CHIT', 16), ('CHI', 9),
                     ('CHAY', 16), ('CHA', 9)]
                    ]

        all_word_from_dict =  load_words_dict(file_path("boggle_dict.txt"))  # Put all words from the dict
        for test_num in range(len(board)):
            result = max_score_paths(board[test_num], all_word_from_dict)
            result = [(''.join([board[test_num][i][j] for i, j in path]),
                       len(path) ** 2) for path in result]
            assert sorted(result) == sorted(expected[test_num])
