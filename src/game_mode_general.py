from game_mode import GameMode
from game_win_state import GameWinState

class GameModeSimple( GameMode ):
    def make_move(self, game, row, col):
        if game.board.make_move(row, col, game.current_player.get_cell_type()):
            game.current_player.score += game.board.count_new_soss(row, col)
            if(game.board.count_new_soss(row, col) == 0):
                game.switch_turn()   
            self.check_win(game)
            if(game.players[0].score > game.players[1].score):
                game.winner = game.players[0]
            elif(game.players[0].score < game.players[1].score):
                game.winner = game.players[1]
            elif(game.players[0].score == game.players[1].score):
                game.winner = None
            print("Player 1 " + str(game.players[0].score))
            print("Player 2 " + str(game.players[1].score))
            print(game.winner.__str__())
            return True
        else:
            print("Invalid move. Try again.")
            return False
    
    def check_win(self, game):
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