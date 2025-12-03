class Person:
    """Базовый класс для всех типов персонала в учебном заведении."""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        """Выводит общую информацию о человеке."""
        print(f"Имя: {self.name}, Возраст: {self.age}")

class Student(Person):
    """Класс, представляющий студента."""
    def __init__(self, name, age, group, gpa):
        super().__init__(name, age) # Вызов конструктора базового класса
        self.group = group
        self.gpa = gpa

    def display_info(self):
        """Переопределенный метод для вывода информации о студенте."""
        super().display_info() # Вызов display_info() базового класса
        print(f"Группа: {self.group}, Средний балл (GPA): {self.gpa}")

class Teacher(Person):
    """Класс, представляющий преподавателя."""
    def __init__(self, name, age, subject, experience):
        super().__init__(name, age)
        self.subject = subject
        self.experience = experience # стаж в годах

    def display_info(self):
        """Переопределенный метод для вывода информации о преподавателе."""
        super().display_info()
        print(f"Предмет: {self.subject}, Стаж: {self.experience} лет")

class AdminStaff(Person):
    """Класс, представляющий административный персонал."""
    def __init__(self, name, age, position, department):
        super().__init__(name, age)
        self.position = position
        self.department = department

    def display_info(self):
        """Переопределенный метод для вывода информации об административном сотруднике."""
        super().display_info()
        print(f"Должность: {self.position}, Отдел: {self.department}")

# Демонстрация полиморфизма
if __name__ == "__main__":
    # Создание объектов
    student1 = Student("Алиса", 19, "IS-23", 3.7)
    teacher1 = Teacher("Профессор Иванов", 45, "Программирование", 15)
    admin1 = AdminStaff("Елена Петровна", 55, "Секретарь", "Деканат")

    # Список для демонстрации полиморфизма
    staff_list = [student1, teacher1, admin1]

    print("--- Информация о персонале Учебного заведения ---")
    for person in staff_list:
        person.display_info() # Вызов переопределенного метода
        print("-" * 20)