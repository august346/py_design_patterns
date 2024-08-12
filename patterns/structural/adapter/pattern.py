import enum
import math
from abc import ABC, abstractmethod


class Fit(ABC):
    @abstractmethod
    def fits(self, some) -> bool:
        pass


class Round(ABC):
    @property
    @abstractmethod
    def radius(self) -> int:
        pass


class RoundObject(Round):
    _radius: int

    def __init__(self, radius: int):
        self._radius = radius

    @property
    def radius(self) -> int:
        return self._radius


class RoundHole(Fit, RoundObject):
    def fits(self, round_: Round) -> bool:
        return self.radius >= round_.radius


class CirclePeg(RoundObject):
    pass


class RoundPegAdapter(Round):
    def __init__(self, peg):
        self.peg = peg

    @abstractmethod
    def radius(self) -> int:
        pass


class SquarePeg:
    width: int

    def __init__(self, width: int):
        self.width = width


class SquarePegAdapter(RoundPegAdapter):
    peg: SquarePeg

    @property
    def radius(self) -> float:
        return self.peg.width * math.sqrt(2) / 2


class TrianglePeg:
    a: int
    b: int
    c: int

    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c


class TrianglePegAdapter(RoundPegAdapter):
    peg: TrianglePeg

    @property
    def radius(self) -> float:
        a, b, c = self.peg.a, self.peg.b, self.peg.c

        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        r = (a * b * c) / (4 * area)

        return r


class PegAdapterFactory:
    @staticmethod
    def build(peg) -> RoundPegAdapter:
        return {
            CirclePeg: lambda _: peg,
            SquarePeg: SquarePegAdapter,
            TrianglePeg: TrianglePegAdapter,
        }[type(peg)](peg)


class PegFactory(enum.Enum):
    CIRCLE = "circle"
    SQUARE = "square"
    TRIANGLE = "triangle"

    @classmethod
    def build(cls, peg_type: str, *args, **kwargs):
        value: PegFactory = PegFactory(peg_type)

        return {
            cls.CIRCLE: CirclePeg,
            cls.SQUARE: SquarePeg,
            cls.TRIANGLE: TrianglePeg,
        }[value](*args, **kwargs)

