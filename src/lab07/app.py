from models import Patient
from collection import PatientCollection
from strategies import by_name, by_age
from exceptions import ItemNotFoundError, DuplicateItemError
import storage

class PatientApp:
    def __init__(self, storage_file: str = "data.json"):
        self.collection = PatientCollection()
        self.storage_file = storage_file
        self._load_data()
    
    def _load_data(self):
        patients = storage.load(self.storage_file)
        for p in patients:
            self.collection.add(p)
    
    def _save_data(self):
        storage.save(self.collection.get_all(), self.storage_file)
    
    def add_patient(self, name, age, diagnosis, doctor=None, status="активен"):
        existing = self.collection.find_by_name(name)
        if existing:
            raise DuplicateItemError(f"Пациент с именем {name} уже существует")
        patient = Patient(name, age, diagnosis, doctor, "Терапевт", status)
        self.collection.add(patient)
        self._save_data()
        return patient
    
    def get_all_patients(self):
        return self.collection.get_all()
    
    def find_by_name(self, name):
        result = self.collection.find_by_name(name)
        if not result:
            raise ItemNotFoundError(f"Пациент с именем {name} не найден")
        return result
    
    def find_by_diagnosis(self, diagnosis):
        return self.collection.find_by_diagnosis(diagnosis)
    
    def remove_patient(self, name, confirm=False):
        patient = self.find_by_name(name)
        if not confirm:
            return patient
        self.collection.remove(patient)
        self._save_data()
        return patient
    
    def sort_by_name(self, reverse=False):
        patients = self.collection.get_all()
        patients.sort(key=by_name, reverse=reverse)
        return patients
    
    def sort_by_age(self, reverse=False):
        patients = self.collection.get_all()
        patients.sort(key=by_age, reverse=reverse)
        return patients
    
    def filter_by_status(self, status):
        return [p for p in self.collection.get_all() if p.status == status]
    
    def filter_by_age_range(self, min_age, max_age):
        return [p for p in self.collection.get_all() if min_age <= p.age <= max_age]
    
    def get_statistics(self):
        patients = self.collection.get_all()
        if not patients:
            return {"total": 0, "avg_age": 0, "statuses": {}}
        ages = [p.age for p in patients]
        statuses = {}
        for p in patients:
            statuses[p.status] = statuses.get(p.status, 0) + 1
        return {
            "total": len(patients),
            "avg_age": sum(ages) / len(ages),
            "statuses": statuses
        }
    
    def exit(self):
        self._save_data()