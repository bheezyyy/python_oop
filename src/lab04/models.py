from interfaces import Printable, Serializable, AgeComparable

class Patient(Printable, Serializable, AgeComparable):
    _count = 0
    
    def __init__(self, name, age, diagnosis, doctor=None, status="активен"):
        self._name = name.strip()
        self._age = age
        self._diagnosis = diagnosis.strip()
        self._doctor = doctor.strip() if doctor else "Дежурный врач"
        self._status = status
    
    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    def get_printable_info(self) -> str:
        return f"{self._name}, {self._age} лет, {self._diagnosis}, врач: {self._doctor}"
    
    def to_dict(self) -> dict:
        return {"name": self._name, "age": self._age, "diagnosis": self._diagnosis, "doctor": self._doctor}
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(data["name"], data["age"], data["diagnosis"], data.get("doctor"))
    
    def compare_age(self, other) -> int:
        if self._age < other._age:
            return -1
        elif self._age > other._age:
            return 1
        return 0


class PatientCollection(Printable, Serializable):
    def __init__(self):
        self._items = []
    
    def add(self, item):
        if not isinstance(item, Patient):
            raise TypeError("Только Patient")
        self._items.append(item)
    
    def get_all(self):
        return self._items.copy()
    
    def get_printable_info(self) -> str:
        lines = [f"Всего: {len(self._items)}"]
        for item in self._items:
            lines.append(f"  - {item.get_printable_info()}")
        return "\n".join(lines)
    
    def to_dict(self) -> dict:
        return {"patients": [item.to_dict() for item in self._items]}
    
    @classmethod
    def from_dict(cls, data: dict):
        collection = cls()
        for p in data.get("patients", []):
            collection.add(Patient.from_dict(p))
        return collection
    
    def __len__(self):
        return len(self._items)
    
    def __iter__(self):
        return iter(self._items)