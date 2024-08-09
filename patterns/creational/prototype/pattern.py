from abc import ABC, abstractmethod


class Shape(ABC):
    _x: int
    _y: int
    _color: str

    def __init__(self, x: int, y: int, color: str):
        self._x = x
        self._y = y
        self._color = color

    @abstractmethod
    def clone(self) -> "Shape":
        pass

    def __eq__(self, other: "Shape") -> bool:
        return (
            self._x == other._x
            and self._y == other._y
            and self._color == other._color
        )


class Circle(Shape):
    _radius: int

    def __init__(self, x: int, y: int, color: str, radius: int):
        super().__init__(x, y, color)
        self._radius = radius

    def clone(self) -> "Circle":
        return Circle(self._x, self._y, self._color, self._radius)

    def __eq__(self, other: "Circle") -> bool:
        return super().__eq__(other) and self._radius == other._radius


class Rectangle(Shape):
    _width: int
    _height: int

    def __init__(self, x: int, y: int, color: str, width: int, height: int):
        super().__init__(x, y, color)
        self._width = width
        self._height = height

    @staticmethod
    def new_square(x: int, y: int, color: str, size: int):
        return Rectangle(x, y, color, size, size)

    def clone(self) -> "Rectangle":
        return Rectangle(self._x, self._y, self._color, self._width, self._height)

    def __eq__(self, other: "Rectangle") -> bool:
        return (
                super().__eq__(other)
                and self._width == other._width
                and self._height == other._height
        )
