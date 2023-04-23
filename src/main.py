import tkinter as tk
from game import Game
from SOSGameUI import SOSGameUI

def main():
    game = Game(3, 'simple', "human", "human")
    app = SOSGameUI(game)
    app.mainloop()

if __name__ == "__main__":
    main()
