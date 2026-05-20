from app import PatientApp
from exceptions import ItemNotFoundError, DuplicateItemError

def print_separator():
    print("-" * 50)

def print_header(title):
    print_separator()
    print(f"{title:^50}")
    print_separator()

def print_patient(patient):
    print(f"  Имя: {patient.name}")
    print(f"  Возраст: {patient.age}")
    print(f"  Диагноз: {patient.diagnosis}")
    print(f"  Врач: {patient.doctor}")
    print(f"  Статус: {patient.status}")
    print()

def print_patients_table(patients):
    if not patients:
        print("  Нет пациентов")
        return
    print(f"  {'Имя':<25} {'Возраст':<8} {'Диагноз':<15} {'Статус':<12}")
    print(f"  {'-'*25} {'-'*8} {'-'*15} {'-'*12}")
    for p in patients:
        print(f"  {p.name:<25} {p.age:<8} {p.diagnosis:<15} {p.status:<12}")

def show_menu():
    print_header("МЕНЮ")
    print("1. Добавить пациента")
    print("2. Показать всех пациентов")
    print("3. Найти пациента по имени")
    print("4. Найти пациентов по диагнозу")
    print("5. Удалить пациента")
    print("6. Сортировка")
    print("7. Фильтрация")
    print("8. Статистика")
    print("0. Выход")
    print_separator()

def add_patient_flow(app):
    print_header("ДОБАВЛЕНИЕ ПАЦИЕНТА")
    
    name = input("ФИО: ")
    try:
        age = int(input("Возраст: "))
    except ValueError:
        print("Ошибка: возраст должен быть числом")
        return
    
    diagnosis = input("Диагноз: ")
    doctor = input("Лечащий врач (Enter - по умолчанию): ")
    status = input("Статус (активен/на лечении/выписан): ")
    if not status:
        status = "активен"
    
    try:
        patient = app.add_patient(name, age, diagnosis, doctor if doctor else None, status)
        print(f"\nПациент добавлен:")
        print_patient(patient)
    except DuplicateItemError as e:
        print(f"\nОшибка: {e}")

def show_patients(app):
    print_header("ВСЕ ПАЦИЕНТЫ")
    patients = app.get_all_patients()
    print_patients_table(patients)
    print(f"\nВсего: {len(patients)}")

def find_patient_by_name(app):
    print_header("ПОИСК ПО ИМЕНИ")
    name = input("Введите ФИО: ")
    try:
        patient = app.find_by_name(name)
        print_patient(patient)
    except ItemNotFoundError as e:
        print(f"Ошибка: {e}")

def find_by_diagnosis(app):
    print_header("ПОИСК ПО ДИАГНОЗУ")
    diagnosis = input("Введите диагноз: ")
    patients = app.find_by_diagnosis(diagnosis)
    if patients:
        print_patients_table(patients)
    else:
        print("Пациенты с таким диагнозом не найдены")

def remove_patient_flow(app):
    print_header("УДАЛЕНИЕ ПАЦИЕНТА")
    name = input("Введите ФИО пациента для удаления: ")
    try:
        patient = app.remove_patient(name, confirm=False)
        print(f"Найден пациент:")
        print_patient(patient)
        confirm = input(f"Удалить пациента {name}? (y/n): ")
        if confirm.lower() == 'y':
            app.remove_patient(name, confirm=True)
            print("Пациент удален")
        else:
            print("Удаление отменено")
    except ItemNotFoundError as e:
        print(f"Ошибка: {e}")

def sort_menu(app):
    print_header("СОРТИРОВКА")
    print("1. По имени (А-Я)")
    print("2. По имени (Я-А)")
    print("3. По возрасту (молодые-пожилые)")
    print("4. По возрасту (пожилые-молодые)")
    choice = input("Выберите: ")
    if choice == "1":
        patients = app.sort_by_name(reverse=False)
    elif choice == "2":
        patients = app.sort_by_name(reverse=True)
    elif choice == "3":
        patients = app.sort_by_age(reverse=False)
    elif choice == "4":
        patients = app.sort_by_age(reverse=True)
    else:
        print("Неверный выбор")
        return
    print_patients_table(patients)

def filter_menu(app):
    print_header("ФИЛЬТРАЦИЯ")
    print("1. По статусу")
    print("2. По диапазону возраста")
    choice = input("Выберите: ")
    if choice == "1":
        status = input("Введите статус: ")
        patients = app.filter_by_status(status)
    elif choice == "2":
        try:
            min_age = int(input("Мин. возраст: "))
            max_age = int(input("Макс. возраст: "))
            patients = app.filter_by_age_range(min_age, max_age)
        except ValueError:
            print("Ошибка: введите числа")
            return
    else:
        print("Неверный выбор")
        return
    print_patients_table(patients)

def show_statistics(app):
    print_header("СТАТИСТИКА")
    stats = app.get_statistics()
    print(f"Всего пациентов: {stats['total']}")
    print(f"Средний возраст: {stats['avg_age']:.1f}")
    print("Статусы:")
    for status, count in stats['statuses'].items():
        print(f"  {status}: {count}")

def run_cli():
    app = PatientApp()
    while True:
        show_menu()
        choice = input("Выберите пункт: ")
        if choice == "1":
            add_patient_flow(app)
        elif choice == "2":
            show_patients(app)
        elif choice == "3":
            find_patient_by_name(app)
        elif choice == "4":
            find_by_diagnosis(app)
        elif choice == "5":
            remove_patient_flow(app)
        elif choice == "6":
            sort_menu(app)
        elif choice == "7":
            filter_menu(app)
        elif choice == "8":
            show_statistics(app)
        elif choice == "0":
            app.exit()
            print("Данные сохранены. До свидания!")
            break
        else:
            print("Ошибка: неверный пункт меню")
        input("\nНажмите Enter для продолжения...")