from tkinter import *
from MVVM.view_base import View
from PIL import Image, ImageTk
import ViewModels


class EndGameView(View):
    """
    viewmodel for Endgame page
    """
    __FONT_NAME = 'Comic Sans MS'

    __RANK = {1: '1st', 2: '2nd', 3: '3rd'}

    def __init__(self, parent, view_model):
        super().__init__(parent)
        self.__view_model = view_model

        self.image = ImageTk.PhotoImage(Image.open("Assest/background.png"))
        self.create_image(0, 0, image=self.image, anchor=NW)

        self.__navigate_in = []
        self.__navigate_out = []

        self.__end_game_msg(view_model.new_high_score.get())
        self.__play_again()
        self.__quit_option()
        self.__init_high_scores()

    def __end_game_msg(self, hs):
        """sets and creates the endgame message appropriate for a new high
        score or not"""
        path = f"Assest/{'cliprabbittrumpet.png' if hs else 'timesup.png'}"
        end_msg = 'NEW HIGH SCORE!' if hs else 'TIME IS UP!'

        score = f'{self.__view_model.score.get()}'
        self.__rabbit = ImageTk.PhotoImage(Image.open(path))
        self.create_image(View.WIDTH / 4, View.HEIGHT / 2, image=self.__rabbit)
        self.create_text(View.WIDTH * 2 / 3, View.HEIGHT / 4,
                         text=end_msg,
                         font=(self.__FONT_NAME, 34, 'bold'))
        self.create_text(View.WIDTH * 2 / 3, View.HEIGHT * 3 / 8,
                         text=score,
                         font=(self.__FONT_NAME, 34))
        if hs:
            place = self.__view_model.all_time_rank.get()
            place_text = self.__RANK[place] if place in self.__RANK \
                else f'{place}th'
            rank_msg = f"YOU RANK {place_text}"
            self.create_text(View.WIDTH * 2 / 3, View.HEIGHT / 2,
                             text=rank_msg,
                             font=(self.__FONT_NAME, 24))

    def __play_again(self):
        """restarts to the game for the same player"""
        self.__play_again_button = Button(
            self,
            text="PLAY AGAIN",
            command=lambda: self._navigate(self.__view_model.play_again()),
            font=(self.__FONT_NAME, 14))
        self.__play_again_button.place(relx=0.615, rely=0.61,
                                       relwidth=0.18, relheight=0.08)

    def __quit_option(self):
        """quits the game"""
        self.__quit_button = Button(
            self,
            text="QUIT",
            command=self.quit,
            font=(self.__FONT_NAME, 14))
        self.__quit_button.place(relx=0.615, rely=0.71,
                                 relwidth=0.18, relheight=0.08)

    def __init_high_scores(self):
        """returns to the High Scores page"""
        self.__high_scores_button = Button(
            self,
            text="HIGH SCORES",
            command=lambda: self._navigate(self.__view_model.high_scores()),
            font=(self.__FONT_NAME, 14))
        self.__high_scores_button.place(relx=0.615, rely=0.81,
                                        relwidth=0.18, relheight=0.08)
