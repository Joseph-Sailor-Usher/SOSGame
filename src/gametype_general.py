from board import Board
from player import Player
from cell import Cell
from gametype import Gametype

'''
    Game class
    1. Stores game information
    1.1 board: Board object
    1.2 players: list of Player objects
    1.3 current_player: Player object

    2. Manages game phases
    2.1 Start a new game (clears the board, sets current player to player 1)
    2.2 Switch the turn (switches current player)
    2.3 Make move (checks if move is valid, makes move, switches turn)
    2.4 Check win (checks if the game has been won)

    2.3 and 2.4 are to be overwritten by child classes
'''

class GametypeGeneral(Gametype):
    def __init__(self):
        super().__init__()
    
    def __str__(self) -> str:
        return "General"

    def make_move(self, game, row, col):
        if game.board.make_move(row, col, game.current_player.get_cell_type()):
            game.current_player.score += game.board.count_new_soss(row, col)
            if(game.board.count_new_soss(row, col) == 0):
                game.switch_turn()   
            self.check_win(game)
            if(game.players[0].score > game.players[1].score):
                game.winner = game.players[0]
            elif(game.players[0].score < game.players[1].score):
                game.winner = game.players[1]
            elif(game.players[0].score == game.players[1].score):
                game.winner = None
            print("Player 1 " + str(game.players[0].score))
            print("Player 2 " + str(game.players[1].score))
            print(game.winner.__str__())
            return True
        else:
            print("Invalid move. Try again.")
            return False

    def check_win(self, game):
        if game.board.is_full():
            game.end_game()
