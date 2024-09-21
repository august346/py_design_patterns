import unittest

from parameterized import parameterized

from . import Radio, RemoteControl, TV


class TestFactory(unittest.TestCase):
    @parameterized.expand([[Radio], [TV]])
    def test(self, builder: type):
        device = builder(20, 40)
        remote = RemoteControl(device)

        self.assertFalse(device.is_enabled)
        remote.toggle_power()
        self.assertTrue(device.is_enabled)

        self.assertEqual(device.volume, 20)
        remote.volume_up()
        self.assertEqual(device.volume, 21)
        remote.volume_down()
        self.assertEqual(device.volume, 20)

        self.assertEqual(device.channel, 1)
        remote.channel_up()
        self.assertEqual(device.channel, 2)
        remote.channel_down()
        self.assertEqual(device.channel, 1)

        self.assertTrue(device.is_enabled)
        remote.toggle_power()
        self.assertFalse(device.is_enabled)


if __name__ == '__main__':
    unittest.main()
