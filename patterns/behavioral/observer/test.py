import unittest
from unittest.mock import MagicMock

from . import Subject, ConcreteObserverA, ConcreteObserverB


class TestObserverPattern(unittest.TestCase):
    def test_observer_receives_notifications(self):
        subject = Subject()
        observer_a = ConcreteObserverA()
        observer_b = ConcreteObserverB()

        subject.attach(observer_a)
        subject.attach(observer_b)

        observer_a.update = MagicMock()
        observer_b.update = MagicMock()

        subject.notify("Hello, Observers!")

        observer_a.update.assert_called_once_with("Hello, Observers!")
        observer_b.update.assert_called_once_with("Hello, Observers!")

    def test_detach_observer(self):
        subject = Subject()
        observer_a = ConcreteObserverA()
        observer_b = ConcreteObserverB()

        subject.attach(observer_a)
        subject.attach(observer_b)

        subject.detach(observer_a)

        observer_a.update = MagicMock()
        observer_b.update = MagicMock()

        subject.notify("Hello, Observers!")

        observer_a.update.assert_not_called()
        observer_b.update.assert_called_once_with("Hello, Observers!")


if __name__ == '__main__':
    unittest.main()
