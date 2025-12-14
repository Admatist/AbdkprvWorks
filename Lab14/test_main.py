import unittest
# Импортируем функции для тестирования
from main import calculate_average, determine_grade_letter, student_report


# 5. Написать unit-тесты
class TestGrades(unittest.TestCase):
    """Класс для Unit-тестирования функций расчёта оценок"""

    # Тестирование расчёта среднего балла
    def test_average_calculation(self):
        # Проверка обычного случая
        self.assertEqual(calculate_average([90, 80, 100]), 90.0)
        # Проверка с десятичными дробями
        self.assertEqual(calculate_average([95.5, 85]), 90.25)

    # Тестирование обработки пустого списка (ValueError)
    def test_average_empty(self):
        with self.assertRaises(ValueError):
            calculate_average([])

    # Тестирование обработки некорректного типа данных (TypeError)
    def test_average_type_error(self):
        with self.assertRaises(TypeError):
            calculate_average([90, "80", 70])

    # Тестирование определения буквенной оценки
    def test_letter_grade(self):
        self.assertEqual(determine_grade_letter(95), "A")
        self.assertEqual(determine_grade_letter(82), "B")
        self.assertEqual(determine_grade_letter(75), "C")
        self.assertEqual(determine_grade_letter(65), "D")
        self.assertEqual(determine_grade_letter(40), "F")

    # Тестирование функции формирования отчёта (Интеграционный тест)
    def test_student_report(self):
        result = student_report("Алиса", [100, 90, 80])
        # Проверяем, что в отчёте содержатся имя, метка среднего балла и итоговая оценка
        self.assertIn("Алиса", result)
        self.assertIn("Средний балл", result)
        self.assertIn("A", result)


if __name__ == "__main__":
    unittest.main()