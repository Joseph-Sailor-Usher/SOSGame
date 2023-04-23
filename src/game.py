from cell import Cell
from player_human import PlayerHuman
from player_ai import PlayerAI
from game_mode_simple import GameModeSimple
from game_mode_general import GameModeGeneral
from SOSGameUI import SOSGameUI

class Game:
    def __init__(self, board_size):
        self.board_size = board_size
        self.board = [[Cell.Empty for i in range(board_size)] for j in range(board_size)]
        self.game_mode = GameModeSimple()
        self.players = [
            PlayerHuman(),
            PlayerHuman()
        ]
        self.current_player = self.players[0]

    def main():
        game = Game(3, 'simple', "human", "human")
        app = SOSGameUI(game)
        app.mainloop()

    def switch_turn(self):
        if self.current_player == self.players[0]:
            self.current_player = self.players[1]
        else:
            self.current_player = self.players[0]

    def get_current_player(self):
        return self.current_player
    
    def set_game_mode(self, game_mode):
        if(game_mode == "simple"):
            self.game_mode = GameModeSimple()
        elif(game_mode == "general"):
            self.game_mode = GameModeGeneral()
        else:
            print("Invalid game mode. Please choose 'simple' or 'general'.")

    def start_new_game(self):
        pass

    def make_move(self, row, col):
        current_player = self.get_current_player()
        if self.board.is_valid_move(row, col):
            self.board.place_move(row, col, current_player.letter)
            self.switch_turn()
            return True
        return False
    
    def checkBoardFull(self):
        pass

    def checkSOS(self, x, y, moveType):
        pass

    if __name__ == "__main__":
        main()


"""
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

"""