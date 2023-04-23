from abc import ABC, abstractmethod

class GameMode( ABC ):
    @abstractmethod
    def make_move(self, game):
        pass
    @abstractmethod
    def check_win(self, game):
        pass
