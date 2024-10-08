from abc import ABC, abstractmethod
from typing import Optional


class Something:
    pass


class AbstractUser(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def do(self) -> Optional[Something]:
        pass

    @abstractmethod
    def is_null(self) -> bool:
        pass


class RealUser(AbstractUser):
    def __init__(self, name: str):
        self._name = name

    def get_name(self) -> str:
        return self._name

    def do(self) -> Optional[Something]:
        return Something()

    def is_null(self) -> bool:
        return False


class NullUser(AbstractUser):
    def get_name(self) -> str:
        return "Not Available"

    def do(self) -> Optional[Something]:
        return

    def is_null(self) -> bool:
        return True


class UserFactory:
    _users = {}

    @classmethod
    def get_user(cls, name: str) -> AbstractUser:
        if name not in cls._users:
            cls._users[name] = RealUser(name)
        return cls._users[name]

    @classmethod
    def get_null_user(cls) -> AbstractUser:
        return NullUser()
