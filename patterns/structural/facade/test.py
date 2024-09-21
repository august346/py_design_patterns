import unittest
from unittest import mock

from . import ComputerFacade


class TestComputerFacade(unittest.TestCase):
    @mock.patch('builtins.print')
    def test_computer_start(self, mock_print):
        computer = ComputerFacade()
        computer.start()

        mock_print.assert_any_call("CPU freezing.")
        mock_print.assert_any_call("HardDrive reading 1024 bytes from LBA 0.")
        mock_print.assert_any_call("Memory loading data 'data' at position 0.")
        mock_print.assert_any_call("CPU jumping to position 0.")
        mock_print.assert_any_call("CPU executing instructions.")


if __name__ == '__main__':
    unittest.main()
