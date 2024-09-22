import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Memento:
    def __init__(self, state: str):
        self._state = state

    @property
    def state(self) -> str:
        return self._state


class Originator(Memento):
    _state: str

    def save(self) -> Memento:
        return Memento(self._state)

    def restore(self, memento: Memento):
        self._state = memento.state

    def change_state(self, new_state: str):
        self._state = new_state


class Caretaker:
    _mementos: list[Memento] = []

    def __init__(self, originator: Originator):
        self._originator = originator

    def backup(self):
        self._mementos.append(self._originator.save())

    def undo(self):
        if not self._mementos:
            return

        memento = self._mementos.pop()
        self._originator.restore(memento)

    def show_history(self):
        for memento in self._mementos:
            logger.info(memento.state)
