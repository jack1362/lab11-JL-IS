# https://github.com/jack1362/lab11-JL-IS
# Partner 1: Jack Lenhart
# Partner 2: Ishan Sujin

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    ######## Partner 1
    def test_multiply(self):  # 3 assertions
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(-2, 3), -6)
        self.assertEqual(mul(0, 5), 0)

    def test_divide(self):  # 3 assertions
        self.assertEqual(div(2, 10), 5)
        self.assertEqual(div(-2, 10), -5)

        with self.assertRaises(ZeroDivisionError):
            div(0, 10)

    ######## Partner 1
    def test_log_invalid_argument(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self):  # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(-3, 4), 5)

    def test_sqrt(self):  # 3 assertions
        self.assertAlmostEqual(square_root(9), 3)
        self.assertAlmostEqual(square_root(2), 1.41421356237)

        with self.assertRaises(ValueError):
            square_root(-4)

    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()