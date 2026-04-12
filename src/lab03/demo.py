from base import Patient
from models import Inpatient, Outpatient
from collection import PatientCollection

def main():
    print("=" * 60)
    print("ЛАБОРАТОРНАЯ РАБОТА 3 - НАСЛЕДОВАНИЕ")
    print("=" * 60)
    
    # СЦЕНАРИЙ 1: Создание и полиморфизм
    print("\n[СЦЕНАРИЙ 1] Создание объектов и полиморфизм")
    print("-" * 40)
    
    p1 = Patient("Иванов Иван", 40, "Осмотр", "Петров П.П.")
    p2 = Inpatient("Петров Петр", 55, "Пневмония", "Сидоров А.А.",
                   room_number="101", admission_date="2026-03-15")
    p3 = Outpatient("Сидорова Анна", 30, "Грипп", "Иванова И.И.",
                    visit_date="2026-03-20", prescription="Тамифлю")
    
    print(p1)
    print(p2)
    print(p3)
    
    # Демонстрация полиморфизма - один метод, разное поведение
    print("\nПолиморфизм метода calculate_treatment_cost():")
    for p in [p1, p2, p3]:
        print(f"  {p.name}: {p.calculate_treatment_cost()} руб.")
    
    # СЦЕНАРИЙ 2: Коллекция с разными типами
    print("\n[СЦЕНАРИЙ 2] Коллекция объектов разных типов")
    print("-" * 40)
    
    collection = PatientCollection()
    collection.add(p1)
    collection.add(p2)
    collection.add(p3)
    
    print(f"Всего пациентов: {len(collection)}")
    for p in collection:
        print(f"  {p.name} - {type(p).__name__}")
    
    # СЦЕНАРИЙ 3: Фильтрация по типу
    print("\n[СЦЕНАРИЙ 3] Фильтрация коллекции по типу")
    print("-" * 40)
    
    inpatients = collection.get_inpatients()
    outpatients = collection.get_outpatients()
    
    print(f"Стационарных: {len(inpatients)}")
    print(f"Амбулаторных: {len(outpatients)}")
    print(f"Общая стоимость лечения: {collection.calculate_total_cost()} руб.")

if __name__ == "__main__":
    main()