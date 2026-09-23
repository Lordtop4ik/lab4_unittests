import unittest
import math
import circle


class CircleTestCase(unittest.TestCase):
    def test_area(self):
        res = circle.area(5)
        self.assertAlmostEqual(res, math.pi * 25)

    def test_area_zero(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_perimeter(self):
        res = circle.perimeter(5)
        self.assertAlmostEqual(res, 2 * math.pi * 5)

    def test_perimeter_zero(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            circle.area(-5)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            circle.perimeter(-5)
