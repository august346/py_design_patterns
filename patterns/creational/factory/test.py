import unittest

from parameterized import parameterized

from . import DialogType


class TestFactory(unittest.TestCase):
    @parameterized.expand([["windows", "windows render result"], ["web", "web render result"]])
    def test(self, key: str, expected: str):
        dialog = DialogType.from_str(key)

        self.assertEqual(dialog.render(), expected)
        self.assertEqual(dialog.click(), "<click>")


if __name__ == '__main__':
    unittest.main()
