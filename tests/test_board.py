import sys
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from src.board import Board

class TestBoard(unittest.TestCase):
    def test_init(self):
        board = Board(5)
        # Add assertions here

    def test_is_valid_move(self):
        board = Board(5)
        # Add assertions here

    def test_make_move(self):
        board = Board(5)
        # Add assertions here

    def test_get_value(self):
        board = Board(5)
        # Add assertions here

    def test_is_full(self):
        board = Board(5)
        # Add assertions here

    def test_count_new_soss(self):
        board = Board(5)
        # Add assertions here

    def test_clear_board(self):
        board = Board(5)
        # Add assertions here

    def test_update_board_size(self):
        board = Board(5)
        # Add assertions here

    def test_str(self):
        board = Board(5)
        # Add assertions here

if __name__ == '__main__':
    unittest.main()
    