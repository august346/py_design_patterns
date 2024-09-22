import logging
from abc import ABC, abstractmethod

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class State(ABC):
    @abstractmethod
    def play(self, player):
        pass

    @abstractmethod
    def pause(self, player):
        pass

    @abstractmethod
    def stop(self, player):
        pass


class PlayingState(State):
    def play(self, player):
        logger.info("Already playing.")

    def pause(self, player):
        logger.info("Pausing the player.")
        player.set_state(PausedState())

    def stop(self, player):
        logger.info("Stopping the player.")
        player.set_state(StoppedState())


class PausedState(State):
    def play(self, player):
        logger.info("Resuming the player.")
        player.set_state(PlayingState())

    def pause(self, player):
        logger.info("Already paused.")

    def stop(self, player):
        logger.info("Stopping the player.")
        player.set_state(StoppedState())


class StoppedState(State):
    def play(self, player):
        logger.info("Starting the player.")
        player.set_state(PlayingState())

    def pause(self, player):
        logger.info("Can't pause. The player is stopped.")

    def stop(self, player):
        logger.info("Already stopped.")


class AudioPlayer:
    def __init__(self):
        self._state = StoppedState()

    def set_state(self, state: State):
        self._state = state

    def play(self):
        self._state.play(self)

    def pause(self):
        self._state.pause(self)

    def stop(self):
        self._state.stop(self)
