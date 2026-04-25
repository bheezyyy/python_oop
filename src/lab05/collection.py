class PatientCollection:
    def __init__(self):
        self._items = []
    
    def add(self, item):
        self._items.append(item)
    
    def get_all(self):
        return self._items.copy()
    
    def sort_by(self, key_func, reverse=False):
        self._items.sort(key=key_func, reverse=reverse)
        return self
    
    def filter_by(self, predicate):
        self._items = list(filter(predicate, self._items))
        return self
    
    def apply(self, func):
        self._items = list(map(func, self._items))
        return self
    
    def __len__(self):
        return len(self._items)
    
    def __iter__(self):
        return iter(self._items)
    
    def __getitem__(self, index):
        return self._items[index]