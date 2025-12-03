import logging
import math
import sys

# Настройка логирования: запись ERROR сообщений в errors.log
# Файл будет создан в корневой папке проекта Lab11.
logging.basicConfig(
    filename='errors.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def get_positive_input(prompt):
    """Запрашивает числовое значение и проверяет его на положительность."""
    while True:
        try:
            # Попытка получить ввод
            value = float(input(prompt))
            # Обработка отрицательных значений (raise)
            if value <= 0:
                raise ValueError("Значение должно быть положительным.")
            return value
        except ValueError as e:
            # Обработка ошибки ввода (except)
            error_message = f"Неверный ввод: {e}. Пожалуйста, введите корректное положительное число."
            print(error_message)
            logging.error(error_message)  # Запись в errors.log
        except Exception as e:
            error_message = f"Непредвиденная ошибка при вводе: {e}"
            print(error_message)
            logging.error(error_message)
            sys.exit(1)


def calculate_compound_interest(P, r_percent, t):
    """Вычисляет итоговую сумму по формуле сложных процентов."""
    r = r_percent / 100
    n = 12  # Количество начислений в год (принять = 12)

    try:
        # Формула: S = P * (1 + r/n)**(n*t)
        total_sum = P * (1 + r / n) ** (n * t)
        return total_sum
    except Exception as e:
        # Проброс вычислительных ошибок
        raise Exception(f"Критическая вычислительная ошибка: {e}")


def main():
    print("--- Финансовый калькулятор ---")

    # 1. Запрос данных с проверкой
    P = get_positive_input("Введите сумму вклада: ")
    r = get_positive_input("Введите годовую ставку (%): ")
    t = get_positive_input("Введите срок вклада (в годах): ")

    try:
        # 2. Выполнение расчёта
        final_amount = calculate_compound_interest(P, r, t)
        formatted_amount = f"{final_amount:,.2f}"

        # 3. Вывод в консоль
        print(f"\nИтоговая сумма через {int(t)} лет: {formatted_amount} тенге")

        # 4. Запись результата в result.txt
        with open('result.txt', 'w', encoding='utf-8') as f:
            f.write(f"Вклад: {P:,.2f} тг\n")
            f.write(f"Ставка: {r}%\n")
            f.write(f"Срок: {int(t)} лет\n")
            f.write(f"Итоговая сумма: {formatted_amount} тг\n")

    except Exception as e:
        # 5. Обработка ошибок, возникших при расчете
        error_message = f"Ошибка выполнения программы: {e}"
        print(error_message)
        logging.error(error_message)

    finally:
        # 6. Гарантированное завершение (блок finally)
        print("Работа программы завершена.")


if __name__ == "__main__":
    main()