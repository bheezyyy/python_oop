import validate

class Patient:
    _count = 0
    RETIREMENT_AGE = 65
    DEFAULT_DOCTOR = "Дежурный врач"
    
    def __init__(self, name, age, diagnosis, doctor=None, 
                 doctor_spec="Терапевт", status="активен"):
        self._name = validate.validate_name(name)
        self._age = validate.validate_age(age)
        self._diagnosis = validate.validate_diagnosis(diagnosis)
        self._doctor = validate.validate_doctor(doctor if doctor else self.DEFAULT_DOCTOR)
        self._doctor_spec = validate.validate_specialization(doctor_spec)
        self._status = validate.validate_status(status)
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
        self._diagnosis = validate.validate_diagnosis(value)
    
    @property
    def doctor(self):
        return self._doctor
    
    @doctor.setter
    def doctor(self, value):
        self._doctor = validate.validate_doctor(value)
    
    @property
    def doctor_spec(self):
        return self._doctor_spec
    
    @doctor_spec.setter
    def doctor_spec(self, value):
        self._doctor_spec = validate.validate_specialization(value)
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, value):
        self._status = validate.validate_status(value)
    
    @property
    def appointment_date(self):
        return self._appointment_date
    
    def to_dict(self):
        return {
            "name": self._name,
            "age": self._age,
            "diagnosis": self._diagnosis,
            "doctor": self._doctor,
            "doctor_spec": self._doctor_spec,
            "status": self._status
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["age"],
            data["diagnosis"],
            data.get("doctor"),
            data.get("doctor_spec", "Терапевт"),
            data.get("status", "активен")
        )
    
    def get_printable_info(self):
        return f"{self._name}, {self._age} лет, {self._diagnosis}"
    
    def __str__(self):
        return f"{self._name}, {self._age} лет, {self._diagnosis}"