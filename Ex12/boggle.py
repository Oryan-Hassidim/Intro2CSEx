#######################################################################
# FILE : boggle.py
# WRITERS : Amit Nudelman-Perl, Oryan Hassidim,
# EXERCISE : intro2cs2 ex12 2022
# DESCRIPTION: boggle game
# STUDENTS I DISCUSSED THE EXERCISE WITH: each other
#######################################################################
import sys
from MVVM.view_base import View
import tkinter as tki
import os

from ViewModels.welcome import WelcomeViewModel
from Views.welcome import WelcomeView
from ViewModels.game import GameViewModel
from Views.game import GameView
from ViewModels.end_game import EndGameViewModel
from Views.end_game import EndGameView
from ViewModels.high_scores import HighScoresViewModel
from Views.high_scores import HighScoresView


def main():
    "main function for running the game."
    tk = tki.Tk()
    tk.title("Boggle")
    tk.iconbitmap("Assest/boggle.ico")
    tk.geometry("{}x{}".format(View.WIDTH, View.HEIGHT))
    tk.resizable(0, 0)
    View.tk = tk
    View.add_view(WelcomeViewModel, WelcomeView)
    View.add_view(GameViewModel, GameView)
    View.add_view(EndGameViewModel, EndGameView)
    View.add_view(HighScoresViewModel, HighScoresView)

    view = WelcomeView(tk, WelcomeViewModel())
    view.pack(fill=tki.BOTH, expand=True)
    view._navigate_in()
    tk.mainloop()


if __name__ == "__main__":
    sys.exit(int(main() or 0))
