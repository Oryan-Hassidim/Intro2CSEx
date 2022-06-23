from tkinter import *
from MVVM.view_base import View
from PIL import ImageTk, Image
from math import sqrt


class WelcomeView(View):
    "Welcome view page. inherits from View class"

    __FONT_NAME = 'Comic Sans MS'

    def __init__(self, parent, view_model):
        "initializes new WelcomeView instance."
        super().__init__(parent)
        self.__view_model = view_model

        self.__image = ImageTk.PhotoImage(Image.open("Assest/background.png"))
        self.create_image(0, 0, image=self.__image, anchor=NW)
        self.__init_name()
        self.__init_welcome()
        self.__init_start_button()
        self.__init_high_scores()

    def __init_name(self):
        "initializes name entry and place holder."
        self.__name = StringVar()
        self._binding(lambda x: self.__name.set(x), self.__view_model.name)
        self.__name.trace(
            "w", lambda *args: self.__view_model.name.set(self.__name.get()))

        self.__name_entry = Entry(
            self,
            textvariable=self.__name,
            font=(self.__FONT_NAME, 20))
        self.__name_entry.place(
            relx=0.3, rely=0.5, relwidth=0.4, relheight=0.1)

        self.__name_entry.bind("<Return>", lambda *args: self.__start())

        holder = 'Enter Your Name'
        self.__place_holder = Label(self, text=holder, bg='white', fg='grey',
                                    font=(self.__FONT_NAME, 20), anchor='w',
                                    cursor=self.__name_entry['cursor'])
        self.__place_holder.place(relx=0.31, rely=0.51, relwidth=0.37, relheight=0.08)

        def place_holder(x):
            if x:
                self.__place_holder.place(relwidth=0.0, relheight=0.0)
            else:
                self.__place_holder.place(relwidth=0.37, relheight=0.08)
        self._binding(place_holder,
                      self.__view_model.name)
        self.__place_holder.bind("<Button-1>", lambda *args: self.__name_entry.focus())

    def __start(self):
        "starts the game - navigates to the game"
        if self.__view_model.name.get():
            self._navigate(self.__view_model.start())
        
    def __init_welcome(self):
        "initializes the Boggle image and rabbit image"
        self.__rabbit_image = ImageTk.PhotoImage(
            Image.open("Assest/welcome_rabbit_s.png"))
        self.__rabbit = self.create_image(-200, -200,
                                          image=self.__rabbit_image)
        self.__welcome_image = ImageTk.PhotoImage(
            Image.open("Assest/Boggle.png"))
        self.__welcome = self.create_image(-200, -200,
                                           image=self.__welcome_image)

    def __init_start_button(self):
        "initializes start button"
        self.__start_button = Button(
            self,
            text=">",
            command=self.__start,
            font=(self.__FONT_NAME, 20, 'bold'))
        self._binding(lambda x: self.__start_button.config(
            state="normal" if x else "disabled"), self.__view_model.name)
        self.__start_button.place(relx=0.615, rely=0.51,
                                  relwidth=0.07, relheight=0.08)

    def __init_high_scores(self):
        "initializes go to high scores button"
        self.__high_scores_button = Button(
            self,
            text="HIGH SCORES",
            command=lambda: self._navigate(self.__view_model.high_scores()),
            font=(self.__FONT_NAME, 14))
        self.__high_scores_button.place(relx=0.81, rely=0.9,
                                        relwidth=0.18, relheight=0.08)

    def _navigate_in(self):
        "plays animation in navigation in to view"
        self._animate(
            lambda y: self.coords(
                self.__welcome, View.WIDTH/2, y),
            -200.0, 200.0,
            2, easing=sqrt)
        self._animate(
            lambda x, y, w, h: self.__name_entry.place(
                relx=x, rely=y, relwidth=w, relheight=h),
            (0.5, 0.5, 0.0, 0.0), (0.3, 0.5, 0.4, 0.1),
            2, easing=sqrt)
        self._animate(
            lambda x, y, w, h: self.__start_button.place(
                relx=x, rely=y, relwidth=w, relheight=h),
            (0.5, 0.5, 0.0, 0.0), (0.62, 0.505, 0.07, 0.09),
            2, easing=sqrt)
        self._animate(
            lambda x, y, w, h: self.__high_scores_button.place(
                relx=x, rely=y, relwidth=w, relheight=h),
            (1.05, 0.9, 0.18, 0.08), (0.81, 0.9, 0.18, 0.08),
            2, easing=sqrt)
        self._animate(
            lambda y: self.coords(
                self.__rabbit, View.WIDTH/2, y),
            View.HEIGHT + 200.0, View.HEIGHT - 170,
            2, easing=sqrt)
        self._animate(
            lambda x, y, w, h: self.__place_holder.place(
                relx=x, rely=y, relwidth=w, relheight=h),
            (0.5, 0.5, 0.0, 0.0), (0.31, 0.51, 0.37, 0.08),
            2, easing=sqrt)
        return super()._navigate_in() + 2000

    def _navigate_out(self):
        "plays animation in navigation out of view"
        self._animate(
            lambda y: self.coords(
                self.__welcome, View.WIDTH/2, y),
            200.0, -200.0,
            2, easing=View.square)
        self._animate(
            lambda x, y, w, h: self.__name_entry.place(
                relx=x, rely=y, relwidth=w, relheight=h),
            (0.3, 0.5, 0.4, 0.1), (0.5, 0.5, 0.0, 0.0),
            2, easing=View.square)
        self._animate(
            lambda x, y, w, h: self.__start_button.place(
                relx=x, rely=y, relwidth=w, relheight=h),
            (0.62, 0.505, 0.07, 0.09), (0.5, 0.5, 0.0, 0.0),
            2, easing=View.square)
        self._animate(
            lambda x, y, w, h: self.__high_scores_button.place(
                relx=x, rely=y, relwidth=w, relheight=h),
            (0.81, 0.9, 0.18, 0.08), (1.05, 0.9, 0.18, 0.08),
            2, easing=View.square)
        self._animate(
            lambda y: self.coords(
                self.__rabbit, View.WIDTH/2, y),
            View.HEIGHT - 170, View.HEIGHT + 200,
            2, easing=View.square)
        if not self.__view_model.name.get():
            self._animate(
                lambda x, y, w, h: self.__place_holder.place(
                    relx=x, rely=y, relwidth=w, relheight=h),
                (0.31, 0.51, 0.37, 0.08), (0.5, 0.5, 0.0, 0.0),
                2, easing=View.square)
        return super()._navigate_out() + 2000
