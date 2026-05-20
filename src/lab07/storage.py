import json
import os
from models import Patient

def save(patients, filepath: str) -> None:
    data = [p.to_dict() for p in patients]
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load(filepath: str):
    if not os.path.exists(filepath):
        return []
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return [Patient.from_dict(item) for item in data]