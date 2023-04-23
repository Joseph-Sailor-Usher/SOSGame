from game_mode import GameMode
from game_win_state import GameWinState

class GameModeSimple( GameMode ):
    def make_move(self, game, row, col):
        tempVar = True
        if game.board.make_move(row, col, game.current_player.get_cell_type()):
            if self.check_win(game, row, col):
                print("Player" + str(game.current_player) + " wins!")
                game.current_player.score += 1
                game.winner = game.current_player
                game.end_game()
                tempVar = True
            else:
                game.switch_turn()
                tempVar = True
        else:
            print("Invalid move. Try again.")
            tempVar = False
        if(game.board.is_full()):
            print("Board is full. Tied game.")
            game.winner = None
            game.end_game()
        return tempVar

    def check_win(self, game):
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