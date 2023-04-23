from board import Board
from player import Player
from cell import Cell

'''
    Game class
    1. Stores game information
    1.1 board: Board object
    1.2 players: list of Player objects
    1.3 current_player: Player object

    2. Manages game phases
    2.1 __str__ returns the name of the game type
    2.2 Start a new game (clears the board, sets current player to player 1)
    2.3 Switch the turn (switches current player)
    2.4 Make move (checks if move is valid, makes move, switches turn)
    2.5 Check win (checks if the game has been won)

    2.1, 2.4 and 2.5 are defined in child classes
'''

class Gametype:
    def __str__(self) -> str:
        return "Undefined"

    def make_move(self, row, col):
        pass
   
    def check_win(self):
        pass
