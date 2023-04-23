from abc import ABC, abstractmethod
from cell import Cell

class PlayerHuman( ABC ):
    def __init__(self, player_type, score, moveType):
        self.player_type = player_type
        self.score = score
        self.moveType = moveType

    def get_move_type(self, board):
        return self.moveType

    def set_move(self, newMoveType):
        self.moveType = newMoveType

    def getScore(self):
        return self.score

    def setScore(self, newScore):
        self.score = newScore

    @abstractmethod
    def getNextMove(self, grid):
        #return x, y, and moveType, to be used in the game class
        pass
