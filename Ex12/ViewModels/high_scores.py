from MVVM.notified_property import NotifiedProperty
import datetime
from Model.high_scores import *


class HighScoresViewModel:
    "ViewModel for high scores page"
    def __init__(self, again=False):
        """
        initializes new HighScoresViewModel.
        Takes an optional parameter of the return button if it again or home.
        """
        high_score = get_high_score()
        self.__high_scores = NotifiedProperty(high_score)
        self.__again = NotifiedProperty(again)

    @property
    def high_scores(self):
        return self.__high_scores
    
    @property
    def again(self):
        return self.__again

    def play_again(self):
        "returns welcome viewmodel."
        from ViewModels.welcome import WelcomeViewModel
        return WelcomeViewModel()
        
        
