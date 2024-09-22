from abc import ABC, abstractmethod
from typing import Any


class Iterator(ABC):
    @abstractmethod
    def __next__(self) -> Any:
        pass

    @abstractmethod
    def has_next(self) -> bool:
        pass


class IterableCollection(ABC):
    @abstractmethod
    def create_iterator(self) -> Iterator:
        pass


class ConcreteIterator(Iterator):
    _collection: list[Any]
    _position: int = 0

    def __init__(self, collection: list[Any]):
        self._collection = collection
        self._position = 0

    def __next__(self) -> Any:
        if not self.has_next():
            raise StopIteration
        value = self._collection[self._position]
        self._position += 1
        return value

    def has_next(self) -> bool:
        return self._position < len(self._collection)


class NumberCollection(IterableCollection):
    _numbers: list[int]

    def __init__(self, numbers: list[int]):
        self._numbers = numbers

    def create_iterator(self) -> Iterator:
        return ConcreteIterator(self._numbers)

    def add_number(self, number: int):
        self._numbers.append(number)

    def get_numbers(self) -> list[int]:
        return self._numbers
