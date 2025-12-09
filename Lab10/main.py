import json

# --- Инициализация данных ---
students = []

# --- Ввод данных пользователем ---
print("--- Ввод данных ---")
try:
    n = int(input("Введите количество студентов: "))
except ValueError:
    print("Ошибка: Введено неверное количество студентов. Установлено 0.")
    n = 0

for i in range(n):
    print(f"\n--- Студент {i + 1} ---")
    name = input("Имя студента: ")
    group = input("Группа: ")

    gpa_valid = False
    while not gpa_valid:
        try:
            gpa = float(input("Средний балл (GPA): "))
            if 0.0 <= gpa <= 5.0:
                gpa_valid = True
            else:
                print("GPA должен быть в диапазоне от 0.0 до 5.0")
        except ValueError:
            print("Ошибка: Введите GPA как число (например, 3.75).")

    # Добавляем данные в список
    students.append({"name": name, "group": group, "gpa": gpa})

# --- Сохранение в текстовый файл (students.txt) ---
print("\n--- Сохранение в students.txt ---")
try:
    with open("students.txt", "w", encoding="utf-8") as f:
        for s in students:
            # Используем разделитель '|' для простоты чтения
            f.write(f"{s['name']} | {s['group']} | {s['gpa']}\n")
    print("Данные успешно сохранены в students.txt.")
except IOError:
    print("Ошибка: Не удалось записать данные в students.txt.")

# --- Чтение и вывод данных из students.txt ---
print("\n--- Чтение из students.txt ---")
try:
    with open("students.txt", "r", encoding="utf-8") as f:
        print("Данные из файла students.txt:")
        for line in f:
            print(line.strip())
except FileNotFoundError:
    print("Ошибка: Файл students.txt не найден.")

# --- Сериализация в JSON (students.json) ---
print("\n--- Сериализация в students.json ---")
try:
    with open("students.json", "w", encoding="utf-8") as jf:
        # Сериализация списка словарей в JSON с форматированием (indent=4)
        json.dump(students, jf, ensure_ascii=False, indent=4)
    print("Данные успешно сериализованы в students.json.")
except IOError:
    print("Ошибка: Не удалось записать данные в students.json.")

# --- Фильтрация по GPA ---
print("\n--- Фильтрация данных ---")
if students:
    try:
        threshold = float(input("Введите минимальный GPA для фильтрации: "))

        # Фильтрация списка с помощью генератора списков
        filtered = [s for s in students if s["gpa"] >= threshold]

        print("\nСтуденты с GPA выше порога:")
        if filtered:
            # Добавляем сортировку по GPA как вариант усложнения
            filtered.sort(key=lambda s: s['gpa'], reverse=True)
            for s in filtered:
                print(f"{s['name']} ({s['group']}) — GPA: {s['gpa']}")
        else:
            print("Студентов, соответствующих порогу, не найдено.")

    except ValueError:
        print("Ошибка фильтрации: Введите порог GPA как число.")
else:
    print("Список студентов пуст, фильтрация невозможна.")