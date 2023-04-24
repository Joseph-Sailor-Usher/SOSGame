from cell import Cell
from board import Board
from gametype_general import GametypeGeneral
from gametype_simple import GametypeSimple
from player_human import PlayerHuman
from player_ai import PlayerAI


class Game:
    def __init__(self, board_size, gametype, player1, player2):
        #assigned members
        self.board = Board(board_size)
        self.gametype = gametype
        self.players = [
            player1,
            player2
        ]
        #default members
        self.winner = self.players[0]
        self.game_over = True
        self.current_player_index = 0
        self.accepting_input = False
   
    #start a new game
    def start_game(self):
        self.board.clear_board()
        self.players[0].score = 0
        self.players[1].score = 0
        self.current_player_index = 0
        self.game_over = False
        print("New game started.")

    #end the game
    def end_game(self):
        print("Game ended.")
        self.game_over = True

    #called by the players when they make a move
    def enter_a_move_to_the_gametype(self, game, row, col):
        if(self.accepting_input == False):
            return False
        return game.gametype.make_move(game, row, col)
    
    def check_win(self, row, col):
        self.gametype.check_win(self.board, row, col)

    def check_board_full(self):
        return self.board.check_board_full()

    #change the current gametype
    def change_gametype(self, game, game_type_string):
        if game_type_string == "Simple" or game_type_string == "simple":
            game.gametype = GametypeSimple()
            print("Game type changed to Simple.")
        elif game_type_string == "General" or game_type_string == "general":
            game.gametype = GametypeGeneral()
            print("Game type changed to General.")
        else:
            print("Invalid game type.")

    #change the player type of a player
    def change_player_type(self, player_index, player_type_string):
        if player_type_string == "Human" or player_type_string == "human":
            self.players[player_index] = PlayerHuman("Human", Cell.S)
            print("Player types changed to Human.")
        elif player_type_string == "AI" or player_type_string == "ai":
            self.players[player_index] = PlayerAI("AI", Cell.S)
            print("Player types changed to AI.")
        else:
            print("Invalid player type.")

    #change the current player move type
    def change_player_move_type(self, player_index, move_type):
        self.players[player_index].letter = move_type
    
    #called by the current gametype when this is necessary
    def switch_turn(self):
        if self.current_player_index == 0:
            self.current_player_index = 1
        else:
            self.current_player_index = 0
