import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class Light:
    def __init__(self):
        self._is_on = False

    def turn_on(self):
        self._is_on = True
        logger.info("Light is on")

    def turn_off(self):
        self._is_on = False
        logger.info("Light is off")

    @property
    def is_on(self) -> bool:
        return self._is_on


class TurnOnCommand(Command):
    def __init__(self, light: Light):
        self._light = light

    def execute(self):
        self._light.turn_on()

    def undo(self):
        self._light.turn_off()


class TurnOffCommand(Command):
    def __init__(self, light: Light):
        self._light = light

    def execute(self):
        self._light.turn_off()

    def undo(self):
        self._light.turn_on()


class RemoteControl:
    def __init__(self):
        self._history = []
        self._current_command = None

    def submit(self, command: Command):
        command.execute()
        self._history.append(command)

    def undo_last(self):
        if self._history:
            command = self._history.pop()
            command.undo()
