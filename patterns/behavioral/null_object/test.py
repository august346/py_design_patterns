import unittest
from typing import Callable, Optional

from parameterized import parameterized

from . import UserFactory, NullUser, RealUser, AbstractUser, Something


class TestNullObjectPattern(unittest.TestCase):
    @parameterized.expand(
        [
            [lambda: UserFactory.get_user("Alice"), "Alice", False, True],
            [lambda: UserFactory.get_null_user(), "Not Available", True, False],
        ]
    )
    def test(self, get_user: Callable[[], AbstractUser], name: str, is_null: bool, result_is_something: bool):
        user: AbstractUser = get_user()
        self.assertEqual(user.get_name(), name)
        [self.assertFalse, self.assertTrue][is_null](user.is_null())
        [self.assertIsNone, self.assertIsNotNone][result_is_something](user.do())

    def test_user_not_found(self):
        user_name = "Bob"
        user = UserFactory.get_user(user_name)
        self.assertEqual(user.get_name(), "Bob")

        user2 = UserFactory.get_user(user_name)
        self.assertIs(user, user2)

        null_user = UserFactory.get_null_user()
        self.assertEqual(null_user.get_name(), "Not Available")


if __name__ == '__main__':
    unittest.main()
