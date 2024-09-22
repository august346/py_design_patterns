import unittest

from . import AudioPlayer, PlayingState, PausedState, StoppedState


class TestAudioPlayerState(unittest.TestCase):
    def test_initial_state(self):
        player = AudioPlayer()
        self.assertIsInstance(player._state, StoppedState)

    def test_play_from_stopped(self):
        player = AudioPlayer()
        player.play()
        self.assertIsInstance(player._state, PlayingState)

    def test_pause_from_playing(self):
        player = AudioPlayer()
        player.play()
        player.pause()
        self.assertIsInstance(player._state, PausedState)

    def test_stop_from_playing(self):
        player = AudioPlayer()
        player.play()
        player.stop()
        self.assertIsInstance(player._state, StoppedState)

    def test_pause_from_paused(self):
        player = AudioPlayer()
        player.play()
        player.pause()
        player.pause()
        self.assertIsInstance(player._state, PausedState)

    def test_play_from_paused(self):
        player = AudioPlayer()
        player.play()
        player.pause()
        player.play()
        self.assertIsInstance(player._state, PlayingState)

    def test_stop_from_paused(self):
        player = AudioPlayer()
        player.play()
        player.pause()
        player.stop()
        self.assertIsInstance(player._state, StoppedState)

    def test_stop_when_already_stopped(self):
        player = AudioPlayer()
        player.stop()
        self.assertIsInstance(player._state, StoppedState)


if __name__ == '__main__':
    unittest.main()
