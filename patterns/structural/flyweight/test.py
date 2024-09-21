import unittest

from parameterized import parameterized

from . import FlyweightFactory


class TestFlyweight(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.factory = FlyweightFactory()

    def setUp(self):
        self.factory.clear()

    @parameterized.expand([
        ["A", "Extrinsic1"],
        ["B", "Extrinsic2"],
        ["A", "Extrinsic3"],
        ["C", "Extrinsic4"],
    ])
    def test_flyweight(self, intrinsic_state: str, extrinsic_state: str):
        flyweight = self.factory.get_flyweight(intrinsic_state)
        result = flyweight.operation(extrinsic_state)

        expected_result = f"Intrinsic: {intrinsic_state}, Extrinsic: {extrinsic_state}"
        self.assertEqual(result, expected_result)

    def test_flyweight_sharing(self):
        flyweight1 = self.factory.get_flyweight("A")
        flyweight2 = self.factory.get_flyweight("A")
        self.assertIs(flyweight1, flyweight2)
        self.assertEqual(self.factory.flyweight_count(), 1)

        flyweight3 = self.factory.get_flyweight("B")
        self.assertIsNot(flyweight1, flyweight3)
        self.assertEqual(self.factory.flyweight_count(), 2)


if __name__ == '__main__':
    unittest.main()
