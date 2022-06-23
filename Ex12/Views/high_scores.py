from tkinter import *
from MVVM.view_base import View
from PIL import ImageTk, Image
import tkinter as tk


class HighScoresView(View):
    "View for high scores page."
    def __init__(self, parent, view_model):
        "initializes new HighScoresView"
        super().__init__(parent)

        self.__image = ImageTk.PhotoImage(Image.open("Assest/background.png"))
        self.create_image(0, 0, image=self.__image, anchor=NW)

        self.__view_model = view_model
        self.__list = []
        self._binding(self.__init_list, self.__view_model.high_scores)
        self.__init_title()
        self.__init_play_again()

    def __init_play_again(self):
        """
        Initialize the play again button.
        """
        again = self.__view_model.again.get()
        self.__play_again = tk.Button(self, text="Play Again" if again else "Back to Menu",
                                      command=lambda: self._navigate(
                                          self.__view_model.play_again()),
                                      font=('Consolas', 15 if again else 13))
        self.__play_again.place(relx=0.81, rely=0.9,
                                relwidth=0.18, relheight=0.08)

    def __init_title(self):
        """
        Initialize the title.
        """
        self.__title = self.create_text(View.WIDTH / 2, -50,
                                        text="High Scores", font=('Consolas', 50, 'bold'))

    def __init_list(self, high_scores):
        """
        Initialize the list of high scores.
        """
        for text in self.__list:
            self.delete(text)
        self.__list.clear()
        date_format = '%m/%d/%Y, %H:%M'
        x = View.WIDTH / 2
        for i, (name, date_time, scores) in enumerate(high_scores):
            text = f"{i+1:>2}. {name:<10s} {date_time.strftime(date_format):<25s} {scores:>3}"
            text = self.create_text(-x, 150 + i*30,
                                    text=text, font=('Consolas', 20))
            self.__list.append(text)

    def _navigate_in(self):
        """
        plays animations of the view when it is navigated in.
        """
        x = View.WIDTH / 2
        for i, text in enumerate(self.__list):
            self._animate(
                lambda x, text=text, i=i: self.coords(text, x, 150 + i*30),
                -x, x, 1, "float", View.linear, 0.1*i)
        self._animate(
            lambda y: self.coords(self.__title, x, y),
            -50.0, 70.0, 1, "float")
        self._animate(
            lambda x, y, w, h: self.__play_again.place(
                relx=x, rely=y, relwidth=w, relheight=h),
            (1.05, 0.9, 0.18, 0.08), (0.81, 0.9, 0.18, 0.08),
            1, easing=View.square)
        return super()._navigate_in() + 1000 + 100 * len(self.__list)

    def _navigate_out(self):
        """
        plays animations of the view when it is navigated out.
        """
        x = View.WIDTH // 2
        for i, text in enumerate(self.__list):
            self._animate(
                lambda x, i=i, t=text: self.coords(t, x, 150 + i*30),
                x, 3*x, 1, "float", View.linear, 0.1*i)
        self._animate(
            lambda y: self.coords(self.__title, x, y),
            70.0, -50.0, 1, "float")
        self._animate(
            lambda x, y, w, h: self.__play_again.place(
                relx=x, rely=y, relwidth=w, relheight=h),
            (0.81, 0.9, 0.18, 0.08), (1.05, 0.9, 0.18, 0.08),
            1, easing=View.square)
        return super()._navigate_out() + 1000 + 100 * len(self.__list)
