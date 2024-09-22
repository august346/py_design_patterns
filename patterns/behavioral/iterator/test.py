import unittest

from . import NumberCollection


class TestIteratorPattern(unittest.TestCase):
    def test_iterator_traversal(self):
        numbers = [1, 2, 3, 4, 5]
        collection = NumberCollection(numbers)
        iterator = collection.create_iterator()

        result = []
        while iterator.has_next():
            result.append(next(iterator))

        self.assertEqual(result, numbers)

    def test_iterator_with_empty_collection(self):
        collection = NumberCollection([])
        iterator = collection.create_iterator()

        with self.assertRaises(StopIteration):
            next(iterator)

    def test_add_element_and_traverse(self):
        collection = NumberCollection([10, 20, 30])
        collection.add_number(40)

        iterator = collection.create_iterator()

        result = []
        while iterator.has_next():
            result.append(next(iterator))

        self.assertEqual(result, [10, 20, 30, 40])


if __name__ == "__main__":
    unittest.main()
