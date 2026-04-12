from base import Patient
from models import Inpatient, Outpatient
class PatientCollection:
    def __init__(self):
        self._items = []
    
    def add(self, item):
        if not hasattr(item, '_name'):
            raise TypeError("Можно добавлять только объекты Patient и его наследников")
        self._items.append(item)
    
    def remove(self, item):
        if item not in self._items:
            raise ValueError("Объект не найден в коллекции")
        self._items.remove(item)
    
    def remove_at(self, index):
        if index < 0 or index >= len(self._items):
            raise IndexError("Индекс вне диапазона")
        return self._items.pop(index)
    
    def get_all(self):
        return self._items.copy()
    
    def __len__(self):
        return len(self._items)
    
    def __iter__(self):
        return iter(self._items)
    
    def __getitem__(self, index):
        if isinstance(index, slice):
            new_collection = PatientCollection()
            for item in self._items[index]:
                new_collection.add(item)
            return new_collection
        return self._items[index]
    
    def get_by_type(self, class_type):
        new_collection = PatientCollection()
        for item in self._items:
            if isinstance(item, class_type):
                new_collection.add(item)
        return new_collection
    
    def get_inpatients(self):
        return self.get_by_type(Inpatient)
    
    def get_outpatients(self):
        return self.get_by_type(Outpatient)
    
    def calculate_total_cost(self):
        total = 0
        for item in self._items:
            total += item.calculate_treatment_cost()
        return total