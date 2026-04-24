from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def get_printable_info(self) -> str:
        """Возвращает строковое представление объекта"""
        pass

class Serializable(ABC):
    @abstractmethod
    def to_dict(self) -> dict:
        """Сериализует объект в словарь"""
        pass
    
    @classmethod
    @abstractmethod
    def from_dict(cls, data: dict):
        """Создает объект из словаря"""
        pass

class AgeComparable(ABC):
    @abstractmethod
    def compare_age(self, other) -> int:
        """Сравнивает объекты по возрасту. Возвращает -1, 0, 1"""
        pass