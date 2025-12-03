import json
import os  # Импортируем для работы с файлами


class Student:
    """Класс для представления студента с инкапсулированными атрибутами."""

    # 1. Метод инициализации
    def __init__(self, name: str, group: str, gpa: float):
        # Использование префикса __ (двойное подчеркивание) для инкапсуляции.
        # Эти поля являются "приватными" и доступны только через методы класса.
        self.__name = name
        self.__group = group
        self.__gpa = gpa

    # 2. Метод вывода информации
    def display_info(self):
        """Выводит информацию о студенте."""
        print(f"| Имя: {self.__name:<15} | Группа: {self.__group:<8} | GPA: {self.__gpa:.2f}")

    # 3. Метод изменения среднего балла (Setter с проверкой)
    def update_gpa(self, new_gpa: float) -> bool:
        """Изменяет средний балл (GPA) с проверкой корректности (0.0 <= GPA <= 4.0)."""
        if 0.0 <= new_gpa <= 4.0:
            self.__gpa = new_gpa
            print(f"✅ GPA для студента {self.__name} обновлён до {self.__gpa:.2f}.")
            return True
        else:
            print(f"❌ Ошибка: Некорректное значение GPA ({new_gpa:.2f}). GPA должен быть в диапазоне от 0.0 до 4.0.")
            return False

    # Вспомогательный метод для сохранения в JSON (получение данных)
    def to_dict(self) -> dict:
        """Возвращает данные студента в виде словаря для сохранения."""
        return {
            "name": self.__name,
            "group": self.__group,
            "gpa": self.__gpa
        }

    # Геттеры (методы доступа)
    def get_name(self) -> str:
        return self.__name

class Group:
    """Класс для управления списком студентов (объектов Student)."""

    # 1. Инициализация: список студентов пуст при создании группы
    def __init__(self):
        self.students = []  # Список для хранения объектов Student

    # 2. Добавление студента
    def add_student(self, student: Student):
        """Добавляет объект Student в список группы."""
        self.students.append(student)
        print(f"✅ Студент {student.get_name()} добавлен в группу.")

    # 3. Удаление студента по имени
    def remove_student(self, name: str) -> bool:
        """Удаляет студента из списка по имени."""
        initial_count = len(self.students)
        # Создаем новый список, исключая студента с искомым именем
        self.students = [s for s in self.students if s.get_name().lower() != name.lower()]
        if len(self.students) < initial_count:
            print(f"✅ Студент с именем '{name}' удалён.")
            return True
        else:
            print(f"❌ Студент с именем '{name}' не найден.")
            return False

    # 4. Вывод всех студентов
    def show_all(self):
        """Выводит информацию обо всех студентах."""
        if not self.students:
            print("\nСписок студентов пуст.")
            return

        print("\n--- Список всех студентов ---")
        for student in self.students:
            student.display_info()
        print("------------------------------")

    # 5. Вывод лучших студентов
    def get_top_students(self, threshold: float):
        """Выводит студентов, чей GPA выше указанного порога."""
        top_students = [s for s in self.students if s.to_dict()['gpa'] > threshold]

        if not top_students:
            print(f"\nНет студентов с GPA выше {threshold:.2f}.")
            return

        print(f"\n--- Студенты с GPA выше {threshold:.2f} ---")
        for student in top_students:
            student.display_info()
        print("------------------------------------------")

    # 6. Сохранение в JSON (Требование задания)
    def save_to_json(self, filename: str):
        """Сохраняет список студентов в JSON файл."""
        # Преобразуем список объектов Student в список словарей
        data = [s.to_dict() for s in self.students]
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                # json.dump записывает данные в файл
                json.dump(data, f, indent=4, ensure_ascii=False)
            print(f"\n✅ Список студентов успешно сохранён в файл '{filename}'.")
        except IOError as e:
            print(f"\n❌ Ошибка при сохранении в файл: {e}")


def run_example():
    """Демонстрация работы программы: создание объектов и вызов методов."""
    print("=================================================")
    print("--- Запуск Демонстрации Системы учёта студентов ---")
    print("=================================================")

    # 1. Создание объектов Student
    print("\n--- 1. Создание студентов ---")
    stud1 = Student("Алихан", "ИС-24-22", 3.75)
    stud2 = Student("Мадина", "ИС-24-22", 3.92)
    stud3 = Student("Ерлан", "ИС-24-22", 2.95)
    stud4 = Student("Айжан", "ИС-24-22", 4.00)

    # 2. Создание объекта Group
    group_is22_1 = Group()

    # 3. Взаимодействие: Добавление студентов в группу
    print("\n--- 3. Добавление студентов в группу ---")
    group_is22_1.add_student(stud1)
    group_is22_1.add_student(stud2)
    group_is22_1.add_student(stud3)
    group_is22_1.add_student(stud4)

    # 4. Вывод всех студентов
    group_is22_1.show_all()

    # 5. Взаимодействие: Изменение GPA (с проверкой)
    print("\n--- 5. Изменение GPA (update_gpa) ---")
    stud1.update_gpa(3.80)  # Корректное обновление
    stud3.update_gpa(4.5)  # Некорректное значение (срабатывает проверка)
    stud3.update_gpa(3.10)  # Корректное обновление

    # 6. Поиск лучших студентов (get_top_students)
    group_is22_1.get_top_students(threshold=3.85)

    # 7. Взаимодействие: Удаление студента
    print("\n--- 7. Удаление студента (remove_student) ---")
    group_is22_1.remove_student("Ерлан")
    group_is22_1.remove_student("Неизвестный")  # Проверка удаления несуществующего

    # 8. Повторный вывод всех студентов (после удаления)
    group_is22_1.show_all()

    # 9. Сохранение данных в students.json
    group_is22_1.save_to_json("students.json")

    # Главная точка входа в программу


if __name__ == "__main__":
    run_example()