import unittest

from parameterized import parameterized

from . import bin_decorator, func_to_str


class TestDecorator(unittest.TestCase):
    @parameterized.expand(
        [(1, '1'), (2, '10'), (3, '11'), (4, '100'), (5, '101'), (6, '110'), (7, '111'), (8, '1000'), (9, '1001'),
         (10, '1010')]
    )
    def test(self, inp: int, expected_result: str):
        actual_result: str = bin_decorator(func_to_str)(inp)

        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
