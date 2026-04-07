

from model import Patient
from collection import PatientCollection

def main():
    print("=" * 60)
    print("ЛАБОРАТОРНАЯ РАБОТА 2 - КОЛЛЕКЦИЯ PATIENT")
    print("=" * 60)
    
    # СЦЕНАРИЙ 1: Создание и добавление
    print("\n[СЦЕНАРИЙ 1] Создание коллекции и добавление пациентов")
    print("-" * 40)
    
    collection = PatientCollection()
    
    p1 = Patient("Иванов Иван", 45, "Гипертония", "Петров П.П.", "Кардиолог")
    p2 = Patient("Петрова Анна", 30, "Грипп", "Сидорова А.А.", "Терапевт")
    p3 = Patient("Сидоров Петр", 25, "Ангина", "Иванов И.И.", "Лор")
    p4 = Patient("Козлова Елена", 55, "Гипертония", "Петров П.П.", "Кардиолог")
    
    collection.add(p1)
    collection.add(p2)
    collection.add(p3)
    collection.add(p4)
    
    print(f"Добавлено пациентов: {len(collection)}")
    
    # Проверка на дубликат
    try:
        duplicate = Patient("Иванов Иван", 50, "Грипп", "Врач", "Терапевт")
        collection.add(duplicate)
    except ValueError as e:
        print(f"Ошибка (дубликат): {e}")
    
    # СЦЕНАРИЙ 2: Вывод всех элементов
    print("\n[СЦЕНАРИЙ 2] Вывод всех пациентов")
    print("-" * 40)
    for patient in collection:
        print(f"{patient.name}, {patient.age} лет, {patient.diagnosis}")
    
    # СЦЕНАРИЙ 3: Поиск
    print("\n[СЦЕНАРИЙ 3] Поиск пациентов")
    print("-" * 40)
    
    found = collection.find_by_name("Петрова Анна")
    print(f"Поиск по имени 'Петрова Анна': {found.name if found else 'Не найден'}")
    
    found_list = collection.find_by_diagnosis("Гипертония")
    print(f"Поиск по диагнозу 'Гипертония': {len(found_list)} пациентов")
    
    # СЦЕНАРИЙ 4: len() и итерация
    print("\n[СЦЕНАРИЙ 4] Демонстрация len() и for")
    print("-" * 40)
    print(f"Всего пациентов: {len(collection)}")
    
    # СЦЕНАРИЙ 5: Индексация
    print("\n[СЦЕНАРИЙ 5] Индексация коллекции")
    print("-" * 40)
    print(f"Первый пациент: {collection[0].name}")
    print(f"Третий пациент: {collection[2].name}")
    
    # СЦЕНАРИЙ 6: Удаление
    print("\n[СЦЕНАРИЙ 6] Удаление пациента")
    print("-" * 40)
    removed = collection.remove_at(1)
    print(f"Удален: {removed.name}")
    print(f"Осталось пациентов: {len(collection)}")
    
    # СЦЕНАРИЙ 7: Сортировка
    print("\n[СЦЕНАРИЙ 7] Сортировка по возрасту")
    print("-" * 40)
    collection.sort_by_age()
    for patient in collection:
        print(f"{patient.name}: {patient.age} лет")
    
    # СЦЕНАРИЙ 8: Фильтрация
    print("\n[СЦЕНАРИЙ 8] Фильтрация (активные пациенты)")
    print("-" * 40)
    active = collection.get_active()
    for patient in active:
        print(f"{patient.name} - статус: {patient.status}")
    
    print("\n[СЦЕНАРИЙ 9] Фильтрация по возрасту (30-50 лет)")
    print("-" * 40)
    age_filtered = collection.get_by_age_range(30, 50)
    for patient in age_filtered:
        print(f"{patient.name}: {patient.age} лет")

if __name__ == "__main__":
    main()