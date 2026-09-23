import unittest
import square


class SquareTestCase(unittest.TestCase):
    def test_area(self):
        res = square.area(4)
        self.assertEqual(res, 16)

    def test_area_zero(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_perimeter(self):
        res = square.perimeter(4)
        self.assertEqual(res, 16)

    def test_perimeter_zero(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            square.area(-4)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            square.perimeter(-4)
