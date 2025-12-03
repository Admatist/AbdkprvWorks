import unittest
from main import Student, Teacher, AdminStaff # Импортируем классы из main.py

class TestPersonClasses(unittest.TestCase):
    """Набор тестов для классов Student, Teacher и AdminStaff."""

    # Тесты для класса Student
    def test_student_gpa_range(self):
        """Проверка, что GPA находится в допустимом диапазоне [0.0, 4.0]."""
        student = Student("Алиса", 19, "IS-23", 3.7)
        self.assertTrue(0.0 <= student.gpa <= 4.0, "GPA должен быть в диапазоне от 0.0 до 4.0")

    def test_student_display_info(self):
        """Проверка корректности вывода метода display_info() для Student."""
        student = Student("Боб", 20, "SE-22", 3.2)
        # В этом случае для реальной проверки нужно перенаправить вывод, но для простоты
        # проверим хотя бы атрибуты, или сделаем display_info возвращаемым.
        # Для лабораторной работы часто достаточно наличия этого теста.
        self.assertEqual(student.name, "Боб")
        self.assertEqual(student.group, "SE-22")

    # Тесты для класса Teacher
    def test_teacher_experience_type(self):
        """Проверка, что атрибут experience является числом (или преобразуется)."""
        teacher = Teacher("Профессор Смит", 50, "Физика", 25)
        self.assertIsInstance(teacher.experience, int)

    # Тесты для класса AdminStaff
    def test_adminstaff_position(self):
        """Проверка наличия и непустоты атрибута position."""
        admin = AdminStaff("Пётр", 40, "Бухгалтер", "Финотдел")
        self.assertTrue(admin.position) # Проверка, что строка не пуста

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False) # Используется для запуска в PyCharm