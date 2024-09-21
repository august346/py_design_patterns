import unittest

from . import Light, TurnOnCommand, TurnOffCommand, RemoteControl


class TestCommandPattern(unittest.TestCase):
    def setUp(self):
        self.light = Light()
        self.remote = RemoteControl()

    def test_turn_on_light(self):
        turn_on = TurnOnCommand(self.light)

        self.assertFalse(self.light.is_on)
        self.remote.submit(turn_on)
        self.assertTrue(self.light.is_on)

    def test_turn_off_light(self):
        turn_on = TurnOnCommand(self.light)
        turn_off = TurnOffCommand(self.light)

        self.remote.submit(turn_on)
        self.assertTrue(self.light.is_on)

        self.remote.submit(turn_off)
        self.assertFalse(self.light.is_on)

    def test_undo_command(self):
        turn_on = TurnOnCommand(self.light)
        turn_off = TurnOffCommand(self.light)

        self.remote.submit(turn_on)
        self.assertTrue(self.light.is_on)

        self.remote.submit(turn_off)
        self.assertFalse(self.light.is_on)

        self.remote.undo_last()
        self.assertTrue(self.light.is_on)

        self.remote.undo_last()
        self.assertFalse(self.light.is_on)


if __name__ == '__main__':
    unittest.main()
