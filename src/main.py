from game import Game
from gametype_simple import GametypeSimple
from player import Player

class main:
    def __init__(self):
        self.game = Game(8, GametypeSimple(), Player("Human", Cell.S), Player("Human", Cell.O))
        self.app = SOSGameUI(self.game)
        self.app.mainloop()
    