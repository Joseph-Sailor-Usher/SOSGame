from player import Player

'''
    Player class
    1. stores player information
'''
class PlayerAI(Player):
    def __init__(self, player_type, letter):
        self.type = player_type
        self.letter = letter
        self.score = 0
    
    def __str__(self) -> str:
        return f"Player {self.type} ({self.letter.__str__()})"
    
    def get_cell_type(self):
        return self.letter

    #called by game when a turn ended and this player became the current player
    def make_next_move(self, game):
        #don't let humans interfere
        game.accepting_input = False
        #make your move
        
