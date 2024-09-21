from abc import ABC, abstractmethod


class Flyweight(ABC):
    @abstractmethod
    def operation(self, extrinsic_state: str) -> str:
        pass


class ConcreteFlyweight(Flyweight):
    def __init__(self, intrinsic_state: str):
        self._intrinsic_state = intrinsic_state

    def operation(self, extrinsic_state: str) -> str:
        return f"Intrinsic: {self._intrinsic_state}, Extrinsic: {extrinsic_state}"


class FlyweightFactory:
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
