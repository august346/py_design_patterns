import operator
from abc import ABC, abstractmethod


class Expression(ABC):
    @abstractmethod
    def interpret(self) -> int:
        pass


class Number(Expression):
    def __init__(self, value: int):
        self._value = value

    def interpret(self) -> int:
        return self._value


class BinaryOperation(Expression, ABC):
    def __init__(self, left: Expression, right: Expression):
        self._left = left
        self._right = right

    @property
    @abstractmethod
    def operator(self):
        pass

    def interpret(self) -> int:
        return self.operator(self._left.interpret(), self._right.interpret())


class Add(BinaryOperation):
    @property
    def operator(self):
        return operator.add


class Subtract(BinaryOperation):
    @property
    def operator(self):
        return operator.sub


class Multiply(BinaryOperation):
    @property
    def operator(self):
        return operator.mul


class Divide(BinaryOperation):
    @property
    def operator(self):
        return operator.floordiv
