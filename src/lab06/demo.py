from model import Patient
from container import TypedCollection

def main():
    print("=" * 60)
    print("ЛАБОРАТОРНАЯ РАБОТА 6 - GENERICS И TYPING")
    print("=" * 60)
    
    # СЦЕНАРИЙ 1: Создание Generic коллекции и добавление объектов
    print("\n[СЦЕНАРИЙ 1] Создание TypedCollection и добавление пациентов")
    print("-" * 40)
    
    p1 = Patient("Иванов Иван", 45, "Гипертония", "Петров П.П.")
    p2 = Patient("Петрова Анна", 30, "Грипп", "Сидорова А.А.")
    p3 = Patient("Сидоров Петр", 25, "Ангина", "Иванов И.И.")
    
    collection = TypedCollection[Patient]()
    collection.add(p1)
    collection.add(p2)
    collection.add(p3)
    
    print(f"Размер коллекции: {len(collection)}")
    print("Все пациенты:")
    for item in collection:
        print(f"  {item.name}, {item.age} лет, {item.diagnosis}")
    
    # СЦЕНАРИЙ 2: find и filter
    print("\n[СЦЕНАРИЙ 2] Поиск find() и фильтрация filter()")
    print("-" * 40)
    
    found = collection.find(lambda p: p.name == "Петрова Анна")
    print(f"find('Петрова Анна'): {found.name if found else 'Не найден'}")
    
    not_found = collection.find(lambda p: p.name == "Неизвестный")
    print(f"find('Неизвестный'): {not_found if not_found else 'None'}")
    
    filtered = collection.filter(lambda p: p.age < 40)
    print(f"filter(возраст < 40): {len(filtered)} пациента")
    for p in filtered:
        print(f"  {p.name} - {p.age} лет")
    
    # СЦЕНАРИЙ 3: map с изменением типа
    print("\n[СЦЕНАРИЙ 3] map() с разными типами результата")
    print("-" * 40)
    
    names = collection.map(lambda p: p.name)
    print(f"map (имена) -> list[str]: {names}")
    
    ages = collection.map(lambda p: p.age)
    print(f"map (возраст) -> list[int]: {ages}")
    
    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")
    print("=" * 60)

if __name__ == "__main__":
    main()