import unittest
import rectangle


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = rectangle.area(10, 10)
        self.assertEqual(res, 100)

    def test_area(self):
        res = rectangle.area(10, 5)
        self.assertEqual(res, 50)

    def test_perimeter(self):
        res = rectangle.perimeter(10, 5)
        self.assertEqual(res, 30)

    def test_perimeter_zero(self):
        res = rectangle.perimeter(10, 0)
        self.assertEqual(res, 20)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            rectangle.area(-5, 10)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(-5, 10)
