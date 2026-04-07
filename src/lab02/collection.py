

from model import Patient

class PatientCollection:
    """Коллекция для хранения объектов Patient"""
    
    def __init__(self):
        """Конструктор - создает пустой список для хранения пациентов"""
        self._items = []
    
    def add(self, item):
        """Добавляет пациента в коллекцию. Проверяет тип и уникальность имени"""
        if not isinstance(item, Patient):
            raise TypeError("Можно добавлять только объекты Patient")
        if self._find_by_name(item.name):
            raise ValueError(f"Пациент с именем {item.name} уже существует")
        self._items.append(item)
    
    def remove(self, item):
        """Удаляет пациента из коллекции по объекту"""
        if item not in self._items:
            raise ValueError("Объект не найден в коллекции")
        self._items.remove(item)
    
    def remove_at(self, index):
        """Удаляет пациента по индексу и возвращает его"""
        if index < 0 or index >= len(self._items):
            raise IndexError("Индекс вне диапазона")
        return self._items.pop(index)
    
    def get_all(self):
        """Возвращает копию списка всех пациентов"""
        return self._items.copy()
    
    def find_by_name(self, name):
        """Ищет пациента по имени (регистронезависимо). Возвращает первого найденного или None"""
        return self._find_by_name(name)
    
    def _find_by_name(self, name):
        """Внутренний метод для поиска по имени"""
        for item in self._items:
            if item.name.lower() == name.lower():
                return item
        return None
    
    def find_by_diagnosis(self, diagnosis):
        """Ищет всех пациентов с указанным диагнозом"""
        result = []
        for item in self._items:
            if item.diagnosis.lower() == diagnosis.lower():
                result.append(item)
        return result
    
    def find_by_doctor(self, doctor):
        """Ищет всех пациентов у указанного врача"""
        result = []
        for item in self._items:
            if item.doctor.lower() == doctor.lower():
                result.append(item)
        return result
    
    def find_by_status(self, status):
        """Ищет всех пациентов с указанным статусом"""
        result = []
        for item in self._items:
            if item.status.lower() == status.lower():
                result.append(item)
        return result
    
    def __len__(self):
        """Возвращает количество пациентов в коллекции"""
        return len(self._items)
    
    def __iter__(self):
        """Позволяет итерироваться по коллекции (for item in collection)"""
        return iter(self._items)
    
    def __getitem__(self, index):
        """Позволяет обращаться по индексу: collection[0] или collection[1:3]"""
        if isinstance(index, slice):
            new_collection = PatientCollection()
            for item in self._items[index]:
                new_collection.add(item)
            return new_collection
        return self._items[index]
    
    def sort_by_age(self, reverse=False):
        """Сортирует коллекцию по возрасту"""
        self._items.sort(key=lambda x: x.age, reverse=reverse)
    
    def sort_by_name(self, reverse=False):
        """Сортирует коллекцию по имени"""
        self._items.sort(key=lambda x: x.name, reverse=reverse)
    
    def sort(self, key, reverse=False):
        """Универсальная сортировка с пользовательским ключом"""
        self._items.sort(key=key, reverse=reverse)
    
    def get_active(self):
        """Возвращает новую коллекцию с активными пациентами (активен или на лечении)"""
        new_collection = PatientCollection()
        for item in self._items:
            if item.status == "активен" or item.status == "на лечении":
                new_collection.add(item)
        return new_collection
    
    def get_by_age_range(self, min_age, max_age):
        """Возвращает новую коллекцию пациентов в указанном возрастном диапазоне"""
        new_collection = PatientCollection()
        for item in self._items:
            if min_age <= item.age <= max_age:
                new_collection.add(item)
        return new_collection