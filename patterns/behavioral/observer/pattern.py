import logging
from abc import ABC, abstractmethod

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)


class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass


class ConcreteObserverA(Observer):
    def update(self, message):
        logger.info(f"Observer A received: {message}")


class ConcreteObserverB(Observer):
    def update(self, message):
        logger.info(f"Observer B received: {message}")
