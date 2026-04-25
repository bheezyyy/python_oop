# demo.py

from models import Patient
from collection import PatientCollection
from strategies import by_name, by_age, is_active, has_diagnosis, StatusUpdateStrategy

def main():
    print("=" * 60)
    print("ЛАБОРАТОРНАЯ РАБОТА 5 - ФУНКЦИИ КАК АРГУМЕНТЫ")
    print("=" * 60)
    
    # СЦЕНАРИЙ 1: Сортировка разными стратегиями
    print("\n[СЦЕНАРИЙ 1] Сортировка разными стратегиями")
    print("-" * 40)
    
    collection = PatientCollection()
    patients_data = [
        ("Иванов Иван", 45, "Гипертония"),
        ("Петрова Анна", 30, "Грипп"),
        ("Сидоров Петр", 25, "Ангина"),
        ("Козлова Елена", 70, "Гипертония"),
        ("Смирнов Дмитрий", 55, "Диабет"),
    ]
    
    for name, age, diag in patients_data:
        collection.add(Patient(name, age, diag))
    
    print("Сортировка по имени:")
    collection.sort_by(by_name)
    for p in collection:
        print(f"  {p.name}")
    
    print("\nСортировка по возрасту:")
    collection.sort_by(by_age)
    for p in collection:
        print(f"  {p.name}: {p.age} лет")
    
    print("\nСортировка через lambda по имени:")
    collection.sort_by(lambda x: x.name)
    for p in collection:
        print(f"  {p.name}")
    
    # СЦЕНАРИЙ 2: Фильтрация коллекции
    print("\n[СЦЕНАРИЙ 2] Фильтрация коллекции")
    print("-" * 40)
    
    collection = PatientCollection()
    patients_full = [
        ("Иванов Иван", 45, "Гипертония", "Петров П.П.", "активен"),
        ("Петрова Анна", 30, "Грипп", "Сидорова А.А.", "активен"),
        ("Сидоров Петр", 25, "Ангина", "Иванов И.И.", "на лечении"),
        ("Козлова Елена", 70, "Гипертония", "Петров П.П.", "активен"),
    ]
    
    for name, age, diag, doctor, status in patients_full:
        collection.add(Patient(name, age, diag, doctor, status))
    
    print("Фильтр: только активные пациенты")
    active = list(filter(is_active, collection.get_all()))
    for p in active:
        print(f"  {p.name} - {p.status}")
    
    print("\nФильтр через фабрику (диагноз 'Гипертония'):")
    hyper_filter = has_diagnosis("Гипертония")
    for p in collection.get_all():
        if hyper_filter(p):
            print(f"  {p.name} - {p.diagnosis}")
    
    # СЦЕНАРИЙ 3: Паттерн Стратегия (callable-объект)
    print("\n[СЦЕНАРИЙ 3] Паттерн Стратегия (callable-объект)")
    print("-" * 40)
    
    print("Статус пациентов до применения стратегии:")
    for p in collection.get_all():
        print(f"  {p.name} - {p.status}")
    
    strategy = StatusUpdateStrategy("на лечении")
    for p in collection.get_all():
        strategy(p)
    
    print("\nСтатус пациентов после применения стратегии:")
    for p in collection.get_all():
        print(f"  {p.name} - {p.status}")

if __name__ == "__main__":
    main()