import unittest

from parameterized import parameterized

from . import PegAdapterFactory, PegFactory, RoundHole


class TestFactory(unittest.TestCase):
    @parameterized.expand(
        [
            [5, ("circle", 5), True],
            [5, ("circle", 6), False],
            [5, ("square", 7), True],
            [5, ("square", 10), False],
            [5, ("triangle", 8, 8, 8), True],
            [5, ("triangle", 10, 10, 10), False],
        ]
    )
    def test(self, hole_radius: int, peg_build_params: tuple, is_fit: bool):
        round_hole = RoundHole(hole_radius)
        peg = PegFactory.build(*peg_build_params)
        adapter = PegAdapterFactory.build(peg)

        assert_method = self.assertTrue if is_fit else self.assertFalse
        assert_method(round_hole.fits(adapter))


if __name__ == '__main__':
    unittest.main()
