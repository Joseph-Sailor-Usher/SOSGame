import sys
import os
import unittest
from tkinter import Tk
from unittest.mock import patch

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
class TestBoard(unittest.TestCase):
    #User story one
    def test_init(self):
        pass

    if __name__ == '__main__':
        unittest.main()
    