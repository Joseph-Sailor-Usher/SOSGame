from player import Player

'''
    Player class
    1. stores player information
'''
class PlayerHuman(Player):
    def __init__(self, player_type, letter):
        self.sos_game_ui = None
        self.type = player_type
        self.letter = letter
        self.score = 0
    
    def __str__(self) -> str:
        return "Human"
    
    def get_cell_type(self):
        return self.letter
    
    #called by game when a turn ended and this player became the current player
    def make_next_move(self, game):
        print("Human turn")
        game.accepting_input = True
