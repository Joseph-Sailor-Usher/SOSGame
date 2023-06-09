from cell import Cell
from player import Player
from game import Game
from gametype_simple import GametypeSimple
from sos_game_ui import SOSGameUI
from player_human import PlayerHuman

'''
    Main function
    1. Instantiate a Game with a GametypeSImple and two PlayerHumans
    2. Instantiate a SOSGameUI with a reference to the game
'''

def main():
    #Instantiate the game
    game = Game(8, GametypeSimple(), PlayerHuman(Cell.S), PlayerHuman(Cell.S))
    #Instantiate the game UI and pass it a reference to the game
    app = SOSGameUI(game)
    app.mainloop()

if __name__ == "__main__":
    main()
