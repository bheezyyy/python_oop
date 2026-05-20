class PatientCollection:
    def __init__(self):
        self._items = []
    
    def add(self, item):
        self._items.append(item)
    
    def remove(self, item):
        if item not in self._items:
            raise ValueError("Объект не найден")
        self._items.remove(item)
    
    def get_all(self):
        return self._items.copy()
    
    def find_by_name(self, name: str):
        for item in self._items:
            if item.name.lower() == name.lower():
                return item
        return None
    
    def find_by_diagnosis(self, diagnosis: str):
        return [item for item in self._items if item.diagnosis.lower() == diagnosis.lower()]
    
    def sort_by(self, key_func, reverse=False):
        self._items.sort(key=key_func, reverse=reverse)
        return self
    
    def __len__(self):
        return len(self._items)
    
    def __iter__(self):
        return iter(self._items)
    
    def __getitem__(self, index):
        return self._items[index]