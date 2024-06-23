import unittest
from calc import Calc

class TestCalc(unittest.TestCase):

    def setUp(self):
        self.calc = Calc()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)

    def test_sub(self):
        self.assertEqual(self.calc.sub(2, 3), -1)
        self.assertEqual(self.calc.sub(5, 2), 3)
        self.assertEqual(self.calc.sub(0, 0), 0)
        self.assertEqual(self.calc.sub(-1, 1), -2)
        self.assertEqual(self.calc.sub(-5, -3), -2)

    def test_mul(self):
        self.assertEqual(self.calc.mul(2, 3), 6)
        self.assertEqual(self.calc.mul(5, 2), 10)
        self.assertEqual(self.calc.mul(0, 5), 0)
        self.assertEqual(self.calc.mul(-1, 1), -1)
        self.assertEqual(self.calc.mul(-5, -3), 15)

    def test_div(self):
        self.assertEqual(self.calc.div(6, 3), 2)
        self.assertEqual(self.calc.div(10, 2), 5)
        self.assertEqual(self.calc.div(5, 2), 2.5)
        self.assertEqual(self.calc.div(0, 5), 0)
        self.assertEqual(self.calc.div(-10, 2), -5)
        self.assertEqual(self.calc.div(-6, -3), 2)

        with self.assertRaises(ZeroDivisionError):
            self.calc.div(5, 0)

    def test_pow(self):
        self.assertEqual(self.calc.pow(2, 3), 8)
        self.assertEqual(self.calc.pow(5, 2), 25)
        self.assertEqual(self.calc.pow(0, 5), 0)
        self.assertEqual(self.calc.pow(-1, 3), -1)
        self.assertEqual(self.calc.pow(-2, 4), 16)

    def test_sqrt(self):
        self.assertEqual(self.calc.sqrt(4), 2)
        self.assertEqual(self.calc.sqrt(9), 3)
        self.assertEqual(self.calc.sqrt(16), 4)
        self.assertEqual(self.calc.sqrt(0), 0)
        self.assertAlmostEqual(self.calc.sqrt(2), 1.41421356237, places=10)

if __name__ == "__main__":
    unittest.main()

