from abc import ABC, abstractmethod
from cell import Cell
from player import Player

class PlayerAI( Player ):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def getNextMove(self, grid):
        #return x, y, and moveType, to be used in the game class
        pass
