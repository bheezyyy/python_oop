import validate

class Patient:
    _count = 0
    RETIREMENT_AGE = 65
    DEFAULT_DOCTOR = "Дежурный врач"
    
    def __init__(self, name, age, diagnosis, doctor=None, 
                 doctor_spec="Терапевт", status="активен"):
        self._validate_all(name, age, diagnosis, doctor, doctor_spec, status)
        
        self._name = validate.validate_name(name)
        self._age = validate.validate_age(age)
        self._diagnosis = validate.validate_diagnosis(diagnosis)
        self._doctor = validate.validate_doctor(doctor if doctor else self.DEFAULT_DOCTOR)
        self._doctor_spec = validate.validate_specialization(doctor_spec)
        self._status = validate.validate_status(status)
        self._appointment_date = None
        self._treatment_history = []
        
        Patient._count += 1
    
    def _validate_all(self, name, age, diagnosis, doctor, doctor_spec, status):
        validate.validate_name(name)
        validate.validate_age(age)
        validate.validate_diagnosis(diagnosis)
        if doctor:
            validate.validate_doctor(doctor)
        validate.validate_specialization(doctor_spec)
        validate.validate_status(status)
    
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
        self._diagnosis = validate.validate_diagnosis(value)
        self._add_to_history(f"Диагноз изменен на: {value}")
    
    @property
    def doctor(self):
        return self._doctor
    
    @doctor.setter
    def doctor(self, value):
        self._doctor = validate.validate_doctor(value)
        self._add_to_history(f"Врач изменен на: {value}")
    
    @property
    def doctor_spec(self):
        return self._doctor_spec
    
    @doctor_spec.setter
    def doctor_spec(self, value):
        old_spec = self._doctor_spec
        self._doctor_spec = validate.validate_specialization(value)
        self._add_to_history(f"Специализация изменена: {old_spec} -> {value}")
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, value):
        old_status = self._status
        new_status = validate.validate_status(value)
        
        if old_status == "выписан":
            raise ValueError("Нельзя изменить статус выписанного пациента")
        
        self._status = new_status
        self._add_to_history(f"Статус изменен: {old_status} -> {new_status}")
    
    @property
    def appointment_date(self):
        return self._appointment_date
    
    @appointment_date.setter
    def appointment_date(self, value):
        if value is None:
            self._appointment_date = None
        else:
            self._appointment_date = validate.validate_appointment_date(value)
            self._add_to_history(f"Назначен прием на: {value}")
    
    def __str__(self):
        return (
            f"Пациент: {self._name}\n"
            f"Возраст: {self._age} лет\n"
            f"Диагноз: {self._diagnosis}\n"
            f"Врач: {self._doctor} ({self._doctor_spec})\n"
            f"Статус: {self._status}"
        )
    
    def __repr__(self):
        return (f"Patient(name='{self._name}', age={self._age}, "
                f"diagnosis='{self._diagnosis}', doctor='{self._doctor}', "
                f"status='{self._status}')")
    
    def __eq__(self, other):
        if not isinstance(other, Patient):
            return False
        return (self._name == other._name and 
                self._age == other._age)
    
    def __lt__(self, other):
        if not isinstance(other, Patient):
            return NotImplemented
        return self._age < other._age
    
    @classmethod
    def get_count(cls):
        return cls._count
    
    @classmethod
    def from_string(cls, data_string):
        parts = data_string.split(',')
        if len(parts) < 3:
            raise ValueError("Строка должна содержать минимум 3 части")
        
        name = parts[0].strip()
        age = int(parts[1].strip())
        diagnosis = parts[2].strip()
        doctor = parts[3].strip() if len(parts) > 3 else None
        
        return cls(name, age, diagnosis, doctor)
    
    def _add_to_history(self, event):
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        self._treatment_history.append(f"[{timestamp}] {event}")
    
    def years_to_retirement(self):
        if self._age >= self.RETIREMENT_AGE:
            return 0
        return self.RETIREMENT_AGE - self._age
    
    def is_senior(self):
        return self._age >= 60
    
    def assign_appointment(self, date_str):
        self.appointment_date = date_str
        return f"Пациенту {self._name} назначен прием на {date_str}"
    
    def discharge(self):
        if self._status == "выписан":
            raise ValueError("Пациент уже выписан")
        
        self.status = "выписан"
        self._add_to_history("Пациент выписан")
        return f"Пациент {self._name} выписан"
    
    def get_history(self):
        if not self._treatment_history:
            return "История лечения пуста"
        return "\n".join(self._treatment_history)