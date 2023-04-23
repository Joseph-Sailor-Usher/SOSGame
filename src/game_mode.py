from abc import ABC, abstractmethod

class GameMode( ABC ):
    @abstractmethod
    def makeMode(self, game):
        pass
    @abstractmethod
    def checkWin(self, game):
        pass
