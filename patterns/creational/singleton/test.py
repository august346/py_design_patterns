import unittest

from . import Singleton


class TestFactory(unittest.TestCase):
    def test(self):
        s_list = [Singleton() for _ in range(10)]
        s = s_list[0]
        for si in s_list[1:]:
            self.assertIs(s, si)
            s = si


if __name__ == '__main__':
    unittest.main()
