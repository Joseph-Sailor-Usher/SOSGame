from cell import Cell
from player import Player
from game import Game
from gametype_simple import GametypeSimple
from sos_game_ui import SOSGameUI
from player_human import PlayerHuman

'''
    Main function
'''

def main():
    #Instantiate the game
    game = Game(8, GametypeSimple(), PlayerHuman("Human", Cell.S), PlayerHuman("Human", Cell.O))

    #Instantiate the game UI and pass it a reference to the game
    app = SOSGameUI(game)
    app.mainloop()

if __name__ == "__main__":
    main()
