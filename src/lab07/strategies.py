def by_name(item):
    return item.name

def by_age(item):
    return item.age

def is_active(item):
    return item.status == "активен"

def has_diagnosis(diagnosis):
    def filter_fn(item):
        return item.diagnosis.lower() == diagnosis.lower()
    return filter_fn