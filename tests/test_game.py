import unittest
from src.game import Game

class TestGame(unittest.TestCase):
    def test_switch_turn(self):
        game = Game(3, 'simple', 'human', 'ai')
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
        players = ['S', 'O']
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

    #User Story two
    def test_set_game_type(self):
        game = Game(3, "simple", "human", "human")
        self.assertEqual(game.game_type, 'simple')
        game_type = game.game_type
        game.set_game_type('general')
        self.assertEqual(game.game_type, 'general')
        game.set_game_type('invalid')
        self.assertEqual(game.game_type, 'general')

        #User story three
    def test_start_new_game(self):
        game = Game(3, "simple", "human", "human")
        self.assertEqual(game.board.size, 3)
        self.assertEqual(game.game_type, "simple")
        self.assertEqual(game.current_player.letter, 'S')
        self.assertEqual(game.players[0].player_id, 1)
        self.assertEqual(game.players[1].player_id, 2)

        game.start_new_game(4, "general")

        self.assertEqual(game.board.size, 4)
        self.assertEqual(game.game_type, "general")
        self.assertEqual(game.current_player.player_id, 1)
        self.assertEqual(game.players[0].player_id, 1)
        self.assertEqual(game.players[1].player_id, 2)

    if __name__ == '__main__':
        unittest.main()
        