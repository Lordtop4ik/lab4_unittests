import unittest
import triangle


class TriangleTestCase(unittest.TestCase):
    def test_area(self):
        res = triangle.area(6, 4)
        self.assertAlmostEqual(res, 12.0)

    def test_area_zero(self):
        res = triangle.area(0, 4)
        self.assertEqual(res, 0.0)

    def test_perimeter(self):
        res = triangle.perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            triangle.area(-6, 4)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(-3, 4, 5)

    def test_perimeter_nonexistent_triangle(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(1, 2, 10)
