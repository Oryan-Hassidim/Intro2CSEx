from MVVM.notified_property import NotifiedProperty
from Model.high_scores import *
from datetime import datetime


class EndGameViewModel:
    """
    viewmodel for Endgame page
    """
    def __init__(self, name, score, words):
        self.__name = NotifiedProperty(name)
        self.__score = NotifiedProperty(score)
        self.__words = NotifiedProperty(words)
        self.__all_time_rank = NotifiedProperty(None)
        self.__new_high_score = NotifiedProperty(self.__new_high_score())

    def play_again(self):
        """returns the game page for the same player"""
        from ViewModels.game import GameViewModel
        return GameViewModel(self.__name.get())
    
    def high_scores(self):
        """returns the High Scores page"""
        from ViewModels.high_scores import HighScoresViewModel
        return HighScoresViewModel()

    def __new_high_score(self):
        """determines whether player reached a new high score"""
        cur_score = self.__score.get()
        high_scores = get_high_score()
        _place = len(high_scores) + 1
        for place, score in enumerate(high_scores):
            if cur_score >= score[2]:
                _place = place
                break
        if _place < 10:
            self.__all_time_rank.set(_place + 1)
            high_scores.insert(_place, (
                self.__name.get(),
                datetime.now(),
                cur_score))
            while len(high_scores) > 10:
                high_scores.pop()
            save_high_score(high_scores)
            return True
        return False

    @property
    def score(self):
        return self.__score

    @property
    def name(self):
        return self.__name

    @property
    def words(self):
        return self.__words

    @property
    def new_high_score(self):
        return self.__new_high_score

    @property
    def all_time_rank(self):
        return self.__all_time_rank
