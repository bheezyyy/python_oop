from datetime import datetime

MAX_AGE = 150
MIN_AGE = 0
RETIREMENT_AGE = 65
VALID_SPECIALIZATIONS = ["Терапевт", "Хирург", "Кардиолог", "Невролог", "Офтальмолог"]
VALID_STATUSES = ["активен", "на лечении", "выписан", "направлен"]

def validate_name(name):
    if not isinstance(name, str):
        raise TypeError("Имя должно быть строкой")
    if not name.strip():
        raise ValueError("Имя не может быть пустым")
    if len(name.strip()) < 2:
        raise ValueError("Имя должно содержать минимум 2 символа")
    return name.strip()

def validate_age(age):
    if not isinstance(age, (int, float)):
        raise TypeError("Возраст должен быть числом")
    if age < MIN_AGE or age > MAX_AGE:
        raise ValueError(f"Возраст должен быть от {MIN_AGE} до {MAX_AGE}")
    return int(age)

def validate_diagnosis(diagnosis):
    if not isinstance(diagnosis, str):
        raise TypeError("Диагноз должен быть строкой")
    if not diagnosis.strip():
        raise ValueError("Диагноз не может быть пустым")
    if len(diagnosis.strip()) < 3:
        raise ValueError("Диагноз должен содержать минимум 3 символа")
    return diagnosis.strip()

def validate_doctor(doctor):
    if not isinstance(doctor, str):
        raise TypeError("ФИО врача должно быть строкой")
    if not doctor.strip():
        raise ValueError("ФИО врача не может быть пустым")
    if len(doctor.strip()) < 5:
        raise ValueError("ФИО врача должно содержать минимум 5 символов")
    return doctor.strip()

def validate_specialization(spec):
    if not isinstance(spec, str):
        raise TypeError("Специализация должна быть строкой")
    if spec not in VALID_SPECIALIZATIONS:
        raise ValueError(f"Специализация должна быть одной из: {', '.join(VALID_SPECIALIZATIONS)}")
    return spec

def validate_status(status):
    if not isinstance(status, str):
        raise TypeError("Статус должен быть строкой")
    if status not in VALID_STATUSES:
        raise ValueError(f"Статус должен быть одним из: {', '.join(VALID_STATUSES)}")
    return status

def validate_appointment_date(date_str):
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
        if date < datetime.now():
            raise ValueError("Дата приема не может быть в прошлом")
        return date_str
    except ValueError as e:
        if "does not match format" in str(e):
            raise ValueError("Дата должна быть в формате ГГГГ-ММ-ДД")
        raise