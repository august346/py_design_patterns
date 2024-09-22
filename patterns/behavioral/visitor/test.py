import math
import unittest
from parameterized import parameterized

from . import Circle, Rectangle, Triangle, AreaVisitor, PerimeterVisitor, ShapeVisitor, Shape


class TestVisitorPattern(unittest.TestCase):
    @parameterized.expand([
        [Circle(5), AreaVisitor(), math.pi * 25],   # Area of Circle (π * r^2)
        [Circle(5), PerimeterVisitor(), 2 * math.pi * 5],   # Perimeter of Circle (2 * π * r)
        [Rectangle(4, 5), AreaVisitor(), 20],   # Area of Rectangle (width * height)
        [Rectangle(4, 5), PerimeterVisitor(), 18],  # Perimeter of Rectangle (2 * (w + h))
        [Triangle(3, 4, 5), AreaVisitor(), 6],  # Area of Triangle (Heron's formula)
        [Triangle(3, 4, 5), PerimeterVisitor(), 12],    # Perimeter of Triangle (sum of sides)
    ])
    def test_visitor(self, shape: Shape, visitor: ShapeVisitor, expected):
        shape.accept(visitor)
        self.assertAlmostEqual(visitor.result, expected)


if __name__ == '__main__':
    unittest.main()
