import unittest

from parameterized import parameterized

from .pattern import SecureDataWrapper


class TestPrivateClassData(unittest.TestCase):
    def setUp(self):
        self.wrapper = SecureDataWrapper(
            sensitive_info="secret_key_123",
            configuration={"setting1": "value1", "setting2": "value2"}
        )

    def test_sensitive_info_access(self):
        self.assertEqual(self.wrapper.view_sensitive_info(), "secret_key_123")

    def test_configuration_access(self):
        config = self.wrapper.view_configuration()
        self.assertDictEqual(config, {"setting1": "value1", "setting2": "value2"})

    @parameterized.expand([
        ("setting1", "new_value1"),
        ("setting2", "new_value2"),
    ])
    def test_modify_configuration(self, key, new_value):
        self.wrapper.modify_configuration(key, new_value)
        config = self.wrapper.view_configuration()
        self.assertEqual(config[key], new_value)

    def test_invalid_configuration_key(self):
        with self.assertRaises(KeyError):
            self.wrapper.modify_configuration("invalid_setting", "new_value")


if __name__ == '__main__':
    unittest.main()
