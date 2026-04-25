# strategies.py

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

class StatusUpdateStrategy:
    def __init__(self, new_status):
        self.new_status = new_status
    def __call__(self, item):
        item.status = self.new_status
        return item