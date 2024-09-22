import logging
from abc import ABC, abstractmethod
from typing import Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Mediator(ABC):
    @abstractmethod
    def notify(self, sender: 'Component', event: str):
        pass


class DialogMediator(Mediator):
    def __init__(self):
        self._components = []

    def register(self, component: 'Component'):
        self._components.append(component)
        component.mediator = self

    def notify(self, sender: 'Component', event: str):
        sender.log_inited(event)
        for component in self._components:
            if component != sender:
                component.update(event)


class Component(ABC):
    _mediator: Optional[Mediator]

    def __init__(self, name: str):
        self._mediator = None
        self.name = name

    @property
    def mediator(self):
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator):
        self._mediator = mediator

    @abstractmethod
    def update(self, event: str):
        pass

    def log_inited(self, event: str):
        cls_name: str = self.__class__.__name__
        logger.info(f"{cls_name} {event} by {self.name}. Updating other components...")


class Button(Component):
    def click(self):
        logger.info(f"{self.name} clicked.")
        if self.mediator:
            self.mediator.notify(self, "button_clicked")

    def update(self, event: str):
        logger.info(f"{self.name} updated due to {event}.")


class Checkbox(Component):
    def check(self):
        logger.info(f"{self.name} checked.")
        if self.mediator:
            self.mediator.notify(self, "checkbox_checked")

    def update(self, event: str):
        logger.info(f"{self.name} updated due to {event}.")


class TextBox(Component):
    def update(self, event: str):
        logger.info(f"{self.name} updated due to {event}.")
