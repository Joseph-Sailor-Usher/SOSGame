from game import Game
from sos_game_ui import SOSGameUI
from player_human import PlayerHuman
from player_ai import PlayerAI
from game_mode_simple import GameModeSimple
from game_mode_general import GameModeGeneral

'''
    Main function
    1. Instantiate the game with an 8x8 board, simple gamemode, and two human players
    2. Instantiate the SOSGameUI and pass it a reference to the game
        2.1 The game UI will then instantiate the menu UI
            2.1.1 Players can change the board size
            2.2.1 Players can change player type from human to ai
            2.2.3 Players can then select the game mode
            2.2.4 Players can start the game
        2.3 The game UI will then instantiate the game board UI
            2.3.1 Players can make moves
'''

def main():
    #Instantiate the game
    game = Game(8, GameModeSimple(), PlayerHuman(), PlayerHuman())

    #Instantiate the game UI and pass it a reference to the game
    app = SOSGameUI(game)
    app.mainloop()

if __name__ == "__main__":
    main()
