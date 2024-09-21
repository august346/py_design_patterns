import logging
import tempfile
import unittest

from parameterized import parameterized

from . import CompressionDecorator, FileDataSource, EncryptionDecorator, bin_decorator, func_to_str


class TestDecorator(unittest.TestCase):
    @parameterized.expand(
        [(1, '1'), (2, '10'), (3, '11'), (4, '100'), (5, '101'), (6, '110'), (7, '111'), (8, '1000'), (9, '1001'),
         (10, '1010')]
    )
    def test(self, inp: int, expected_result: str):
        actual_result: str = bin_decorator(func_to_str)(inp)

        self.assertEqual(actual_result, expected_result)


class TestClassBasedDecorator(unittest.TestCase):
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.file_name = self.temp_file.name
        self.temp_file.close()

    def tearDown(self):
        try:
            self.temp_file.close()
        except Exception as e:
            logging.warning(e)

    @parameterized.expand([["foo"], ["bar"], ["baz"]])
    def test(self, inp: str):
        fds = FileDataSource(self.file_name)
        cds = CompressionDecorator(fds)
        eds = EncryptionDecorator(cds, "secret_key")

        eds.write(inp)

        self.assertEqual(eds.read(), inp)


if __name__ == '__main__':
    unittest.main()
