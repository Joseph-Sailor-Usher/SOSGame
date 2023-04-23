from board import Board
from gametype_general import GametypeGeneral
from gametype_simple import GametypeSimple

class Game:
    def __init__(self, board_size, gametype, player1, player2):
        self.board = Board(board_size)
        self.gametype = gametype
        self.players = [
            player1,
            player2
        ]
        self.winner = self.players[0]
        self.game_over = True
        self.current_player = self.players[0]

    def change_gametype(self, game, game_type_string):
        if game_type_string == "Simple":
            game.gametype = GametypeSimple()
            print("Game type changed to Simple.")
        elif game_type_string == "General":
            game.gametype = GametypeGeneral()
            print("Game type changed to General.")
        else:
            print("Invalid game type.")

    def start_game(self):
        self.board.clear_board()
        self.players[0].score = 0
        self.players[1].score = 0
        self.current_player = self.players[0]
        self.game_over = False
        print("New game started.")
    
    def get_current_player(self):
        return self.current_player

    def switch_turn(self):
        if self.current_player == self.players[0]:
            self.current_player = self.players[1]
        else:
            self.current_player = self.players[0]
        #print("It is now player " + self.current_player.letter.__str__() + "'s turn.")
   
    def end_game(self):
        print("Game ended.")
        self.game_over = True

    def make_move(self, game, row, col):
        return game.gametype.make_move(game, row, col)
    
    def check_win(self, row, col):
        self.gametype.check_win(self.board, row, col)
