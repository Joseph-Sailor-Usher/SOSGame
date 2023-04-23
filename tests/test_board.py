import sys
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from src.board import Board

class TestBoard(unittest.TestCase):
    def test_init(self):
        board = Board(5)
        self.assertEqual(board.size, 5)
        self.assertEqual(len(board.board), 5)
        self.assertEqual(len(board.board[0]), 5)

    def test_is_valid_move(self):
        board = Board(5)
        self.assertTrue(board.is_valid_move(0, 0))
        self.assertFalse(board.is_valid_move(5, 0))
        self.assertFalse(board.is_valid_move(0, 5))

    def test_place_move(self):
        board = Board(5)
        self.assertTrue(board.place_move(0, 0, 'S'))
        self.assertEqual(board.board[0][0], 'S')
        self.assertFalse(board.place_move(0, 0, 'O'))
        self.assertFalse(board.place_move(5, 0, 'S'))

    def test_str(self):
        board = Board(3)
        board.place_move(0, 0, 'S')
        board.place_move(1, 1, 'O')
        expected_output = "S . .\n. O .\n. . ."
        self.assertEqual(str(board), expected_output)

    if __name__ == '__main__':
        unittest.main()
    