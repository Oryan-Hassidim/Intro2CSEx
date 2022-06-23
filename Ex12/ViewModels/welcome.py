from MVVM.notified_property import NotifiedProperty


class WelcomeViewModel:
    "ViewMOdel for the welcome page"
    def __init__(self):
        "initializes new WelcomeViewModel"
        self.__name = NotifiedProperty("")
    
    def start(self):
        "starts the game. returns new GameViewModel"
        from ViewModels.game import GameViewModel
        return GameViewModel(self.__name.get())

    def high_scores(self):
        "navigates to view the high scores. returns new HighScoresViewModel"
        from ViewModels.high_scores import HighScoresViewModel
        return HighScoresViewModel(False)
    
    @property
    def name(self):
        return self.__name
