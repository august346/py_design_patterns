import unittest

from parameterized import parameterized

from . import AbstractFurnitureFactory, ArtDecoFurnitureFactory, VictorianFurnitureFactory, ModernFurnitureFactory


class TestAbstractFactory(unittest.TestCase):
    @parameterized.expand(
        [
            [ArtDecoFurnitureFactory, "art_deco"],
            [VictorianFurnitureFactory, "victorian"],
            [ModernFurnitureFactory, "modern"],
        ]
    )
    def test(self, factory: AbstractFurnitureFactory, design_type: str):
        furniture = [
            factory.create_chair(),
            factory.create_table(),
            factory.create_sofa(),
        ]

        for f in furniture:
            self.assertEqual(f.get_type(), design_type)


if __name__ == '__main__':
    unittest.main()
