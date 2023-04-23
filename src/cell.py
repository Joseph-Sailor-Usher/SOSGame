from enum import Enum

'''
    Enum for the cell states.
        EMPTY: no move has been made
        CROSS: a cross has been placed
        CIRCLE: a circle has been placed
'''
class Cell(Enum):
    EMPTY = 0
    S = 1
    O = 2

    def __str__(self):
        if self == Cell.EMPTY:
            return "."
        elif self == Cell.S:
            return "S"
        elif self == Cell.O:
            return "O"
