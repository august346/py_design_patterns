import unittest
from typing import Callable

from parameterized import parameterized

from . import Circle, Shape, Rectangle


class TestFactory(unittest.TestCase):
    @parameterized.expand(
        [
            [lambda: Circle(0, 0, "red", 75)],
            [lambda: Rectangle(50, 10, "blue", 100, 50)],
            [lambda: Rectangle.new_square(-30, 40, "green", 120)],
        ]
    )
    def test(self, create_object: Callable[[], Shape]):
        obj = create_object()
        obj_cloned = obj.clone()

        self.assertIsNot(obj, obj_cloned)
        self.assertEqual(obj, obj_cloned)


if __name__ == '__main__':
    unittest.main()
