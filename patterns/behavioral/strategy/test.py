import unittest
from parameterized import parameterized

from . import BubbleSortStrategy, QuickSortStrategy, InsertionSortStrategy, Sorter


class TestStrategyPattern(unittest.TestCase):
    @parameterized.expand([
        [BubbleSortStrategy, [3, 1, 4, 1, 5, 9, 2], [1, 1, 2, 3, 4, 5, 9]],
        [QuickSortStrategy, [10, 7, 8, 9, 1, 5], [1, 5, 7, 8, 9, 10]],
        [InsertionSortStrategy, [2, 5, 6, 1, 3, 7, 4], [1, 2, 3, 4, 5, 6, 7]],
    ])
    def test_sorting(self, strategy_class, data, expected):
        strategy = strategy_class()
        sorter = Sorter(strategy)
        sorted_data = sorter.sort(data)
        self.assertEqual(sorted_data, expected)

    def test_change_strategy(self):
        data = [4, 2, 7, 3, 8, 6]

        sorter = Sorter(BubbleSortStrategy())
        self.assertEqual(sorter.sort(data.copy()), [2, 3, 4, 6, 7, 8])

        sorter.set_strategy(QuickSortStrategy())
        self.assertEqual(sorter.sort(data.copy()), [2, 3, 4, 6, 7, 8])

        sorter.set_strategy(InsertionSortStrategy())
        self.assertEqual(sorter.sort(data.copy()), [2, 3, 4, 6, 7, 8])


if __name__ == '__main__':
    unittest.main()
