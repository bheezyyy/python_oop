from typing import TypeVar, Generic, Callable, Optional, Protocol
from model import Patient

T = TypeVar('T')
R = TypeVar('R')

class Displayable(Protocol):
    def get_printable_info(self) -> str:
        ...

class AgeComparable(Protocol):
    def compare_age(self, other) -> int:
        ...

D = TypeVar('D', bound=Displayable)
A = TypeVar('A', bound=AgeComparable)

class TypedCollection(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []
    
    def add(self, item: T) -> None:
        if not isinstance(item, (Patient,)):
            raise TypeError(f"Можно добавлять только объекты Patient, получен {type(item).__name__}")
        self._items.append(item)
    
    def remove(self, item: T) -> None:
        if item not in self._items:
            raise ValueError("Объект не найден в коллекции")
        self._items.remove(item)
    
    def remove_at(self, index: int) -> T:
        if index < 0 or index >= len(self._items):
            raise IndexError("Индекс вне диапазона")
        return self._items.pop(index)
    
    def get_all(self) -> list[T]:
        return self._items.copy()
    
    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        for item in self._items:
            if predicate(item):
                return item
        return None
    
    def filter(self, predicate: Callable[[T], bool]) -> list[T]:
        return [item for item in self._items if predicate(item)]
    
    def map(self, transform: Callable[[T], R]) -> list[R]:
        return [transform(item) for item in self._items]
    
    def sort(self, key_func: Callable[[T], any], reverse: bool = False) -> None:
        self._items.sort(key=key_func, reverse=reverse)
    
    def __len__(self) -> int:
        return len(self._items)
    
    def __iter__(self):
        return iter(self._items)
    
    def __getitem__(self, index: int) -> T:
        return self._items[index]