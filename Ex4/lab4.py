#############################################################
# FILE : lab4.py
# WRITER : Oryan Hassidim , oryan.hassidim , 319131579
# EXERCISE : intro2cs2 Lab4 2022
# DESCRIPTION: Nim Game.
# STUDENTS I DISCUSSED THE EXERCISE WITH: --
# WEB PAGES I USED:
# NOTES:
#############################################################

from random import randint

board = []
player = True


def init_board():
    global board
    board = [randint(1, 20) for i in range(10)]


def get_next_player():
    global player
    player = not player
    return player


def print_board():
    for row in board:
        print("|" * row, f"({row})")


def is_board_empty():
    return all(row == 0 for row in board)


def get_input():
    return int(input("Enter a row number: ")), int(input("Enter a number of matches: "))


def check_row_number_validity(row):
    return 0 < row <= len(board)


def check_amount_taken(row, amount):
    return 0 < amount <= board[row - 1]


def update_board(row, amount):
    board[row - 1] -= amount


def run_game():
    init_board()
    while not is_board_empty():
        print(f" player {'1' if player else '2'} turn")
        print_board()
        row, amount = get_input()
        if not check_row_number_validity(row) or not check_amount_taken(row, amount):
            print("Invalid input")
            continue
        update_board(row, amount)
        get_next_player()
    print("Game over")
    print("Player " + ("1" if player else "2") + " won!")

def main():
    flag = True
    while flag:
        run_game()
        flag = input("Play again? (y/n)") == "y"