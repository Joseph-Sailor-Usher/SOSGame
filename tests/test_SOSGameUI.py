import sys
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from src.board import Board
from src.game import Game

class TestBoard(unittest.TestCase):
    #User story one
    def test_init(self):
        board_size = 5
        board = Board(board_size)
        self.assertEqual(board.size, board_size)
        self.assertEqual(len(board.board), board_size)
        self.assertEqual(len(board.board[0]), board_size)

    if __name__ == '__main__':
        unittest.main()
    