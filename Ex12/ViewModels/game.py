from MVVM.notified_property import NotifiedProperty
from boggle_board_randomizer import randomize_board
from ViewModels.end_game import EndGameViewModel
from dataclasses import dataclass
from random import sample
import ex12_utils


@dataclass
class Cell:
    char: NotifiedProperty
    enabled: NotifiedProperty
    location: NotifiedProperty
    selected: NotifiedProperty


class GameViewModel:
    """
    ViewModel for Game page.
    """
    def __init__(self, name: str):
        self.__name = NotifiedProperty(name)
        board = randomize_board()
        self.__board = board
        self.__init_cells()
        self.__selected_cells = NotifiedProperty([])
        self.__current_word = NotifiedProperty('')
        max_paths = ex12_utils.max_score_paths(board, self.__all_words())
        self.__words = [''.join(board[i][j] for i,j in path)
                        for path in max_paths]
        self.__all_optional_words = self.__words
        items = min(5, len(self.__all_optional_words))
        self.__optional_words = NotifiedProperty(
            sample(self.__all_optional_words, items))
        self.__correct_words = NotifiedProperty([])
        self.__score = NotifiedProperty(0)
        self.__seconds = NotifiedProperty(60*3)
        self.__seconds.add_observer(self.__tick)
        self.__game_over = NotifiedProperty(False)

    def __init_cells(self):
        "initialize the cells"
        board = self.__board
        cells = []
        for i, row in enumerate(board):
            for j, char in enumerate(row):
                cells.append(
                    Cell(
                        NotifiedProperty(char),
                        NotifiedProperty(True),
                        NotifiedProperty((i, j)),
                        NotifiedProperty(False)))
        self.__cells = NotifiedProperty(cells)

    def clear(self):
        "clears the selected cells"
        self.__selected_cells.get().clear()
        self.__current_word.set('')
        self.__update_cells()
        self.__selected_cells.notify_changed()

    def __update_cells(self):
        "updates the cells"
        selected = self.__selected_cells.get()
        last = selected[-1] if len(selected) > 0 else None
        for cell in self.__cells.get():
            i, j = cell.location.get()
            cell.selected.set((i, j) in selected)
            enabled = last is None or (
                abs(i - last[0]) <= 1
                and abs(j - last[1]) <= 1
                and ((i, j) == last or (i, j) not in selected))
            cell.enabled.set(enabled)

    def __tick(self):
        "method which called every second"
        if self.__seconds.get() <= 0:
            self.optional_words.set([])
            for cell in self.__cells.get():
                cell.enabled.set(False)
            self.__current_word.set('')
            self.__game_over.set(True)

    def end_game(self):
        "ends the game, and returns EndGameViewModel"
        return EndGameViewModel(
            self.__name.get(),
            self.__score.get(),
            self.__correct_words.get())

    def select_cell(self, ij):
        "command to select a cell"
        i, j = ij
        selected = self.__selected_cells.get()
        # remove
        if (i, j) in selected:
            if (i, j) == selected[-1]:
                selected.remove((i, j))
                words = self.__words
            else:
                return
        # add
        else:
            selected.append((i, j))
            words = self.__all_optional_words

        current_word = ''.join(self.__board[i][j] for i, j in selected)

        # check win
        if current_word in self.__all_optional_words:
            self.__score.set(self.__score.get() + len(selected) ** 2)
            self.__correct_words.get().append(current_word)
            self.__words.remove(current_word)
            self.__selected_cells.get().clear()
            self.__correct_words.notify_changed()
            current_word = ''
            words = self.__words
            
        self.__all_optional_words = [w
                                     for w in words
                                     if w.startswith(current_word)]
        items = min(5, len(self.__all_optional_words))
        self.__optional_words.set(sample(self.__all_optional_words, items))

        # update view
        self.__update_cells()

        self.__current_word.set(current_word)
        self.__selected_cells.notify_changed()

    # region properties
    @property
    def name(self):
        return self.__name

    @property
    def cells(self):
        return self.__cells

    @property
    def selected_cells(self):
        return self.__selected_cells

    @property
    def current_word(self):
        return self.__current_word

    @property
    def words(self):
        return self.__words

    @property
    def optional_words(self):
        return self.__optional_words

    @property
    def correct_words(self):
        return self.__correct_words

    @property
    def score(self):
        return self.__score

    @property
    def seconds(self):
        return self.__seconds

    @property
    def game_over(self):
        return self.__game_over
    # endregion

    @staticmethod
    def __all_words():
        with open('boggle_dict.txt') as f:
            return f.read().splitlines()
