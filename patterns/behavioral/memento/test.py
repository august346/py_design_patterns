import unittest

from . import Originator, Caretaker


class TestMementoPattern(unittest.TestCase):
    def setUp(self):
        self.originator = Originator("Initial State")
        self.caretaker = Caretaker(self.originator)

    def test_save_restore_state(self):
        self.originator.change_state("State #1")
        self.caretaker.backup()

        self.originator.change_state("State #2")
        self.caretaker.backup()

        self.originator.change_state("State #3")

        self.caretaker.undo()
        self.assertEqual(self.originator.state, "State #2")

        self.caretaker.undo()
        self.assertEqual(self.originator.state, "State #1")

    def test_undo_without_backup(self):
        self.caretaker.undo()
        self.assertEqual(self.originator.state, "Initial State")


if __name__ == '__main__':
    unittest.main()
