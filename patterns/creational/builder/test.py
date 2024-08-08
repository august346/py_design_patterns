import unittest

from parameterized import parameterized

from . import ProductType


class TestFactory(unittest.TestCase):
    @parameterized.expand([["car", "I'm a car"], ["manual", "I'm a manual"]])
    def test(self, key: str, expected: str):
        product = ProductType.from_str(key)

        self.assertEqual(product.who_are_you(), expected)


if __name__ == '__main__':
    unittest.main()
