import unittest
from dataclasses import dataclass

from parameterized import parameterized
import yaml

from . import Factory


@dataclass
class TestData:
    total_price: int
    struct: list[list, int]


with open("patterns/structural/composite/data.yml", "r") as file:
    test_data: list[tuple[TestData]] = [(TestData(**td),) for td in yaml.safe_load(file)]


class TestFactory(unittest.TestCase):
    @parameterized.expand(test_data)
    def test(self, td: TestData):
        box = Factory.build(td.struct)

        self.assertEqual(box.get_price(), td.total_price)


if __name__ == '__main__':
    unittest.main()
