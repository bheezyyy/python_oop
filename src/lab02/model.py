class Patient:
    _count = 0
    RETIREMENT_AGE = 65
    DEFAULT_DOCTOR = "Дежурный врач"
    
    def __init__(self, name, age, diagnosis, doctor=None, 
                 doctor_spec="Терапевт", status="активен"):
        self._name = name.strip()
        self._age = age
        self._diagnosis = diagnosis.strip()
        self._doctor = (doctor if doctor else self.DEFAULT_DOCTOR).strip()
        self._doctor_spec = doctor_spec
        self._status = status
        self._appointment_date = None
        self._treatment_history = []
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
    
    @diagnosis.setter
    def diagnosis(self, value):
        self._diagnosis = value
        self._add_to_history(f"Диагноз изменен на: {value}")
    
    @property
    def doctor(self):
        return self._doctor
    
    @doctor.setter
    def doctor(self, value):
        self._doctor = value
        self._add_to_history(f"Врач изменен на: {value}")
    
    @property
    def doctor_spec(self):
        return self._doctor_spec
    
    @doctor_spec.setter
    def doctor_spec(self, value):
        old_spec = self._doctor_spec
        self._doctor_spec = value
        self._add_to_history(f"Специализация изменена: {old_spec} -> {value}")
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, value):
        old_status = self._status
        self._status = value
        self._add_to_history(f"Статус изменен: {old_status} -> {value}")
    
    @property
    def appointment_date(self):
        return self._appointment_date
    
    @appointment_date.setter
    def appointment_date(self, value):
        self._appointment_date = value
        if value:
            self._add_to_history(f"Назначен прием на: {value}")
    
    def __str__(self):
        return f"Пациент: {self._name}, {self._age} лет, {self._diagnosis}"
    
    def __repr__(self):
        return f"Patient(name='{self._name}', age={self._age}, diagnosis='{self._diagnosis}')"
    
    def __eq__(self, other):
        if not isinstance(other, Patient):
            return False
        return self._name == other._name and self._age == other._age
    
    def __lt__(self, other):
        return self._age < other._age
    
    @classmethod
    def get_count(cls):
        return cls._count
    
    def _add_to_history(self, event):
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        self._treatment_history.append(f"[{timestamp}] {event}")
    
    def years_to_retirement(self):
        if self._age >= self.RETIREMENT_AGE:
            return 0
        return self.RETIREMENT_AGE - self._age
    
    def assign_appointment(self, date_str):
        self.appointment_date = date_str
        return f"Пациенту {self._name} назначен прием на {date_str}"
    
    def discharge(self):
        self.status = "выписан"
        self._add_to_history("Пациент выписан")
        return f"Пациент {self._name} выписан"
    
    def get_history(self):
        if not self._treatment_history:
            return "История лечения пуста"
        return "\n".join(self._treatment_history)