from player import Player

'''
    Player class
    1. stores player information
'''
class PlayerHuman(Player):
    def __init__(self, letter):
        self.sos_game_ui = None
        self.letter = letter
        self.score = 0
    
    def __str__(self) -> str:
        return "Human"
    
    def get_cell_type(self):
        return self.letter
    
    #called by game when a turn ended and this player became the current player
    def make_next_move(self, game):
        game.accepting_input = True
