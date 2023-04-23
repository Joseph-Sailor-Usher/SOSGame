from abc import ABC, abstractmethod
from cell import Cell

class PlayerAI( ABC ):
    def __init__(self, player_type, score, moveType):
        self.player_type = player_type
        self.score = score
        self.moveType = moveType

    @abstractmethod
    def get_move_type(self, board):
        return self.moveType

    @abstractmethod
    def set_move(self, newMoveType):
        self.moveType = newMoveType

    @abstractmethod
    def getScore(self):
        return self.score

    @abstractmethod
    def setScore(self, newScore):
        self.score = newScore

    @abstractmethod
    def getNextMove(self, grid):
        #return x, y, and moveType, to be used in the game class
        pass
