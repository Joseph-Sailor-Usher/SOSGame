import sys
import os
import unittest
from tkinter import Tk
from unittest.mock import patch
from board import Board
from game import Game
from gametype_general import GametypeGeneral
from gametype_simple import GametypeSimple
from cell import Cell
from player import Player
from sos_game_ui import SOSGameUI

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
class TestGame(unittest.TestCase):
    def test_resize_board_when_game_not_in_progress(self):
        root = Tk()
        game = Game(3, GametypeSimple(), Player("Human", Cell.S), Player("Human", Cell.O))
        game.board = Board(5) # current board size is 5x5
        game.game_over = True

        with patch('builtins.input', return_value='7'):
            game.board.update_board_size(7) # resizing to 7x7

        self.assertEqual(game.board.board_size, 7)
        self.assertEqual(len(game.board.board), 7)
        self.assertEqual(len(game.board.board[0]), 7)

    def test_resize_board_when_game_in_progress_and_make_move_to_change_turn(self):
        root = Tk()
        game = Game(3, GametypeSimple(), Player("Human", Cell.S), Player("Human", Cell.O))
        game.board = Board(5) # current board size is 5x5
        game.start_game()
        
        #check if we really changed players.
        game.make_move(0, 0)
        self.assertEqual(game.players[1], game.get_current_player())

        with patch('builtins.input', return_value='7'):
            game.board.update_board_size(7) # resizing to 7x7

        self.assertEqual(game.board.board_size, 7)
        self.assertEqual(len(game.board.board), 7)
        self.assertEqual(len(game.board.board[0]), 7)

    def test_board_size_unmodifiable_during_game(self):
        # Start a game with a specified board size
        game = Game(8, GametypeSimple(), Player("Human", Cell.S), Player("Human", Cell.O))
        app = SOSGameUI(game)
        app.mainloop()

        # Confirm that the game is in progress
        self.assertEqual(game.game_over(), False)

        # Attempt to modify the board size through the user interface
        # (in this case, by clicking on a resize button that should be disabled)
        resize_button = app.resize_button
        self.assertEqual(resize_button['state'], 'disabled')

        # End the game
        app.destroy()

    def test_switch_turn(self):
        game = Game(3, GametypeSimple(), Player("Human", Cell.S), Player("Human", Cell.O))
        current_player = game.get_current_player()
        game.switch_turn()
        next_player = game.get_current_player()

        self.assertNotEqual(current_player, next_player)
        game.switch_turn()
        self.assertEqual(current_player, game.get_current_player())

    #User story four
    def play_simple_game(board):
        """
        Plays a simple game of SOS on the given board.
        """
        players = [Player("Human", Cell.S), Player("Human", Cell.O)]
        current_player = players[0]
        while True:
            print(f"\nIt's {current_player}'s turn")
            print(board)
            row = int(input("Enter row number: "))
            col = int(input("Enter column number: "))
            if board.place_move(row, col, current_player):
                if board.check_for_sos(row, col, current_player):
                    print(f"\n{current_player} completed an SOS!")
                    print(board)
                    return current_player
                else:
                    current_player = players[(players.index(current_player) + 1) % 2]
            else:
                print("Invalid move! Try again.")

    #Game(8, GametypeSimple(), Player("Human", Cell.S), Player("Human", Cell.O))
    #User Story two
    def test_set_gametype(self):
        game = Game(3, GametypeSimple(), Player("Human", Cell.S), Player("Human", Cell.O))
        assert isinstance(game.gametype, GametypeSimple)
        game.change_gametype(game, "General")
        assert isinstance(game.gametype, GametypeGeneral)
        game.change_gametype(game, "invalid")
        assert isinstance(game.gametype, GametypeGeneral)

        #User story three
    def test_start_new_game(self):
        game = Game(8, GametypeSimple(), Player("Human", Cell.S), Player("Human", Cell.O))
        self.assertEqual(game.board.board_size, 8)
        assert isinstance(game.gametype, GametypeSimple)
        game.change_gametype(game, "General")
        game.start_game()
        assert isinstance(game.gametype, GametypeGeneral)

    def test_start_new_game_and_make_a_move(self):
        game = Game(8, GametypeSimple(), Player("Human", Cell.S), Player("Human", Cell.O))
        self.assertEqual(game.board.board_size, 8)
        assert isinstance(game.gametype, GametypeSimple)
        game.change_gametype(game, "General")
        game.start_game()
        assert isinstance(game.gametype, GametypeGeneral)
        game.board.make_move(0, 0, game.get_current_player())
        assert isinstance(game.board[0][0].get_cell(), Cell.S)

    def test_start_new_game_and_fill_the_board_and_check_for_game_over(self):
        game = Game(8, GametypeSimple(), Player("Human", Cell.S), Player("Human", Cell.O))
        self.assertEqual(game.board.board_size, 8)
        assert isinstance(game.gametype, GametypeSimple)
        for i in range(8):
            for j in range(8):
                game.board.make_move(i, j, game.get_current_player())
        self.assertEqual(game.game_over(), True)

    def test_winner(self):
        game = Game(8, GametypeSimple(), Player("Human", Cell.S), Player("Human", Cell.O))
        self.assertEqual(game.board.board_size, 8)
        assert isinstance(game.gametype, GametypeSimple)
        game.make_move(0, 0)
        game.make_move(1, 1)
        game.make_move(1, 2)
        self.assertEqual(game.game_over(), True)
        self.assertEqual(game.get_winner(), "O")
    
    def test_tie(self):
        game = Game(3, GametypeSimple(), Player("Human", Cell.S), Player("Human", Cell.O))
        self.assertEqual(game.board.board_size, 3)
        assert isinstance(game.gametype, GametypeSimple)
        game.make_move(0, 0)
        game.make_move(2, 0)
        game.make_move(0, 1)
        game.make_move(2, 1)
        game.make_move(0, 2)
        game.make_move(2, 2)
        game.make_move(1, 0)
        game.make_move(1, 2)
        game.make_move(1, 1)
        self.assertEqual(game.game_over(), True)
        self.assertEqual(game.get_winner(), "Tie")

    def test_general_game_play_again_feature(self):
        game = Game(3, GametypeSimple(), Player("Human", Cell.S), Player("Human", Cell.O))
        game.make_move(0, 0)
        game.make_move(1, 1)
        game.make_move(2, 2)
        game.make_move(3, 3)
        assert isinstance(game.board[3][3], Cell.S)
    
    #test case 8.1
    def test_human_opponent_for_read_player(self):
        game = Game(3, GametypeSimple(), Player("Human", Cell.S), Player("Human", Cell.O))
        game.change_player_type(game, "red", "Human")
        self.assertEqual(game.red_player.player_type, "Human")
    
    #test case 8.2
    def test_ai_opponent_for_red_player(self):
        game = Game(3, GametypeSimple(), Player("Human", Cell.S), Player("Human", Cell.O))
        game.change_player_type(game, "red", "AI")
        self.assertEqual(game.red_player.player_type, "AI")
    
    #test case 8.3
    def test_human_opponent_for_blue_player(self):
        game = Game(3, GametypeSimple(), Player("Human", Cell.S), Player("Human", Cell.O))
        game.change_player_type(game, "blue", "Human")
        self.assertEqual(game.blue_player.player_type, "Human")
    
    #test case 8.4
    def test_ai_opponent_for_blue_player(self):
        game = Game(3, GametypeSimple(), Player("Human", Cell.S), Player("Human", Cell.O))
        game.change_player_type(game, "blue", "AI")
        self.assertEqual(game.blue_player.player_type, "AI")
    
    #test case 8.6
    def test_invalid_opponent_for_red_player(self):
        game = Game(3, GametypeSimple(), Player("Human", Cell.S), Player("Human", Cell.O))
        game.change_player_type(game, "red", "Invalid")
        self.assertEqual(game.red_player.player_type, "Human")

    #test case 8.5
    def test_invalid_opponent_for_blue_player(self):
        game = Game(3, GametypeSimple(), Player("Human", Cell.S), Player("Human", Cell.O))
        game.change_player_type(game, "blue", "Invalid")
        self.assertEqual(game.blue_player.player_type, "Human")

    #test case 9.1
    def test_human_player_makes_a_move_in_a_simple_game(self):
        game = Game(3, GametypeSimple(), Player("Human", Cell.S), Player("Human", Cell.O))
        game.make_move(0, 0)
        assert isinstance(game.board[0][0], Cell.S)
    
    #test case 9.2
    def test_ai_player_makes_a_move_in_a_simple_game(self):
        game = Game(3, GametypeSimple(), Player("AI", Cell.S), Player("Human", Cell.O))
        game.make_move(0, 0)
        assert isinstance(game.board[0][0], Cell.S)
    
    #test case 10.1
    def test_human_player_makes_a_move_in_a_general_game(self):
        game = Game(3, GametypeGeneral(), Player("Human", Cell.S), Player("Human", Cell.O))
        game.make_move(0, 0)
        assert isinstance(game.board[0][0], Cell.S)
    
    #test case 10.2
    def test_ai_player_makes_a_move_in_a_general_game(self):
        game = Game(3, GametypeGeneral(), Player("AI", Cell.S), Player("Human", Cell.O))
        game.make_move(0, 0)
        assert isinstance(game.board[0][0], Cell.S)

    if __name__ == '__main__':
        unittest.main()
        
    '''
    AC 8.1 <Choose a human opponent for the red player>
    Given the main menu is displayed and a game is not started  is started
    When a player clicks the human button in the red player’s player type select widget
    Then change the red player to be a human
    AC 8.2 <Choose an ai opponent for the redplayer>
    Given the main menu is displayed and a game is not started 
    When a player clicks the ai button in the red player’s player type select widget
    Then change the red player to be an ai
    AC 8.3 <Choose a human opponent for the blue player>
    Given the main menu is displayed and a game is not started 
    When a player clicks the human button in the blue player’s player type select widget
    Then change the blue player to be a human
    AC 8.4 <Choose an ai opponent for the blue player>
    Given the main menu is displayed and a game is not started 
    When a player clicks the ai button in the blue player’s player type select widget
    Then change the blue player to be an ai
    AC 9.1 <A human makes a move in a simple game>
    Given a simple game is underway
    When it becomes a human player’s turn
    Then change the input_allowed member variable on the game object and call the make move function on the player which will enable the buttons to be pressed by the player to let them make their move
    AC 9.2 <An ai makes a move in a simple game>
    Given a simple game is underway
    When it becomes an ai player’s turn
    Then call the make move function on the ai player which will return a tuple of (x, y, move_type) which we can use to make a move.
    AC 10.1 <A human makes a move in a general game>
    Given a general game is underway
    When it becomes a human player’s turn
    Then change the input_allowed member variable on the game object and call the make move function on the player which will enable the buttons to be pressed by the player to let them make their move, and if they get an sos allow them to make another move until they do not make an sos
    AC 10.2 <A human makes a move in a general game>
    Given a general game is underway
    When it becomes a human player’s turn
    Then change the input_allowed member variable on the game object and call the make move function on the player which will enable the buttons to be pressed by the player to let them make their move, and if they get an sos allow them to make another move until they do not make an sos

'''