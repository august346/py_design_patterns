from abc import ABC, abstractmethod


class Device(ABC):
    _is_enabled: bool
    _volume: int
    _channel: int

    max_channels: int

    def __init__(self, volume: int, max_channels: int):
        self._is_enabled = False
        self._volume = volume
        self._channel = 1

        self.max_channels = max_channels

    @property
    @abstractmethod
    def is_enabled(self) -> bool:
        pass

    @abstractmethod
    def enable(self):
        pass

    @abstractmethod
    def disable(self):
        pass

    @property
    @abstractmethod
    def volume(self) -> int:
        pass

    @abstractmethod
    def set_volume(self, percent: int):
        pass

    @property
    @abstractmethod
    def channel(self) -> int:
        pass

    @abstractmethod
    def set_channel(self, channel: int):
        pass


class RemoteControl:
    _device: Device

    def __init__(self, device: Device):
        self._device = device

    def toggle_power(self):
        if self._device.is_enabled:
            self._device.disable()
        else:
            self._device.enable()

    def volume_down(self):
        self._device.set_volume(max(0, self._device.volume - 1))

    def volume_up(self):
        self._device.set_volume(min(100, self._device.volume + 1))

    def channel_down(self):
        value = self._device.channel - 1
        if value < 1:
            value = self._device.max_channels

        self._device.set_channel(value)

    def channel_up(self):
        value = self._device.channel + 1
        if value > self._device.max_channels:
            value = 1

        self._device.set_channel(value)


class TV(Device):
    @property
    def is_enabled(self) -> bool:
        return self._is_enabled

    def enable(self):
        self._is_enabled = True

    def disable(self):
        self._is_enabled = False

    @property
    def volume(self) -> int:
        return self._volume

    def set_volume(self, percent: int):
        self._volume = percent

    @property
    def channel(self) -> int:
        return self._channel

    def set_channel(self, channel: int):
        if 1 <= channel <= self.max_channels:
            self._channel = channel


class Radio(Device):
    @property
    def is_enabled(self) -> bool:
        return self._is_enabled

    def enable(self):
        self._is_enabled = True

    def disable(self):
        self._is_enabled = False

    @property
    def volume(self) -> int:
        return self._volume

    def set_volume(self, percent: int):
        self._volume = percent

    @property
    def channel(self) -> int:
        return self._channel

    def set_channel(self, channel: int):
        if 1 <= channel <= self.max_channels:
            self._channel = channel
