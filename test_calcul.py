# test_calcul.py

import unittest
from calcul import addition, division

class TestCalcul(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(addition(3, 5), 8)
        self.assertEqual(addition(-2, 2), 0)

    def test_division(self):
        self.assertEqual(division(10, 2), 5)
        self.assertAlmostEqual(division(7, 3), 2.3333, places=4)

    def test_division_par_zero(self):
        with self.assertRaises(ValueError):
            division(10, 0)

if __name__ == '__main__':
    unittest.main()