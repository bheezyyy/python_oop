def validate_name(name):
    if not name or not name.strip():
        return "Неизвестный"
    return name.strip()

def validate_age(age):
    try:
        age = int(age)
        if age < 0 or age > 150:
            return 0
        return age
    except:
        return 0

def validate_diagnosis(diagnosis):
    if not diagnosis or not diagnosis.strip():
        return "Без диагноза"
    return diagnosis.strip()

def validate_doctor(doctor):
    if not doctor or not doctor.strip():
        return "Дежурный врач"
    return doctor.strip()

def validate_specialization(spec):
    valid = ["Терапевт", "Хирург", "Кардиолог", "Невролог", "Офтальмолог"]
    if spec not in valid:
        return "Терапевт"
    return spec

def validate_status(status):
    valid = ["активен", "на лечении", "выписан", "направлен"]
    if status not in valid:
        return "активен"
    return status

def validate_appointment_date(date_str):
    return date_str