import sys
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

if __name__ == '__main__':
    test_suite = unittest.TestLoader().discover(start_dir=os.path.dirname(__file__))
    unittest.TextTestRunner(verbosity=2).run(test_suite)
