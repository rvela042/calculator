import unittest
from calc import Calc

class TestFileName(unittest.TestCase):
    def add(self):
        self.assertEqual(add(1), 0)

    def sub(self):
        self.assertEqual(sub(2,1), 3)
        self.assertEqual(sub(2.1, 1.2), 3.3)

if __name__ == '__main__':
    unittest.main()