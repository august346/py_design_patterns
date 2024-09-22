import unittest

from . import UserFactory, NullUser, RealUser


class TestNullObjectPattern(unittest.TestCase):
    def test_real_user(self):
        user = UserFactory.get_user("Alice")
        self.assertIsInstance(user, RealUser)
        self.assertEqual(user.get_name(), "Alice")
        self.assertFalse(user.is_null())

    def test_null_user(self):
        user = UserFactory.get_null_user()
        self.assertIsInstance(user, NullUser)
        self.assertEqual(user.get_name(), "Not Available")
        self.assertTrue(user.is_null())

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
