import enum
from abc import ABC, abstractmethod
from typing import Callable


class DialogType(enum.Enum):
    WINDOWS = "windows"
    WEB = "web"

    @staticmethod
    def from_str(string: str) -> "Dialog":
        try:
            dialog_type = DialogType(string)
        except TypeError:
            raise ValueError(f"invalid dialog_type={string}")

        return {
            DialogType.WINDOWS: WindowsDialog,
            DialogType.WEB: WebDialog,
        }[dialog_type]()


class Dialog(ABC):
    _btn: "Button"

    @staticmethod
    @abstractmethod
    def create_button() -> "Button":
        pass

    def render(self) -> str:
        self._btn = self.create_button()
        self._btn.on_click(lambda: "<click>")

        return self._btn.render()

    def click(self) -> str:
        try:
            return self._btn.click()
        except AttributeError:
            raise RuntimeError("not rendered yet")


class WindowsDialog(Dialog):

    @staticmethod
    def create_button() -> "Button":
        return WindowsButton()


class WebDialog(Dialog):

    @staticmethod
    def create_button() -> "Button":
        return WebButton()


class Button(ABC):
    _on_click: Callable[[], str]

    @abstractmethod
    def render(self) -> str:
        pass

    def on_click(self, func: Callable[[], str]):
        self._on_click = func

    def click(self) -> str:
        return self._on_click()


class WindowsButton(Button):
    def render(self) -> str:
        return "windows render result"


class WebButton(Button):
    def render(self) -> str:
        return "web render result"
