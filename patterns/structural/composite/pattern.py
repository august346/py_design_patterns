from abc import ABC, abstractmethod
from typing import Union


class Priced(ABC):
    @abstractmethod
    def get_price(self) -> int:
        pass


class Item(Priced):
    _price: int

    def __init__(self, price: int):
        self._price = price

    def get_price(self) -> int:
        return self._price


class Box(Priced):
    _items: list[Priced]

    def __init__(self, _items: list[Priced]):
        self._items = _items

    def get_price(self) -> int:
        return sum(map(lambda i: i.get_price(), self._items), 0)


class Factory:
    @staticmethod
    def build(data: Union[int, list[list, int]]) -> Priced:
        if isinstance(data, int):
            return Item(data)

        if isinstance(data, list):
            return Box([Factory.build(i) for i in data])

        raise NotImplemented
