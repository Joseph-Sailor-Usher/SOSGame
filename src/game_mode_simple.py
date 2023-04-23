from game_mode import GameMode
from game_win_state import GameWinState

class GameModeSimple( GameMode ):
    def makeMode(self, game):
        pass

    def checkWin(self, game):
        #If no moves left, and no one scored, it's a tie
        if(game.checkBoardFull()
           and game.players[0].getScore() == 0
           and game.players[1].getScore() == 0):
            return GameWinState.tie
        #If someone scored, they win
        if(game.players[0].getSCore() != 0):
            return GameWinState.red_player
        if(game.players[1].getScore() != 0):
            return GameWinState.blue_player
        #Otherwise, no one has won yet
        return GameWinState.none        