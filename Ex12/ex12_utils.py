#############################################################
# FILE : ex12_utils.py
# EXERCISE : intro2cs2 Ex12 2022
# DESCRIPTION: This file contains the functions for the exercise
# NOTES:
#############################################################

DIRECTIONS = {
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1)
}


def pairwise(iterable):
    """
    returns a generator of pairs of items from an iterable.
    """
    flag = False
    for item in iterable:
        if flag:
            yield last, item
        last = item
        flag = True


def subtract_vecors(vec1, vec2):
    """
    returns the vector that is the difference of vec1 and vec2
    """
    return (vec2[0]-vec1[0], vec2[1]-vec1[1])


def is_valid_path(board, path, words):
    """
    returns the word if the path is valid, None otherwise
    """
    if False in (in_board(board, i, j) for i, j in path):
        return None
    word = ''.join(board[i][j] for i, j in path)
    if word not in words:
        return None
    for cell1, cell2 in pairwise(path):
        if subtract_vecors(cell1, cell2) not in DIRECTIONS:
            return None
    return word


def in_board(board, i, j):
    """
    returns True if the cell is in the board, False otherwise
    """
    return 0 <= i < len(board) and 0 <= j < len(board[i])


def find_paths_core_rec(board, words, i, j, path_so_far, word_so_far, n=None, m=None):
    """
    recursive function for finding all paths in board of words from a given words list.
    :param board: a board
    :param words: a list of words
    :param i: the row index of the current cell
    :param j: the column index of the current cell
    :param path_so_far: the path so far
    :param word_so_far: the word so far
    :param n: the requested length of the path, if exists
    :param m: the requested length of the word, if exists
    :return: generator of paths
    """

    # stop condition
    if not in_board(board, i, j) or (i, j) in path_so_far:
        return

    # add current cell to path
    word = word_so_far + board[i][j]
    # filtering words
    words = [w for w in words if w.startswith(word)]
    # stop condition
    if len(words) == 0:
        return
    path_so_far.append((i, j))

    # if there is a requested length, check if the path is valid and stop
    if (n and n == len(path_so_far)) or (m and len(word) >= m):
        if word in words and (not m or len(word) == m):
            yield path_so_far
        path_so_far.pop()
        return
    # else, yield and continue
    else:
        if word in words:
            yield path_so_far

    # recursive call
    for di, dj in DIRECTIONS:
        yield from find_paths_core_rec(board, words, i+di, j+dj, path_so_far, word, n, m)
    path_so_far.pop()


def find_paths_core(board, words, n=None, m=None):
    """
    returns all paths in board of words from a given words list.
    :param board: a board
    :param words: a list of words
    :param n: the requested length of the path, if exists
    :param m: the requested length of the word, if exists
    :return: generator of paths
    """
    chars = {c for row in board for cell in row for c in cell}
    words = [word for word in words if chars.issuperset(word)]
    for i, row in enumerate(board):
        for j, _ in enumerate(row):
            gen = find_paths_core_rec(
                board, words, i, j, [], '', n, m)
            yield from gen


def find_length_n_paths(n, board, words):
    """
    returns all paths of length n in board of words from a given words list.
    """
    if n == 0:
        return []
    gen = find_paths_core(board, words, n, None)
    return list(path.copy() for path in gen)


def find_length_n_words(n, board, words):
    """
    returns all words of length n in board of words from a given words list.
    """
    if n == 0:
        return []
    words_in_length = [word for word in words if len(word) == n]
    gen = find_paths_core(board, words_in_length, None, n)
    return list(path.copy() for path in gen)


def max_score_paths(board, words):
    """
    returns paths for achieving the highest score in board of 
    words from a given words list.
    """
    res = {}
    gen = find_paths_core(board, words, None, None)
    for path in gen:
        word = ''.join([board[i][j] for i, j in path])
        if len(res.get(word, [])) < len(path):
            res[word] = path.copy()
    return [path for path in res.values()]


# def max_score_paths(board, words):
#    res = {}
#    n = len(board) * len(board[0])
#    while n > 0:
#        words_sub = [word for word in words if word not in res]
#        if words_sub:
#            n_paths = find_length_n_paths(n, board, words_sub)
#            if not n_paths:
#                n -= 1
#                continue
#            for path in n_paths:
#                word = ''.join([board[i][j] for i, j in path])
#                if word not in res:
#                    res[word] = path
#            n -= 1
#        else:
#            return [path for path in res.values()]
#    return [path for path in res.values()]


def __all_words():
    """
    returns all words in the dictionary
    """
    with open('boggle_dict.txt') as f:
        return f.read().splitlines()


if __name__ == '__main__':
    words = __all_words()

    board1 = [
        ['A', 'E', 'K', 'E'],
        ['S', 'C', 'EE', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    board2 = [
        ['A', 'K', 'C', 'E', 'K', 'Q', 'D', 'R'],
        ['S', 'F', 'U', 'S', 'A', 'BA', 'C', 'E'],
        ['A', 'Q', 'E', 'E', 'A', 'B', 'C', 'E'],
        ['A', 'B', 'CR', 'C', 'KEC', 'Q', 'D', 'R'],
        ['S', 'F', 'C', 'S', 'K', 'Q', 'D', 'R'],
        ['A', 'D', 'E', 'E', 'K', 'QU', 'D', 'R']
    ]
    words1 = ["SEED", "SEE", "SEEK"]
    words2 = ['ABAB', 'ABAC', 'QUD', 'QUK']
    # print(find_length_n_paths(3, board1, words))
    # print(find_length_n_paths(4, board1, words))
    # print(find_length_n_paths(6, board1, words))
    # print(find_length_n_words(3, board1, words))
    # print(max_score_paths(board2, words))
    path1 = [(1, 3), (2, 3), (2, 2)]
    path2 = [(0, 0), (1, 0), (2, 0), (3, 0)]
    path3 = [(0, 0), (1, 0), (2, 0), (3, 0)]
    path4 = [(0, 0), (2, 0), (2, 1), (3, 1)]
    path5 = [(1, 0), (2, 0), (2, 1), (3, 1)]
    # print(path1, is_valid_path(board, path1, words), ''.join([board[i][j] for i, j in path1]))
    # print(path2, is_valid_path(board, path2, words))
    # print(path3, is_valid_path(board, path3, words))
    # print(path4, is_valid_path(board, path4, words))
    # print(path5, is_valid_path(board, path5, words))

    # print(max_score_paths(board2, words))
    words = __all_words()
    from boggle_board_randomizer import randomize_board

    board = randomize_board()

    from time import perf_counter_ns

    # start = perf_counter()
    # print(max_score_paths(board, words))
    # print(perf_counter() - start)
    start = perf_counter_ns()
    print(start)
    paths = max_score_paths(board, words)
    end = perf_counter_ns()
    print(end)
    ms = (end - start) / 1e6
    print(f"{ms}ms")
    sum = 0
    print("\n".join(str(row) for row in board))
    lst = []
    for path in paths:
        word = ''.join([board[i][j] for i, j in path])
        score = len(path) ** 2
        sum += score
        lst.append((word, score))
        print(word, words.index(word), score)

    print(lst)

    board = [
        ['A', 'I', 'P', 'H'],
        ['I', 'R', 'S', 'S'],
        ['A', 'E', 'E', 'T'],
        ['T', 'H', 'E', 'R']
    ]
    expected = [('AIR', 9), ('AIRS', 16), ('AIRIEST', 49), ('AIREST', 36), ('AIRER', 25), ('AIS', 9), ('AIA', 9), ('ARS', 9), ('ARSE', 16), ('ARSES', 25), ('ARIS', 16), ('ARISH', 25), ('ARISE', 25), ('ARISES', 36), ('ARIA', 16), ('ARE', 9), ('ARES', 16), ('AREA', 16), ('ARET', 16), ('ARETS', 25), ('ARETE', 25), ('ARERE', 25), ('IRE', 9), ('IRES', 16), ('IRATE', 25), ('IRATEST', 49), ('ISH', 9), ('PIA', 9), ('PIR', 9), ('PIRS', 16), ('PIRAI', 25), ('PIRATE', 36), ('PIRATES', 49), ('PIS', 9), ('PISS', 16), ('PISSER', 36), ('PISH', 16), ('PISE', 16), ('PISES', 25), ('PISTE', 25), ('PISTES', 36), ('PSST', 16), ('PSI', 9), ('PST', 9), ('PRISS', 25), ('PRISE', 25), ('PRISES', 36), ('PRISER', 36), ('PRISERE', 49), ('PRAISE', 36), ('PRAISES', 49), ('PRAISER', 49), ('PRIES', 25), ('PRIEST', 36), ('PRIESTS', 49), ('PRE', 9), ('PREE', 16), ('PREES', 25), ('PRESS', 25), ('PRESSER', 49), ('PRESE', 25), ('PRESET', 36), ('PRESETS', 49), ('PRESES', 36), ('PREST', 25), ('PRESTS', 36), ('PRESTER', 49), ('PRAESES', 49), ('PRAT', 16), ('PRATE', 25), ('PRATES', 36), ('PREHEAT', 49), ('IRIS', 16), ('IRISES', 36), ('RIP', 9), ('RIPS', 16), ('RIA', 9), ('RISP', 16), ('RISPS', 25), ('RISE', 16), ('RISES', 25), ('RISER', 25), ('RAI', 9), ('RAIS', 16), ('RAISE', 25), ('RAISES', 36), ('RAISER', 36), ('RAIA', 16), ('REE', 9), ('REES', 16), ('REEST', 25), ('REESTS', 36), ('RES', 9), ('RESH', 16), ('RESET', 25), ('RESETS', 36), ('RESES', 25), ('RESEE', 25), ('REST', 16), ('RESTS', 25), ('RESTER', 36), ('REI', 9), ('REH', 9), ('RET', 9), ('RAT', 9), ('RATH', 16), ('RATHE', 25), ('RATHER', 36), ('RATHEREST', 81), ('RATHEST', 49), ('RATE', 16), ('RATES', 25), ('RAH', 9), ('RETS', 16), ('RETREE', 36), ('RETREES', 49), ('RETE', 16), ('RESEAT', 36), ('REHEAT', 36), ('SPIRE', 25), ('SPIREA', 36), ('SPIRES', 36), ('SPREE', 25), ('SPREES', 36), ('SPREATHE', 64), ('SPREATHES', 81), ('SPRAT', 25), ('SPREETHE', 64), ('SIP', 9), ('SIPS', 16), ('SIR', 9), ('SIRI', 16), ('SIRE', 16), ('SIREE', 25), ('SIREES', 36), ('SIRES', 25), ('SRI', 9), ('SET', 9), ('SETS', 16), ('SESH', 16), ('SER', 9), ('SERIPH', 36), ('SERIPHS', 49), ('SERA', 16), ('SERAI', 25), ('SERIATE', 49), ('SERE', 16), ('SEE', 9), ('SEER', 16), ('SEETHE', 36), ('SEETHER', 49), ('SEES', 16), ('SERES', 25), ('SEREST', 36), ('SERER', 25), ('SEI', 9), ('SEIR', 16), ('SEA', 9), ('SEAR', 16), ('SEARE', 25), ('SEAREST', 49), ('SEARER', 36), ('SEAT', 16), ('SETA', 16), ('STERE', 25), ('STEER', 25), ('STREET', 36), ('STERES', 36), ('STEERER', 49), ('SPIRIEST', 64), ('SPRIEST', 49), ('STEERS', 36),
                ('STEERIES', 64), ('SESE', 16), ('SERS', 16), ('SERAIS', 36), ('SERIATES', 64), ('SERIES', 36), ('SEERS', 25), ('AESIR', 25), ('AETHER', 36), ('AETHERS', 49), ('ARAISE', 36), ('ARAISES', 49), ('ATE', 9), ('ATES', 16), ('ESS', 9), ('ESSE', 16), ('ESES', 16), ('EST', 9), ('ESTS', 16), ('ESTER', 25), ('ERS', 9), ('ERSES', 25), ('ERST', 16), ('ERA', 9), ('ERE', 9), ('ERES', 16), ('EAR', 9), ('EARS', 16), ('EARST', 25), ('EAT', 9), ('EATH', 16), ('EATHE', 25), ('ETH', 9), ('ETHE', 16), ('ETHER', 25), ('ETHERS', 36), ('ETHERISH', 64), ('ETHERIST', 64), ('ETHERISTS', 81), ('ETA', 9), ('TES', 9), ('TESSERA', 49), ('TERSE', 25), ('TERAI', 25), ('TERAIS', 36), ('TERES', 25), ('TEE', 9), ('TEES', 16), ('TEER', 16), ('TEERS', 25), ('TEETH', 25), ('TEETHE', 36), ('TEETHER', 49), ('TRES', 16), ('TRESS', 25), ('TREE', 16), ('TREES', 25), ('TEETHES', 49), ('TEETHERS', 64), ('THE', 9), ('THERE', 25), ('THERES', 36), ('THETE', 25), ('THETES', 36), ('THEE', 16), ('THEES', 25), ('THESP', 25), ('THESPS', 36), ('THESE', 25), ('THESES', 36), ('THEIR', 25), ('THEIRS', 36), ('THAE', 16), ('THAR', 16), ('THARS', 25), ('TEETER', 36), ('TEST', 16), ('TESTS', 25), ('TESTE', 25), ('TESTES', 36), ('TESTER', 36), ('TESTEE', 36), ('TESTEES', 49), ('TERSEST', 49), ('TERSER', 36), ('TERETE', 36), ('TEA', 9), ('TEAR', 16), ('TEARS', 25), ('TEARER', 36), ('TEETERS', 49), ('TAE', 9), ('TAES', 16), ('TAR', 9), ('TARS', 16), ('TARSI', 25), ('TARSIA', 36), ('TARP', 16), ('TARPS', 25), ('TARA', 16), ('TARE', 16), ('TARES', 25), ('TAI', 9), ('TAIRA', 25), ('HER', 9), ('HERE', 16), ('HERES', 25), ('HET', 9), ('HETS', 16), ('HETE', 16), ('HETES', 25), ('HES', 9), ('HESP', 16), ('HESPS', 25), ('HEST', 16), ('HESTS', 25), ('HERS', 16), ('HERSE', 25), ('HERIES', 36), ('HEREAT', 36), ('HERSES', 36), ('HERISSE', 49), ('HEIR', 16), ('HEIRS', 25), ('HEIRESS', 49), ('HEAR', 16), ('HEARS', 25), ('HEARSE', 36), ('HEARSES', 49), ('HEARE', 25), ('HEARES', 36), ('HEARER', 36), ('HEAT', 16), ('HETAIRIA', 64), ('HETAIRIST', 81), ('HETAIRISTS', 100), ('HETAIRA', 49), ('HETAIRAI', 64), ('HAE', 9), ('HAES', 16), ('HAERES', 36), ('HAET', 16), ('HARSH', 25), ('HARP', 16), ('HARPIST', 49), ('HARPISTS', 64), ('HARPS', 25), ('HARISH', 36), ('HARE', 16), ('HARES', 25), ('HAIR', 16), ('HAIRS', 25), ('HAIRST', 36), ('HAIRSTS', 49), ('HAT', 9), ('HATE', 16), ('HATES', 25), ('HATER', 25), ('HATERS', 36), ('EERIE', 25), ('EERIEST', 49), ('RESPIRE', 49), ('RESPIRES', 64), ('RERISE', 36), ('RERAISE', 49), ('REHEAR', 36), ('REHEARS', 49), ('REHEARSE', 64), ('REHEARSES', 81)]
    all_word_from_dict =  __all_words() # Put all words from the dict
    result = max_score_paths(board, all_word_from_dict)
    result = [(''.join([board[i][j] for i, j in path]), len(path)**2)
              for path in result]
    assert sorted(result) == sorted(expected)
