import unittest
from parameterized import parameterized

from . import Add, Subtract, Multiply, Divide, Number


class TestInterpreterPattern(unittest.TestCase):

    @parameterized.expand([
        (Add(Number(5), Number(10)), 15),
        (Subtract(Number(10), Number(5)), 5),
        (Multiply(Number(5), Number(10)), 50),
        (Divide(Number(10), Number(5)), 2),
        (Multiply(Add(Number(5), Number(10)), Number(2)), 30),
        (Multiply(
            Add(Number(5), Subtract(Number(10), Number(3))),
            Add(Number(2), Number(1))
        ), 36),
    ])
    def test_operations(self, expression, expected):
        self.assertEqual(expression.interpret(), expected)

    @parameterized.expand([(Divide(Number(10), Number(0)), ZeroDivisionError)])
    def test_exceptions(self, expression, exception):
        with self.assertRaises(exception):
            expression.interpret()


if __name__ == '__main__':
    unittest.main()
