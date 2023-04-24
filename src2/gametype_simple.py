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

    def make_move(self, game, row, col, move_type):
        print("make move")
        tempVar = True
        if game.board.make_move(row, col, move_type):
            if self.check_win(game, row, col):
                print("Player" + str(game.players[game.current_player_index]) + " wins!")
                game.players[game.current_player_index].score += 1
                game.winner = game.players[game.current_player_index]
                game.end_game()
                game.players[game.current_player_index].sos_game_ui.create_post_game_widgets()
                tempVar = True
            else:
                game.switch_turn()
                game.players[game.current_player_index].make_next_move(game)
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
        if(game.board.count_soss(row, col, Cell.S) > 0 or game.board.count_soss(row, col, Cell.O) > 0):
            return True
        return False
