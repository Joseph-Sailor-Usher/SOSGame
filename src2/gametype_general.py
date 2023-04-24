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

    def make_move(self, game, row, col, move_type):
        result = False
        if game.board.make_move(row, col, move_type):
            game.players[game.current_player_index].score += game.board.count_soss(row, col, move_type)
            if(game.board.count_soss(row, col, move_type) == 0):
                game.switch_turn()   
                game.players[game.current_player_index].make_next_move(game)
            elif(game.board.count_soss(row, col, move_type) > 0 and game.game_over == False):
                game.players[game.current_player_index].make_next_move(game)
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
            result = True
        else:
            print("Invalid move. Try again.")
            result = False
        if(self.check_win(game)):
            game.players[game.current_player_index].sos_game_ui.create_post_game_widgets()


    def check_win(self, game):
        return game.board.is_full()
