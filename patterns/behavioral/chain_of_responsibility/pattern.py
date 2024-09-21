from abc import ABC, abstractmethod
from typing import Optional


class Handler(ABC):
    _next_handler: Optional['Handler'] = None

    def set_next(self, handler: 'Handler') -> 'Handler':
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: str) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class AuthenticationHandler(Handler):
    def handle(self, request: str) -> Optional[str]:
        if request == "authenticate":
            return "User authenticated"

        return super().handle(request)


class AuthorizationHandler(Handler):
    def handle(self, request: str) -> Optional[str]:
        if request == "authorize":
            return "User authorized"

        return super().handle(request)


class LoggingHandler(Handler):
    def handle(self, request: str) -> Optional[str]:
        if request == "log":
            return "Logging request"

        return super().handle(request)


class ErrorHandler(Handler):
    def handle(self, request: str) -> Optional[str]:
        if request == "error":
            return "Handling error"

        return super().handle(request)
