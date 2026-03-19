from model import Patient
from datetime import datetime, timedelta

def main():
    print("=" * 60)
    print("ЛАБОРАТОРНАЯ РАБОТА 1 - КЛАСС PATIENT")
    print("=" * 60)
    
    # Сценарий 1: Создание и базовые операции
    print("\n[СЦЕНАРИЙ 1] Создание пациентов и базовые методы")
    print("-" * 40)
    
    p1 = Patient("Иванов Иван Иванович", 45, "Гипертония", "Петров П.П.", "Кардиолог")
    p2 = Patient("Петрова Анна Сергеевна", 67, "Артрит", "Сидорова А.А.", "Терапевт")
    p3 = Patient("Сидоров Петр", 30, "Грипп")
    
    print("Создано пациентов:")
    print(p1)
    print()
    print(p2)
    print()
    print(p3)
    print(f"\nВсего пациентов: {Patient.get_count()}")
    
    # Сценарий 2: Сравнение и сортировка
    print("\n[СЦЕНАРИЙ 2] Сравнение и сортировка")
    print("-" * 40)
    
    p4 = Patient("Иванов Иван Иванович", 45, "Ангина", "Петров П.П.")
    print(f"p1 == p4: {p1 == p4} (одинаковые ФИО и возраст)")
    
    patients = [p1, p2, p3]
    patients.sort()
    print("\nПациенты после сортировки по возрасту:")
    for p in patients:
        print(f"  {p.name}: {p.age} лет")
    
    # Сценарий 3: Изменение свойств через сеттеры
    print("\n[СЦЕНАРИЙ 3] Изменение свойств с валидацией")
    print("-" * 40)
    
    print(f"Текущий диагноз p1: {p1.diagnosis}")
    p1.diagnosis = "Гипертония 2 степени"
    print(f"Новый диагноз: {p1.diagnosis}")
    
    try:
        p1.doctor_spec = "Стоматолог"
    except ValueError as e:
        print(f"Ошибка при смене специализации: {e}")
    
    # Сценарий 4: Работа со статусом
    print("\n[СЦЕНАРИЙ 4] Изменение статуса пациента")
    print("-" * 40)
    
    print(f"Статус p2: {p2.status}")
    p2.status = "на лечении"
    print(f"Новый статус: {p2.status}")
    
    # Сценарий 5: Назначение приема
    print("\n[СЦЕНАРИЙ 5] Назначение даты приема")
    print("-" * 40)
    
    future_date = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
    print(p1.assign_appointment(future_date))
    
    try:
        past_date = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
        p2.assign_appointment(past_date)
    except ValueError as e:
        print(f"Ошибка при назначении даты в прошлом: {e}")
    
    # Сценарий 6: Выписка пациента
    print("\n[СЦЕНАРИЙ 6] Выписка пациента")
    print("-" * 40)
    
    print(p2.discharge())
    
    try:
        p2.discharge()
    except ValueError as e:
        print(f"Ошибка при повторной выписке: {e}")
    
    # Сценарий 7: История лечения
    print("\n[СЦЕНАРИЙ 7] История лечения")
    print("-" * 40)
    
    print("История пациента p1:")
    print(p1.get_history())
    
    # Сценарий 8: Демонстрация __repr__
    print("\n[СЦЕНАРИЙ 8] Представление для разработчиков")
    print("-" * 40)
    
    print(repr(p1))
    
    # Сценарий 9: Альтернативный конструктор
    print("\n[СЦЕНАРИЙ 9] Создание из строки")
    print("-" * 40)
    
    p5 = Patient.from_string("Козлова Елена, 28, Ангина, Смирнова Е.Е.")
    print(p5)
    
    # Сценарий 10: Проверка валидации
    print("\n[СЦЕНАРИЙ 10] Проверка валидации")
    print("-" * 40)
    
    test_cases = [
        ("", 30, "Грипп", None, "Пустое имя"),
        ("Иван", -5, "Грипп", None, "Отрицательный возраст"),
        ("Иван", 200, "Грипп", None, "Слишком большой возраст"),
        ("Иван", 30, "", None, "Пустой диагноз"),
        ("Иван", 30, "Грипп", "Ив", "Короткое имя врача"),
    ]
    
    for name, age, diag, doctor, desc in test_cases:
        try:
            Patient(name, age, diag, doctor)
            print(f"  {desc}: НЕ пройдена (должна быть ошибка)")
        except (ValueError, TypeError) as e:
            print(f"  {desc}: пройден - {e}")
    
    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")
    print("=" * 60)

if __name__ == "__main__":
    main()