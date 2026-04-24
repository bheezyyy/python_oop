from models import Patient, PatientCollection
from interfaces import Printable, Serializable, AgeComparable

def print_all(items):
    for item in items:
        print(item.get_printable_info())
    print()

def main():
    print("=" * 60)
    print("ЛАБОРАТОРНАЯ РАБОТА 4 - ИНТЕРФЕЙСЫ И АБСТРАКТНЫЕ КЛАССЫ")
    print("=" * 60)
    
    # СЦЕНАРИЙ 1: Создание объектов и проверка интерфейсов
    print("\n[СЦЕНАРИЙ 1] Проверка реализации интерфейсов")
    print("-" * 40)
    
    p1 = Patient("Иванов Иван", 45, "Гипертония", "Петров П.П.")
    p2 = Patient("Петрова Анна", 30, "Грипп", "Сидорова А.А.")
    p3 = Patient("Сидоров Петр", 25, "Ангина", "Иванов И.И.")
    
    collection = PatientCollection()
    collection.add(p1)
    collection.add(p2)
    collection.add(p3)
    
    print(f"Patient implements Printable: {isinstance(p1, Printable)}")
    print(f"Patient implements Serializable: {isinstance(p1, Serializable)}")
    print(f"Patient implements AgeComparable: {isinstance(p1, AgeComparable)}")
    print(f"PatientCollection implements Printable: {isinstance(collection, Printable)}")
    print(f"PatientCollection implements Serializable: {isinstance(collection, Serializable)}")
    
    # СЦЕНАРИЙ 2: Работа через интерфейсы (полиморфизм)
    print("\n[СЦЕНАРИЙ 2] Полиморфизм через единый интерфейс")
    print("-" * 40)
    
    printable_items = [p1, p2, collection]
    for item in printable_items:
        print(item.get_printable_info())
    
    # СЦЕНАРИЙ 3: Сериализация и AgeComparable
    print("\n[СЦЕНАРИЙ 3] Сериализация и сравнение по возрасту")
    print("-" * 40)
    
    p1_dict = p1.to_dict()
    print(f"Сериализация: {p1_dict}")
    
    p1_restored = Patient.from_dict(p1_dict)
    print(f"Восстановлен: {p1_restored.get_printable_info()}")
    
    print(f"Сравнение возрастов ({p1.name} 45 лет, {p2.name} 30 лет): {p1.compare_age(p2)}")

if __name__ == "__main__":
    main()