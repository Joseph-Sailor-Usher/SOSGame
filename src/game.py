from board import Board
from player import Player

class Game:
    def __init__(self, board_size, game_type, player1_type, player2_type):
        self.board = Board(board_size)
        self.game_type = game_type
        self.players = [
            Player(1, player1_type, 'S'),
            Player(2, player2_type, 'O')
        ]
        self.current_player = self.players[0]

    def switch_turn(self):
        if self.current_player == self.players[0]:
            self.current_player = self.players[1]
        else:
            self.current_player = self.players[0]

    def get_current_player(self):
        return self.current_player
    
    def set_game_type(self, game_type):
        if game_type == "simple" or game_type == "general":
            self.game_type = game_type
            print(f"Game type changed to {self.game_type}.")
        else:
            print("Invalid game type. Please choose 'simple' or 'general'.")

    def start_new_game(self):
        pass

    def is_finished(self):
        pass

    def make_move(self, row, col):
        current_player = self.get_current_player()
        if self.board.is_valid_move(row, col):
            self.board.place_move(row, col, current_player.letter)
            self.switch_turn()
            return True
        return False