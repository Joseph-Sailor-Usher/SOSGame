from board import Board
from player import Player
from cell import Cell
from gametype import Gametype

'''
    Game Simple class
    1. Overrides functions from game class
    1.1 make_move: checks if move is valid, makes move, switches turn
    1.2 check_win: checks if the game has been won
'''

class GametypeSimple(Gametype):
    def __init__(self):
        super().__init__()
    
    def __str__(self) -> str:
        return "Simple"

    def make_move(self, game, row, col):
        tempVar = True
        if game.board.make_move(row, col, game.current_player.get_cell_type()):
            if self.check_win(game, row, col):
                print("Player" + str(game.current_player) + " wins!")
                game.current_player.score += 1
                game.winner = game.current_player
                game.end_game()
                tempVar = True
            else:
                game.switch_turn()
                tempVar = True
        else:
            print("Invalid move. Try again.")
            tempVar = False
        if(game.board.is_full()):
            print("Board is full. Tied game.")
            game.winner = None
            game.end_game()
        return tempVar

    def check_win(self, game, row, col):
        return game.board.count_new_soss(row, col) > 0
