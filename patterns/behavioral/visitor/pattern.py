from abc import ABC, abstractmethod
import math
from typing import Optional, Any


class ShapeVisitor(ABC):
    result: Optional[Any]

    def __init__(self):
        self.result = None

    @abstractmethod
    def visit_circle(self, circle: "Circle"):
        pass

    @abstractmethod
    def visit_rectangle(self, rectangle: "Rectangle"):
        pass

    @abstractmethod
    def visit_triangle(self, triangle: "Triangle"):
        pass


class Shape(ABC):
    @abstractmethod
    def accept(self, visitor: ShapeVisitor):
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def accept(self, visitor: ShapeVisitor):
        visitor.visit_circle(self)


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def accept(self, visitor: ShapeVisitor):
        visitor.visit_rectangle(self)


class Triangle(Shape):
    def __init__(self, side_a: float, side_b: float, side_c: float):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def accept(self, visitor: ShapeVisitor):
        visitor.visit_triangle(self)


class AreaVisitor(ShapeVisitor):
    def visit_circle(self, circle: Circle):
        self.result = math.pi * (circle.radius ** 2)

    def visit_rectangle(self, rectangle: Rectangle):
        self.result = rectangle.width * rectangle.height

    def visit_triangle(self, triangle: Triangle):
        s = (triangle.side_a + triangle.side_b + triangle.side_c) / 2
        self.result = math.sqrt(s * (s - triangle.side_a) * (s - triangle.side_b) * (s - triangle.side_c))


class PerimeterVisitor(ShapeVisitor):
    def visit_circle(self, circle: Circle):
        self.result = 2 * math.pi * circle.radius

    def visit_rectangle(self, rectangle: Rectangle):
        self.result = 2 * (rectangle.width + rectangle.height)

    def visit_triangle(self, triangle: Triangle):
        self.result = triangle.side_a + triangle.side_b + triangle.side_c
