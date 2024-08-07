from abc import ABC, abstractmethod


class Designed(ABC):
    @property
    @abstractmethod
    def _type(self) -> str:
        pass

    def get_type(self) -> str:
        return self._type


class ArtDecoDesign:
    _type = "art_deco"


class VictorianDesign:
    _type = "victorian"


class ModernDesign:
    _type = "modern"


class Chair(Designed, ABC):
    pass


class ArtDecoChair(ArtDecoDesign, Chair):
    pass


class VictorianChair(VictorianDesign, Chair):
    pass


class ModernChair(ModernDesign, Chair):
    pass


class Table(Designed, ABC):
    pass


class ArtDecoTable(ArtDecoDesign, Table):
    pass


class VictorianTable(VictorianDesign, Table):
    pass


class ModernTable(ModernDesign, Table):
    pass


class Sofa(Designed, ABC):
    pass


class ArtDecoSofa(ArtDecoDesign, Sofa):
    pass


class VictorianSofa(VictorianDesign, Sofa):
    pass


class ModernSofa(ModernDesign, Sofa):
    pass


class AbstractFurnitureFactory(ABC):
    @staticmethod
    @abstractmethod
    def create_chair() -> Chair:
        pass

    @staticmethod
    @abstractmethod
    def create_table() -> Table:
        pass

    @staticmethod
    @abstractmethod
    def create_sofa() -> Sofa:
        pass


class ArtDecoFurnitureFactory(AbstractFurnitureFactory):
    create_chair = ArtDecoChair
    create_table = ArtDecoTable
    create_sofa = ArtDecoSofa


class VictorianFurnitureFactory(AbstractFurnitureFactory):
    create_chair = VictorianChair
    create_table = VictorianTable
    create_sofa = VictorianSofa


class ModernFurnitureFactory(AbstractFurnitureFactory):
    create_chair = ModernChair
    create_table = ModernTable
    create_sofa = ModernSofa
