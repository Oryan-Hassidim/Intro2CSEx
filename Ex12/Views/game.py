from tkinter import *
from MVVM.view_base import View
from PIL import ImageTk, Image
from random import randint, sample
from itertools import combinations
from math import floor


class GameView(View):
    "View of game page"
    __FONT_NAME = 'Comic Sans MS'

    def __init__(self, parent, view_model):
        "initializes new GameView"
        super().__init__(parent)
        self.__view_model = view_model

        self.__image = ImageTk.PhotoImage(Image.open("Assest/background.png"))
        self.create_image(0, 0, image=self.__image, anchor=NW)

        self.__navigate_in = []
        self.__navigate_out = []

        self.__init_board()
        self.__init_score()
        self.__init_timer()
        self.__init_correct_words()
        self.__init_current_word()
        self.__init_optional_words()

    def __init_board(self):
        "initializes the board"
        self.__cells = []
        vm_cells = self.__view_model.cells.get()
        for cell in vm_cells:
            self.__init_cell(cell)
        for vm_cell, (oval, text) in zip(vm_cells, self.__cells):
            self.__init_oval_animations(vm_cell.location.get(), oval)
            self.__init_text_animations(vm_cell.location.get(), text)

    def __init_cell(self, cell):
        "initializes a cell"
        oval = self.create_oval(0, 0, 0, 0)
        # bindings
        self._binding(lambda ij: self.coords(oval,
                                             200 + ij[0]*75, 150+ij[1]*75,
                                             275 + ij[0]*75, 225+ij[1]*75), cell.location)
        self._binding(lambda s: self.itemconfig(oval, fill='#cc00cc' if s else '#e0e0e0'),
                      cell.selected)
        text = self.create_text(0, 0, text='', font=(self.__FONT_NAME, 18))
        self._binding(lambda c: self.itemconfig(text, text=c), cell.char)
        self._binding(lambda ij: self.coords(text,
                                             200 + 75/2 + ij[0]*75, 150 + 75/2 + ij[1]*75), cell.location)
        self._binding(lambda e: self.itemconfig(text, fill='black' if e else '#808080',
                                                font=(self.__FONT_NAME, 20, 'bold') if e else ('Helvetica', 18)),
                      cell.enabled)

        # click
        def click(e):
            if cell.enabled.get():
                self.__view_model.select_cell(cell.location.get())
        Canvas.tag_bind(self, oval, '<Button-1>', click)
        Canvas.tag_bind(self, text, '<Button-1>', click)

        self.__cells.append((oval, text))

    def __init_oval_animations(self, ij, oval):
        "initializes the oval in and out animations"
        coords = self.coords(oval)
        start = (coords[0], coords[1] - 500, coords[2], coords[3] - 500)
        end = (coords[0], coords[1] + 500, coords[2], coords[3] + 500)
        i, j = ij
        delay = 0.16 - i * 0.4 - j * 0.1
        self.__navigate_in.append(lambda: self.coords(oval, *start))
        self.__navigate_in.append(
            lambda: self._animate(lambda *args: self.coords(oval, *args),
                                  start, coords, 2.5, "floats", View.square, delay))
        self.__navigate_out.append(
            lambda: self._animate(lambda *args: self.coords(oval, *args),
                                  coords, end, 2.5, "floats", View.square, delay))

    def __init_text_animations(self, ij, text):
        "initializes the text in and out animations"
        i, j = ij
        delay = 0.16 - i * 0.4 - j * 0.1
        coords = self.coords(text)
        start_t = (coords[0], coords[1] - 500)
        end_t = (coords[0], coords[1] + 500)
        self.__navigate_in.append(lambda: self.coords(text, *start_t))
        self.__navigate_in.append(
            lambda: self._animate(lambda *args: self.coords(text, *args),
                                  start_t, coords, 2.5, "floats", View.square, delay))
        self.__navigate_out.append(
            lambda: self._animate(lambda *args: self.coords(text, *args),
                                  coords, end_t, 2.5, "floats", View.square, delay))

    def __init_score(self):
        """initializes the scores label"""
        score_text = self.create_text((4 / 5) * View.WIDTH, 35, text='',
                                      font=(self.__FONT_NAME, 30, 'bold'))
        self._binding(lambda s: self.itemconfig(score_text, text='SCORE: ' + str(s)),
                      self.__view_model.score)

    def __init_timer(self):
        """initializes the timer"""
        # initialize the beads
        self.__time_beads = {}
        for bead in range(1, View.SECONDS + 1):
            self.__init_time_bead(bead)
        # initialize the rabbit image animation
        self.__rabbit_image = ImageTk.PhotoImage(
            Image.open("Assest/rabbit_small.png"))
        self.rabbit = self.create_image(
            50, View.HEIGHT - 60, image=self.__rabbit_image)
        self.__navigate_in.append(
            lambda:
            self._animate(lambda x: self.coords(self.rabbit, x, View.HEIGHT - 60),
                          60, View.WIDTH - 60, View.SECONDS, "float", View.linear, 3))
        # initialize time label
        self.__timer_label = self.create_text(
            View.WIDTH / 2, 35, text='', font=(self.__FONT_NAME, 30, 'bold'))
        self._binding(lambda s: self.itemconfig(self.__timer_label,
                                                text=f"{s//60}:{s%60:02d}",
                                                fill='black' if s > 5 else 'red'),
                      self.__view_model.seconds)
        # initialize the timer running
        self.__navigate_in.append(
            lambda:
            self._animate(lambda x: self.__view_model.seconds.set(floor(x)),
                          View.SECONDS + 1, 0, View.SECONDS + 1, 'float', View.linear, 3))

        # end game
        def end_game():
            if self.__view_model.game_over.get():
                self._navigate(self.__view_model.end_game())
        self.__view_model.game_over.add_observer(end_game)

    def __init_time_bead(self, bead):
        "initializes a time bead"
        size = 180 / 20
        x, y = 10 + size * ((bead - 1) % 20), 10 + size * ((bead - 1) // 20)
        oval = self.create_oval(x, y, x + size, y + size, fill='#704583')
        self.__time_beads[oval] = False

        self.__navigate_in.append(
            lambda:
            self._animate(
                lambda y: self.coords(oval, x, y, x+size, y+size),
                y, y + 370, 4, 'float',
                View.square, delay=View.SECONDS - bead + 3))

    def __init_correct_words(self):
        "initializes the correct words labels"
        start_x, start_y = 200 + 75*2, 115
        def xy(i): return (4 / 5) * View.WIDTH + (60 if i %
                                                  2 == 0 else -60), 100 + 25 * (i // 2)
        self.__correct_words = []

        def add_word():
            words = self.__view_model.correct_words.get()
            while len(self.__correct_words) < len(words):
                word = self.create_text(start_x, start_y,  text=words[-1],
                                        font=("Comic Sans MS", 30), fill='#00cc00')
                self.__correct_words.append(word)
                x, y = xy(len(self.__correct_words) - 1)

                def anim(x, y, r, g, b, ts, word=word):
                    color = View.color(r, g, b)
                    self.itemconfig(word, fill=color,
                                    font=("Comic Sans MS", round(ts)))
                    self.coords(word, x, y)
                self._animate(anim,
                              (start_x, start_y, 0, 204, 0, 30),
                              (x, y, 0, 0, 0, 18),
                              2.5, "floats", View.square)
        self.__view_model.correct_words.add_observer(add_word)

    def __init_current_word(self):
        "initializes the current word label"
        self.__current_word = self.create_text(
            200 + 75*2, 115, text='', font=('Comic Sans MS', 30, 'bold'))
        self._binding(lambda c: self.itemconfig(self.__current_word, text=c),
                      self.__view_model.current_word)

    def __init_optional_words(self):
        "initializes the optional words labels"
        optional = []
        locations = [(i, j)
                     for i in range(200, 200+150*3+1, 150)
                     for j in range(150+75*4+30, 150+75*4+30+20*4+1, 20)]

        def update(words):
            for word in optional:
                self.delete(word)
            optional.clear()
            locs = sample(locations, len(words))
            for word, (i, j) in zip(words, locs):
                text = self.create_text(i, j, text=word,
                                        font=(self.__FONT_NAME, 15), fill="purple")
                optional.append(text)
        self._binding(update, self.__view_model.optional_words)

    def _navigate_in(self):
        "plays all navigation in animations"
        for f in self.__navigate_in:
            f()
        return super()._navigate_in() + 3000

    def _navigate_out(self):
        "plays all navigation out animations"
        for f in self.__navigate_out:
            f()
        return super()._navigate_out() + 3000
