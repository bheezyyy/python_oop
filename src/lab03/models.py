from base import Patient

class Inpatient(Patient):
    def __init__(self, name, age, diagnosis, doctor=None, doctor_spec="Терапевт",
                 room_number=None, admission_date=None):
        super().__init__(name, age, diagnosis, doctor, doctor_spec, status="на лечении")
        self._room_number = room_number
        self._admission_date = admission_date
    
    @property
    def room_number(self):
        return self._room_number
    
    @property
    def admission_date(self):
        return self._admission_date
    
    def discharge(self):
        result = super().discharge()
        self._add_to_history(f"Выписан из палаты {self._room_number}")
        return f"{result}, палата {self._room_number}"
    
    def calculate_treatment_cost(self):
        days = 10
        return 5000 + (days * 1000)
    
    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, палата: {self._room_number}, поступление: {self._admission_date}"


class Outpatient(Patient):
    def __init__(self, name, age, diagnosis, doctor=None, doctor_spec="Терапевт",
                 visit_date=None, prescription=None):
        super().__init__(name, age, diagnosis, doctor, doctor_spec, status="активен")
        self._visit_date = visit_date
        self._prescription = prescription
    
    @property
    def visit_date(self):
        return self._visit_date
    
    @property
    def prescription(self):
        return self._prescription
    
    def assign_prescription(self, prescription):
        self._prescription = prescription
        self._add_to_history(f"Назначено лечение: {prescription}")
        return f"Пациенту {self._name} назначено: {prescription}"
    
    def calculate_treatment_cost(self):
        return 1500
    
    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, дата визита: {self._visit_date}, назначение: {self._prescription}"