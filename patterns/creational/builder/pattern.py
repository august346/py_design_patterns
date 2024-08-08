import enum
from abc import ABC, abstractmethod


class ProductType(enum.Enum):
    CAR = "car"
    MANUAL = "manual"

    @staticmethod
    def from_str(value: str) -> "Product":
        try:
            product_type = ProductType(value)
        except TypeError:
            raise ValueError(f"invalid product_type={value}")

        director = Director()
        builder = {
            ProductType.CAR: CarBuilder,
            ProductType.MANUAL: ManualBuilder,
        }[product_type]()
        director.construct_sport_car(builder)

        return builder.get_product()


class Product(ABC):
    @property
    @abstractmethod
    def title(self) -> str:
        pass

    def who_are_you(self) -> str:
        return f"I'm a {self.title}"


class Builder(ABC):
    _product: Product

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def set_seats(self, num: int):
        pass

    @abstractmethod
    def set_engine(self, engine: "Engine"):
        pass

    @abstractmethod
    def set_trip_computer(self):
        pass

    @abstractmethod
    def set_gps(self):
        pass

    def get_product(self):
        return self._product


class Director:
    @staticmethod
    def construct_sport_car(builder: Builder):
        builder.set_seats(2)
        builder.set_engine(SportEngine())
        builder.set_trip_computer()
        builder.set_gps()


class Engine(ABC):
    pass


class SportEngine(Engine):
    pass


class CarBuilder(Builder):
    def __init__(self):
        self._product = Car()

    def set_seats(self, num: int):
        pass

    def set_engine(self, engine: "Engine"):
        pass

    def set_trip_computer(self):
        pass

    def set_gps(self):
        pass


class Car(Product):
    title = "car"


class ManualBuilder(Builder):
    def __init__(self):
        self._product = Manual()

    def set_seats(self, num: int):
        pass

    def set_engine(self, engine: "Engine"):
        pass

    def set_trip_computer(self):
        pass

    def set_gps(self):
        pass


class Manual(Product):
    title = "manual"
