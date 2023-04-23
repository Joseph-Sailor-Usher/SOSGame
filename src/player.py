from abc import ABC, abstractmethod
from cell import Cell
from tuple import Tuple

class Player( ABC ):
    def __init__(self, player_type, moveType):
        self.player_type = player_type
        self.score = 0
        self.moveType = moveType

    def get_move_type(self):
        return self.moveType

    def set_move(self, newMoveType):
        self.moveType = newMoveType

    def getScore(self):
        return self.score

    def setScore(self, newScore):
        self.score = newScore

    @abstractmethod
    def getNextMove(self, grid) -> Tuple(int, int, str):
        #return x, y, and moveType, to be used in the game class
        pass
