# models.py

class Patient:
    _count = 0
    
    def __init__(self, name, age, diagnosis, doctor=None, status="активен"):
        self._name = name.strip()
        self._age = age
        self._diagnosis = diagnosis.strip()
        self._doctor = doctor.strip() if doctor else "Дежурный врач"
        self._status = status
        Patient._count += 1
    
    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    @property
    def diagnosis(self):
        return self._diagnosis
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, value):
        self._status = value
    
    def to_dict(self):
        return {
            "name": self._name,
            "age": self._age,
            "diagnosis": self._diagnosis,
            "doctor": self._doctor,
            "status": self._status
        }
    
    def __str__(self):
        return f"{self._name}, {self._age} лет"