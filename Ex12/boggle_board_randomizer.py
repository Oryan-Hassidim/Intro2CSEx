import random

BOARD_SIZE = 4
LETTERS = [
    ['A', 'E', 'A', 'N', 'E', 'G'],
    ['A', 'H', 'S', 'P', 'C', 'O'],
    ['A', 'S', 'P', 'F', 'F', 'K'],
    ['O', 'B', 'J', 'O', 'A', 'B'],
    ['I', 'O', 'T', 'M', 'U', 'C'],
    ['R', 'Y', 'V', 'D', 'E', 'L'],
    ['L', 'R', 'E', 'I', 'X', 'D'],
    ['E', 'I', 'U', 'N', 'E', 'S'],
    ['W', 'N', 'G', 'E', 'E', 'H'],
    ['L', 'N', 'H', 'N', 'R', 'Z'],
    ['T', 'S', 'T', 'I', 'Y', 'D'],
    ['O', 'W', 'T', 'O', 'A', 'T'],
    ['E', 'R', 'T', 'T', 'Y', 'L'],
    ['T', 'O', 'E', 'S', 'S', 'I'],
    ['T', 'E', 'R', 'W', 'H', 'V'],
    ['N', 'U', 'I', 'H', 'M', 'QU']
]


def randomize_board(dice_list=LETTERS):
    dice_indices = list(range(len(dice_list)))
    random.shuffle(dice_indices)
    dice_indices_iter = iter(dice_indices)
    board = []
    for i in range(BOARD_SIZE):
        row = []
        for j in range(BOARD_SIZE):
            die = dice_list[next(dice_indices_iter)]
            letter = random.choice(die)
            row.append(letter)
        board.append(row)
    return board

if __name__=="__main__":
    from pprint import pprint
    pprint(randomize_board())
