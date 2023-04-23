from abc import ABC, abstractmethod
from cell import Cell

class Player( ABC ):
    def __init__(self):
        self.score = 0
        self.moveType = Cell.Empty

    def get_move_type(self):
        return self.moveType

    def set_move(self, newMoveType):
        self.moveType = newMoveType

    def getScore(self):
        return self.score

    def setScore(self, newScore):
        self.score = newScore

    @abstractmethod
    def getNextMove(self, grid) -> tuple[int, int, str]:
        x = 0
        y = 0
        Cell = Cell.EMPTY
        return x, y, Cell
