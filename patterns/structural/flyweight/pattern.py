from abc import ABC, abstractmethod


class Flyweight(ABC):
    """
    The Flyweight interface declares methods that can be used by clients.
    Concrete Flyweights must be sharable and contain intrinsic data.
    """

    @abstractmethod
    def operation(self, extrinsic_state: str) -> str:
        pass


class ConcreteFlyweight(Flyweight):
    """
    The ConcreteFlyweight stores intrinsic data and shares it across multiple clients.
    """

    def __init__(self, intrinsic_state: str):
        self._intrinsic_state = intrinsic_state

    def operation(self, extrinsic_state: str) -> str:
        return f"Intrinsic: {self._intrinsic_state}, Extrinsic: {extrinsic_state}"


class FlyweightFactory:
    """
    The FlyweightFactory creates and manages flyweights. It ensures that
    flyweights are shared properly.
    """

    def __init__(self):
        self._flyweights: dict[str, Flyweight] = {}

    def get_flyweight(self, intrinsic_state: str) -> Flyweight:
        result: Flyweight

        try:
            result = self._flyweights[intrinsic_state]
        except KeyError:
            result = self._flyweights[intrinsic_state] = ConcreteFlyweight(intrinsic_state)

        return result

    def flyweight_count(self) -> int:
        return len(self._flyweights)

    def clear(self):
        self._flyweights.clear()
