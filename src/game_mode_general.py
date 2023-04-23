from game_mode import GameMode
from game_win_state import GameWinState

class GameModeSimple( GameMode ):
    def makeMode(self, game):
        pass
    
    def checkWin(self, game):
        #If the board is full
        if(game.checkBoardFull()):
            #If the red player has more points, they win
            if(game.players[0].getSCore() > game.players[1].getScore()):
                return GameWinState.red_player
            #If they have the same amount of points, it's a tie
            elif(game.players[0].getSCore() == game.players[1].getScore()):
                return GameWinState.tie
            #Otherwise, the blue player has more points, so they win
            else:
                return GameWinState.blue_player
        #Otherwise, no one has won yet
        return GameWinState.none