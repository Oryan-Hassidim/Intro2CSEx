import tkinter as tki
from typing import Any, Optional, List, Tuple, Dict


INPUT = [None, 'Right', None, None, None, None, 'Down', 'Left', None, 'Up', None, None, None, None, 'Right', 'Down', None, 'Left', 'Up', None, None, None, None, 'Right']
EXPECTED = [(0, {(20, 15): 'black', (20, 14): 'black', (20, 13): 'black', (29, 19): 'red', (8, 5): 'green', (21, 16): 'green', (38, 2): 'green'}), (0, {(8, 5): 'green', (21, 16): 'green', (38, 2): 'green', (20, 16): 'black', (20, 15): 'black', (20, 14): 'black', (29, 19): 'red'}), (4, {(8, 5): 'green', (38, 2): 'green', (35, 29): 'green', (21, 16): 'black', (20, 16): 'black', (20, 15): 'black', (29, 19): 'red'}), (4, {(8, 5): 'green', (38, 2): 'green', (35, 29): 'green', (22, 16): 'black', (21, 16): 'black', (20, 16): 'black', (20, 15): 'black', (29, 19): 'red'}), (4, {(8, 5): 'green', (38, 2): 'green', (35, 29): 'green', (23, 16): 'black', (22, 16): 'black', (21, 16): 'black', (20, 16): 'black', (20, 15): 'black', (29, 19): 'red'}), (4, {(8, 5): 'green', (38, 2): 'green', (35, 29): 'green', (24, 16): 'black', (23, 16): 'black', (22, 16): 'black', (21, 16): 'black', (20, 16): 'black', (20, 15): 'black', (29, 19): 'red'}), (4, {(8, 5): 'green', (38, 2): 'green', (35, 29): 'green', (25, 16): 'black', (24, 16): 'black', (23, 16): 'black', (22, 16): 'black', (21, 16): 'black', (20, 16): 'black', (29, 19): 'red'}), (4, {(8, 5): 'green', (38, 2): 'green', (35, 29): 'green', (25, 15): 'black', (25, 16): 'black', (24, 16): 'black', (23, 16): 'black', (22, 16): 'black', (21, 16): 'black', (29, 19): 'red'}), (4, {(8, 5): 'green', (38, 2): 'green', (35, 29): 'green', (24, 15): 'black', (25, 15): 'black', (25, 16): 'black', (24, 16): 'black', (23, 16): 'black', (22, 16): 'black', (29, 19): 'red'}), (4, {(8, 5): 'green', (38, 2): 'green', (35, 29): 'green', (23, 15): 'black', (24, 15): 'black', (25, 15): 'black', (25, 16): 'black', (24, 16): 'black', (23, 16): 'black', (29, 19): 'red'}), (4, {(8, 5): 'green', (38, 2): 'green', (35, 29): 'green', (23, 16): 'black', (23, 15): 'black', (24, 15): 'black', (25, 15): 'black', (25, 16): 'black', (24, 16): 'black', (29, 19): 'red'}), (4, {(8, 5): 'green', (38, 2): 'green', (35, 29): 'green', (23, 17): 'black', (23, 16): 'black', (23, 15): 'black', (24, 15): 'black', (25, 15): 'black', (25, 16): 'black', (29, 19): 'red'}), (4, {(8, 5): 'green', (38, 2): 'green', (35, 29): 'green', (23, 18): 'black', (23, 17): 'black', (23, 16): 'black', (23, 15): 'black', (24, 15): 'black', (25, 15): 'black', (29, 19): 'red'}), (4, {(8, 5): 'green', (38, 2): 'green', (35, 29): 'green', (23, 19): 'black', (23, 18): 'black', (23, 17): 'black', (23, 16): 'black', (23, 15): 'black', (24, 15): 'black', (29, 19): 'red'}), (4, {(8, 5): 'green', (38, 2): 'green', (35, 29): 'green', (23, 20): 'black', (23, 19): 'black', (23, 18): 'black', (23, 17): 'black', (23, 16): 'black', (23, 15): 'black', (29, 19): 'red'}), (4, {(8, 5): 'green', (38, 2): 'green', (35, 29): 'green', (24, 20): 'black', (23, 20): 'black', (23, 19): 'black', (23, 18): 'black', (23, 17): 'black', (23, 16): 'black', (29, 19): 'red'}), (4, {(8, 5): 'green', (38, 2): 'green', (35, 29): 'green', (24, 19): 'black', (24, 20): 'black', (23, 20): 'black', (23, 19): 'black', (23, 18): 'black', (23, 17): 'black', (29, 19): 'red'}), (4, {(8, 5): 'green', (38, 2): 'green', (35, 29): 'green', (24, 18): 'black', (24, 19): 'black', (24, 20): 'black', (23, 20): 'black', (23, 19): 'black', (23, 18): 'black', (29, 19): 'red'}), (4, {(8, 5): 'green', (38, 2): 'green', (35, 29): 'green', (23, 18): 'black', (24, 18): 'black', (24, 19): 'black', (24, 20): 'black', (23, 20): 'black', (23, 19): 'black', (29, 19): 'red'}), (4, {(8, 5): 'green', (38, 2): 'green', (35, 29): 'green', (23, 19): 'black', (23, 18): 'black', (24, 18): 'black', (24, 19): 'black', (24, 20): 'black', (23, 20): 'black', (29, 19): 'red'}), (4, {(8, 5): 'green', (38, 2): 'green', (35, 29): 'green', (23, 20): 'black', (23, 19): 'black', (23, 18): 'black', (24, 18): 'black', (24, 19): 'black', (24, 20): 'black', (29, 19): 'red'}), (4, {(8, 5): 'green', (38, 2): 'green', (35, 29): 'green', (23, 21): 'black', (23, 20): 'black', (23, 19): 'black', (23, 18): 'black', (24, 18): 'black', (24, 19): 'black', (29, 19): 'red'}), (4, {(8, 5): 'green', (38, 2): 'green', (35, 29): 'green', (23, 22): 'black', (23, 21): 'black', (23, 20): 'black', (23, 19): 'black', (23, 18): 'black', (24, 18): 'black', (29, 19): 'red'}), (4, {(8, 5): 'green', (38, 2): 'green', (35, 29): 'green', (23, 23): 'black', (23, 22): 'black', (23, 21): 'black', (23, 20): 'black', (23, 19): 'black', (23, 18): 'black', (29, 19): 'red'}), (4, {(8, 5): 'green', (38, 2): 'green', (35, 29): 'green', (24, 23): 'black', (23, 23): 'black', (23, 22): 'black', (23, 21): 'black', (23, 20): 'black', (23, 19): 'black', (29, 19): 'orange'}), (4, {(8, 5): 'green', (38, 2): 'green', (35, 29): 'green', (25, 23): 'black', (24, 23): 'black', (23, 23): 'black', (23, 22): 'black', (23, 21): 'black', (23, 20): 'black', (29, 20): 'orange', (28, 19): 'orange', (29, 18): 'orange', (30, 19): 'orange'}), (4, {(8, 5): 'green', (38, 2): 'green', (35, 29): 'green', (26, 23): 'black', (25, 23): 'black', (24, 23): 'black', (23, 23): 'black', (23, 22): 'black', (23, 21): 'black', (29, 21): 'orange', (30, 20): 'orange', (27, 19): 'orange', (28, 20): 'orange', (29, 17): 'orange', (28, 18): 'orange', (31, 19): 'orange', (30, 18): 'orange'}), (4, {(8, 5): 'green', (38, 2): 'green', (35, 29): 'green', (27, 23): 'black', (26, 23): 'black', (25, 23): 'black', (24, 23): 'black', (23, 23): 'black', (23, 22): 'black', (29, 22): 'orange', (30, 21): 'orange', (31, 20): 'orange', (26, 19): 'orange', (27, 20): 'orange', (28, 21): 'orange', (29, 16): 'orange', (28, 17): 'orange', (27, 18): 'orange', (32, 19): 'orange', (31, 18): 'orange', (30, 17): 'orange'}), (4, {(8, 5): 'green', (38, 2): 'green', (35, 29): 'green', (28, 23): 'black', (27, 23): 'black', (26, 23): 'black', (25, 23): 'black', (24, 23): 'black', (23, 23): 'black', (29, 23): 'orange', (30, 22): 'orange', (31, 21): 'orange', (32, 20): 'orange', (25, 19): 'orange', (26, 20): 'orange', (27, 21): 'orange', (28, 22): 'orange', (29, 15): 'orange', (28, 16): 'orange', (27, 17): 'orange', (26, 18): 'orange', (33, 19): 'orange', (32, 18): 'orange', (31, 17): 'orange', (30, 16): 'orange'}), (5, {(8, 5): 'green', (38, 2): 'green', (35, 29): 'green', (29, 23): 'orange', (28, 23): 'black', (27, 23): 'black', (26, 23): 'black', (25, 23): 'black', (24, 23): 'black', (30, 22): 'orange', (31, 21): 'orange', (32, 20): 'orange', (25, 19): 'orange', (26, 20): 'orange', (27, 21): 'orange', (28, 22): 'orange', (29, 15): 'orange', (28, 16): 'orange', (27, 17): 'orange', (26, 18): 'orange', (33, 19): 'orange', (32, 18): 'orange', (31, 17): 'orange', (30, 16): 'orange'})]
ACTUAL = [(0, {(8, 5): 'green', (20, 13): 'black', (20, 14): 'black', (20, 15): 'black', (21, 16): 'green', (29, 19): 'red', (38, 2): 'green'}), (0, {(8, 5): 'green', (20, 14): 'black', (20, 15): 'black', (20, 16): 'black', (21, 16): 'green', (29, 19): 'red', (38, 2): 'green'}), (4, {(8, 5): 'green', (20, 15): 'black', (20, 16): 'black', (21, 16): 'black', (29, 19): 'red', (35, 29): 'green', (38, 2): 'green'}), (4, {(8, 5): 'green', (20, 15): 'black', (20, 16): 'black', (21, 16): 'black', (22, 16): 'black', (29, 19): 'red', (35, 29): 'green', (38, 2): 'green'}), (4, {(8, 5): 'green', (20, 15): 'black', (20, 16): 'black', (21, 16): 'black', (22, 16): 'black', (23, 16): 'black', (29, 19): 'red', (35, 29): 'green', (38, 2): 'green'}), (4, {(8, 5): 'green', (20, 15): 'black', (20, 16): 'black', (21, 16): 'black', (22, 16): 'black', (23, 16): 'black', (24, 16): 'black', (29, 19): 'red', (35, 29): 'green', (38, 2): 'green'}), (4, {(8, 5): 'green', (20, 16): 'black', (21, 16): 'black', (22, 16): 'black', (23, 16): 'black', (24, 16): 'black', (25, 16): 'black', (29, 19): 'red', (35, 29): 'green', (38, 2): 'green'}), (4, {(8, 5): 'green', (21, 16): 'black', (22, 16): 'black', (23, 16): 'black', (24, 16): 'black', (25, 15): 'black', (25, 16): 'black', (29, 19): 'red', (35, 29): 'green', (38, 2): 'green'}), (4, {(8, 5): 'green', (22, 16): 'black', (23, 16): 'black', (24, 15): 'black', (24, 16): 'black', (25, 15): 'black', (25, 16): 'black', (29, 19): 'red', (35, 29): 'green', (38, 2): 'green'}), (4, {(8, 5): 'green', (23, 15): 'black', (23, 16): 'black', (24, 15): 'black', (24, 16): 'black', (25, 15): 'black', (25, 16): 'black', (29, 19): 'red', (35, 29): 'green', (38, 2): 'green'}), (4, {(8, 5): 'green', (23, 15): 'black', (23, 16): 'black', (24, 15): 'black', (24, 16): 'black', (25, 15): 'black', (25, 16): 'black', (29, 19): 'red', (35, 29): 'green', (38, 2): 'green'}), (4, {(8, 5): 'green', (23, 15): 'black', (23, 16): 'black', (23, 17): 'black', (24, 15): 'black', (25, 15): 'black', (25, 16): 'black', (29, 19): 'red', (35, 29): 'green', (38, 2): 'green'}), (4, {(8, 5): 'green', (23, 15): 'black', (23, 16): 'black', (23, 17): 'black', (23, 18): 'black', (24, 15): 'black', (25, 15): 'black', (29, 19): 'red', (35, 29): 'green', (38, 2): 'green'}), (4, {(8, 5): 'green', (23, 15): 'black', (23, 16): 'black', (23, 17): 'black', (23, 18): 'black', (23, 19): 'black', (24, 15): 'black', (29, 19): 'red', (35, 29): 'green', (38, 2): 'green'}), (4, {(8, 5): 'green', (23, 15): 'black', (23, 16): 'black', (23, 17): 'black', (23, 18): 'black', (23, 19): 'black', (23, 20): 'black', (29, 19): 'red', (35, 29): 'green', (38, 2): 'green'}), (4, {(8, 5): 'green', (23, 16): 'black', (23, 17): 'black', (23, 18): 'black', (23, 19): 'black', (23, 20): 'black', (24, 20): 'black', (29, 19): 'red', (35, 29): 'green', (38, 2): 'green'}), (4, {(8, 5): 'green', (23, 17): 'black', (23, 18): 'black', (23, 19): 'black', (23, 20): 'black', (24, 19): 'black', (24, 20): 'black', (29, 19): 'red', (35, 29): 'green', (38, 2): 'green'}), (4, {(8, 5): 'green', (23, 18): 'black', (23, 19): 'black', (23, 20): 'black', (24, 18): 'black', (24, 19): 'black', (24, 20): 'black', (29, 19): 'red', (35, 29): 'green', (38, 2): 'green'}), (4, {(8, 5): 'green', (23, 18): 'black', (23, 19): 'black', (23, 20): 'black', (24, 18): 'black', (24, 19): 'black', (24, 20): 'black', (29, 19): 'red', (35, 29): 'green', (38, 2): 'green'}), (4, {(8, 5): 'green', (23, 18): 'black', (23, 19): 'black', (23, 20): 'black', (24, 18): 'black', (24, 19): 'black', (24, 20): 'black', (29, 19): 'red', (35, 29): 'green', (38, 2): 'green'}), (4, {(8, 5): 'green', (23, 18): 'black', (23, 19): 'black', (23, 20): 'black', (24, 18): 'black', (24, 19): 'black', (24, 20): 'black', (29, 19): 'red', (35, 29): 'green', (38, 2): 'green'}), (4, {(8, 5): 'green', (23, 18): 'black', (23, 19): 'black', (23, 20): 'black', (23, 21): 'black', (24, 18): 'black', (24, 19): 'black', (29, 19): 'red', (35, 29): 'green', (38, 2): 'green'}), (4, {(8, 5): 'green', (23, 18): 'black', (23, 19): 'black', (23, 20): 'black', (23, 21): 'black', (23, 22): 'black', (24, 18): 'black', (29, 19): 'red', (35, 29): 'green', (38, 2): 'green'}), (4, {(8, 5): 'green', (23, 18): 'black', (23, 19): 'black', (23, 20): 'black', (23, 21): 'black', (23, 22): 'black', (23, 23): 'black', (29, 19): 'red', (35, 29): 'green', (38, 2): 'green'}), (4, {(8, 5): 'green', (23, 19): 'black', (23, 20): 'black', (23, 21): 'black', (23, 22): 'black', (23, 23): 'black', (24, 23): 'black', (29, 19): 'orange', (35, 29): 'green', (38, 2): 'green'}), (4, {(8, 5): 'green', (23, 20): 'black', (23, 21): 'black', (23, 22): 'black', (23, 23): 'black', (24, 23): 'black', (25, 23): 'black', (28, 19): 'orange', (29, 18): 'orange', (29, 20): 'orange', (30, 19): 'orange', (35, 29): 'green', (38, 2): 'green'}), (4, {(8, 5): 'green', (23, 21): 'black', (23, 22): 'black', (23, 23): 'black', (24, 23): 'black', (25, 23): 'black', (26, 23): 'black', (27, 19): 'orange', (28, 18): 'orange', (28, 20): 'orange', (29, 17): 'orange', (29, 21): 'orange', (30, 18): 'orange', (30, 20): 'orange', (31, 19): 'orange', (35, 29): 'green', (38, 2): 'green'}), (4, {(8, 5): 'green', (23, 22): 'black', (23, 23): 'black', (24, 23): 'black', (25, 23): 'black', (26, 19): 'orange', (26, 23): 'black', (27, 18): 'orange', (27, 20): 'orange', (27, 23): 'black', (28, 17): 'orange', (28, 21): 'orange', (29, 16): 'orange', (29, 22): 'orange', (30, 17): 'orange', (30, 21): 'orange', (31, 18): 'orange', (31, 20): 'orange', (32, 19): 'orange', (35, 29): 'green', (38, 2): 'green'}), (4, {(8, 5): 'green', (23, 23): 'black', (24, 23): 'black', (25, 19): 'orange', (25, 23): 'black', (26, 18): 'orange', (26, 20): 'orange', (26, 23): 'black', (27, 17): 'orange', (27, 21): 'orange', (27, 23): 'black', (28, 16): 'orange', (28, 22): 'orange', (28, 23): 'black', (29, 15): 'orange', (29, 23): 'orange', (30, 16): 'orange', (30, 22): 'orange', (31, 17): 'orange', (31, 21): 'orange', (32, 18): 'orange', (32, 20): 'orange', (33, 19): 'orange', (35, 29): 'green', (38, 2): 'green'}), (4, {(2, 23): 'red', (8, 5): 'green', (24, 23): 'black', (25, 23): 'black', (26, 23): 'black', (27, 23): 'black', (28, 23): 'black', (29, 23): 'black', (35, 29): 'green', (38, 2): 'green'})]


WIDTH = 40
HEIGHT = 30
CELL_SIZE = 15


class GameDisplay:
    def __init__(self) -> None:
        """Creates a new game display object and initializes it"""
        # placed this import in here to solve circular import issues.
        self._round_num = 0
        self._root = tki.Tk()
        self._root.title('Snake Compare')
        self._root.bind('<KeyPress>', self._key_press)

        self._score_var = tki.StringVar()
        self._level_var = tki.StringVar()
        self._input = [''] + INPUT
        self._expected = EXPECTED
        self._actual = ACTUAL
        if len(self._actual) != len(self._expected):
            raise ValueError("Actual and expected are not the same length")

        self._init_level_frame()
        self._init_score_frame()
        # self._init_input_frame()

        self._expected_canvas = tki.Canvas(self._root, bg="white",
                                           width=WIDTH * CELL_SIZE,
                                           height=HEIGHT * CELL_SIZE)
        self._expected_canvas.pack(side=tki.RIGHT)
        self._expected_to_draw: List[Tuple[int, int, str]] = list()
        self._expected_already_drawn: Dict[Tuple[int, int, str], int] = dict()

        self._actual_canvas = tki.Canvas(self._root, bg="white",
                                         width=WIDTH * CELL_SIZE,
                                         height=HEIGHT * CELL_SIZE)
        self._actual_canvas.pack(side=tki.LEFT)
        self._actual_to_draw: List[Tuple[int, int, str]] = list()
        self._actual_already_drawn: Dict[Tuple[int, int, str], int] = dict()

        self._root.resizable(False, False)
        self.key_click: Optional[str] = None
        self._key_click_round: int = 0
        self._update_drawing()

    def _key_press(self, e: tki.Event) -> None:
        """
        Internal: This method is called when a key is pressed.
        :param event: The event that triggered this method
        :return: None
        """
        if e.keysym in ["Left", "Down"] and self._round_num > 0:
            self._level_down()
        elif e.keysym in ["Right", "Up"] and self._round_num < len(self._actual) - 1:
            self._level_up()

    def _init_score_frame(self) -> None:
        """
        Internal: This method initializes the score frame
        :return: None
        """
        self._score_frame = tki.Frame(self._root)
        self._score_frame.pack(side=tki.TOP)

        self.show_score("Not Set")
        self._score_label = tki.Label(self._score_frame,
                                      borderwidth=2,
                                      relief="ridge",
                                      textvariable=self._score_var,
                                      font=("Courier", 22))

        self._score_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)

        self._score_frame.grid_rowconfigure(0, weight=1)

    def _init_level_frame(self) -> None:
        """
        Internal: This method initializes the score frame
        :return: None
        """
        self._level_frame = tki.Frame(self._root)
        self._level_frame.pack(side=tki.TOP)

        self._left_button = tki.Button(self._level_frame,
                                       text="<",
                                       command=self._level_down,
                                       font=("Courier", 22))
        self._left_button.grid(row=0, column=0, sticky="w", padx=10, pady=10)

        self._level_var.set("Level: Not Set")
        self._level_label = tki.Label(self._level_frame,
                                      borderwidth=2,
                                      relief="ridge",
                                      textvariable=self._level_var,
                                      font=("Courier", 22))
        self._level_label.grid(row=0, column=1, sticky="w", padx=10, pady=10)

        self._right_button = tki.Button(self._level_frame,
                                        text=">",
                                        command=self._level_up,
                                        font=("Courier", 22))
        self._right_button.grid(row=0, column=2, sticky="w", padx=10, pady=10)

        self._level_frame.grid_rowconfigure(0, weight=1)

    def _level_up(self) -> None:
        """
        Internal: This method increases the level of the game
        :return: None
        """
        self._round_num += 1
        self._update_drawing()

    def _level_down(self) -> None:
        """
        Internal: This method decreases the level of the game
        :return: None
        """
        self._round_num -= 1
        self._update_drawing()

    def _init_input_frame(self) -> None:
        """
        Internal: This method initializes the score frame
        :return: None
        """
        self._input_frame = tki.Frame(self._root)
        self._input_frame.pack(side=tki.BOTTOM)

        self._actual_label = tki.Label(self._input_frame,
                                       borderwidth=0,
                                       relief="ridge",
                                       text="actual:",
                                       font=("Courier", 22))

        self._actual_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self._expected_label = tki.Label(self._input_frame,
                                         borderwidth=0,
                                         relief="ridge",
                                         text="expected:",
                                         font=("Courier", 22))

        self._expected_label.grid(
            row=1, column=0, sticky="w", padx=10, pady=10)

        self._actual_var = tki.StringVar()
        self._actual_var.trace(
            "w", lambda _, __, ___, sv=self._actual_var: self._actual_input_changed())
        self._actual_input = tki.Entry(self._input_frame,
                                       borderwidth=2,
                                       width=WIDTH,
                                       relief="ridge",
                                       font=("Courier", 22),
                                       textvariable=self._actual_var)
        self._actual_input.grid(row=0, column=1, sticky="w", padx=10, pady=10)
        self._expected_var = tki.StringVar()
        self._expected_var.trace(
            "w", lambda _, __, ___, sv=self._actual_var: self._expected_input_changed())
        self._expected_input = tki.Entry(self._input_frame,
                                         borderwidth=2,
                                         width=WIDTH,
                                         relief="ridge",
                                         font=("Courier", 22),
                                         textvariable=self._expected_var)
        self._expected_input.grid(
            row=1, column=1, sticky="w", padx=10, pady=10)

        self._input_frame.grid_rowconfigure(0, weight=1)
        self._input_frame.grid_rowconfigure(1, weight=1)
        self._input_frame.grid_columnconfigure(0, weight=1)
        self._input_frame.grid_columnconfigure(1, weight=1)

    def _actual_input_changed(self) -> None:
        """
        Internal: This method updates the actual input
        :return: None
        """
        try:
            self._actual = eval(self._actual_input.get())
        except:
            self._actual = []
        self._update_drawing()

    def _expected_input_changed(self) -> None:
        """
        Internal: This method updates the expected input
        :return: None
        """
        try:
            self._expected = eval(self._expected_input.get())
        except:
            self._expected = []
        self._update_drawing()

    def start(self) -> None:
        """
        Internal: Starts the program: calls the main method and runs the GUI.
        :return: None
        """
        #self._root.after(500, self._game_control_thread.start)
        #self._root.after(1000, self._check_end)

        self._root.mainloop()

    def _buffer_draw_cell(self, x: int, y: int, color: str, canvas, same=True) -> int:
        """
        Internal: internal method to draw the x,y cell in color
        :param x: coordinate at x
        :param y: coordinate at y
        :param color: the color we wish to draw
        :return: None
        """
        if x < 0 or x >= WIDTH or \
                y < 0 or y >= HEIGHT:
            raise ValueError(
                "cell index out of bounds of the board: " + str((x, y)))

        # setting the coordinates of the board correctly,
        # the y axis needs to point up.
        # the following line adjusts this.
        y = HEIGHT - y
        return canvas.create_rectangle(
            x * CELL_SIZE, (y - 1) * CELL_SIZE,
            (x + 1) * CELL_SIZE, y * CELL_SIZE,
            width=0 if same else 3,
            fill=color, outline=color if same else "blue")

    def _update_drawing(self) -> None:
        """
        Internal: method to update drawing
        :return: None
        """
        try:
            ac_points, ac_dict = self._actual[self._round_num]
            ex_points, ex_dict = self._expected[self._round_num]
        except IndexError:
            return
        try:
            key = self._input[self._round_num]
        except:
            key = None

        self._actual_canvas.delete("all")
        self._expected_canvas.delete("all")
        to_draw = {(x, y, color) for (x, y), color in ac_dict.items()}

        for x, y, color in to_draw:
            ind = self._actual_already_drawn.get((x, y, color), None)
            if ind is None:
                ind = self._buffer_draw_cell(x, y, color, self._actual_canvas,
                                             ac_dict.get((x, y), None) == ex_dict.get((x, y), None))

        to_draw = {(x, y, color) for (x, y), color in ex_dict.items()}
        for rect in self._expected_already_drawn:
            if rect not in to_draw:
                self._expected_canvas.delete(
                    self._expected_already_drawn[rect])

        for x, y, color in to_draw:
            ind = self._expected_already_drawn.get((x, y, color), None)
            if ind is None:
                ind = self._buffer_draw_cell(x, y, color, self._expected_canvas,
                                             ac_dict.get((x, y), None) == ex_dict.get((x, y), None))

        self.show_score(f"Actual: {ac_points}, Expected: {ex_points}")
        self._level_var.set(
            f"Level: {self._round_num} of {len(self._actual)}\nKey: {key}")

        self._right_button.config(state="normal" if self._round_num < len(
            self._actual) - 1 else "disabled")
        self._left_button.config(
            state="normal" if self._round_num > 0 else "disabled")

        # bold if false
        self._score_label.config(
            fg="black" if ac_points == ex_points else "blue",
            font=("Courier", 22, "bold" if ac_points != ex_points else "normal"))

    def show_score(self, val: Any) -> None:
        """
        This method updates the currently shown score on the board.
        :param val: the score we wish to display
        :return: None
        """
        self._score_var.set("Score: " + str(val))


if __name__ == "__main__":
    gd = GameDisplay()
    gd.start()
