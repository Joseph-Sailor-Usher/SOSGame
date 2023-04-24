import random
from player import Player
from cell import Cell

'''
    Player class
    1. stores player information
'''

class PlayerAI(Player):
    def __init__(self, player_type, letter):
        self.sos_game_ui = None
        self.type = player_type
        self.letter = letter
        self.score = 0
    
    def __str__(self) -> str:
        return "AI"
    
    def get_cell_type(self):
        return self.letter

    #called by game when a turn ended and this player became the current player
    def make_next_move(self, game):
        print("AI turn")
        if(game.game_over or game.board.is_full()):
            return
        #don't let humans interfere
        game.accepting_input = False
        #make your move
        #find the move with the highest SOS's
        #if there are multiple moves with the same number of SOS's, choose one at random
        moves = []
        for i in range(game.board.board_size):
            for j in range(game.board.board_size):
                #get value of cell ->> def get_value(self, row, col): return self.board[row][col]
                if game.board.get_value(i, j) == Cell.EMPTY:
                    #count_potential_soss(self, row, col, move_type):
                    moves.append((game.board.count_soss(i, j, Cell.S), i, j, Cell.S))
                    moves.append((game.board.count_soss(i, j, Cell.O), i, j, Cell.O))
        #sort the list of possible move by what move has the most SOS's
        moves.sort(key=lambda x: x[0], reverse=True)
        #print(moves)
        good_moves = []
        #i accesses lists, and j accesses the elements in the list
        if(moves.__len__() == 0):
            good_moves.append(moves[0])
        if(len(moves) > 1):    
            for i in range(len(moves)):
                #print(moves[i][j])
                #if the new move is better or equal to the current best move
                if(moves[i][0] >= moves[0][0]):
                    good_moves.append(moves[i])
        #print(moves)
        #make the best move
        random_index = random.randint(0, len(good_moves) - 1)
        #print(str(good_moves[random_index][1]) + " " +  str(good_moves[random_index][2]))
        self.sos_game_ui.game.players[self.sos_game_ui.game.current_player_index].letter = good_moves[random_index][3]
        #def change_button_text(self, row, col, text): 
        self.sos_game_ui.rename_board_buttons(good_moves[random_index][1], good_moves[random_index][2], good_moves[random_index][3])
        print("AI made a move " + str(good_moves[random_index][1]) + str(good_moves[random_index][2]) + " " + str(good_moves[random_index][3]))
        game.gametype.make_move(game, good_moves[random_index][1], good_moves[random_index][2], good_moves[random_index][3])
