import unittest
from first_homework import solve
from math import nan, inf


class TestSolve(unittest.TestCase):

    def test_solve(self):
        self.assertEqual(solve(1, 0, 1), ())
        self.assertEqual(solve(1, 0, -1), (1, -1))
        self.assertEqual(solve(1, 2, 0.999998581), (-1, -1))
        self.assertRaises(ValueError, solve, 0, 3, 5)
        self.assertRaises(ValueError, solve, nan, nan, nan)
        self.assertRaises(ValueError, solve, inf, -inf, inf)
