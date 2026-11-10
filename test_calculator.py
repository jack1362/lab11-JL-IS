# https://github.com/jack1362/lab11-JL-IS
# Partner 1: Jack Lenhart
# Partner 2: Ishan Sujin

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(2,3), 5)
        self.assertEqual(add(1, 1), 2)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(6, 1), 5)
        self.assertEqual(subtract(1, 1), 0)



    ######## Partner 1
    def test_multiply(self):  # 3 assertions
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(-2, 3), -6)
        self.assertEqual(mul(0, 5), 0)

    def test_divide(self):  # 3 assertions
        self.assertEqual(div(2, 10), 5)
        self.assertEqual(div(-2, 10), -5)
        self.assertEqual(div(1, 1), 1)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 10)

    def test_logarithm(self):
        self.assertEqual(logarithm(2, 8), 3.0)
        self.assertEqual(logarithm(10, 100), 2.0)
        self.assertEqual(logarithm(3, 9), 2.0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1, 8)
    

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
        self.assertAlmostEqual(square_root(4), 2)

        with self.assertRaises(ValueError):
            square_root(-4)

# Do not touch this
if __name__ == "__main__":
    unittest.main()