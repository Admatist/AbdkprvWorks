# Задание 1. Вычисление факториала
def factorial(n):
    # Базовое (остановочное) условие: 0! и 1! равны 1
    if n == 0 or n == 1:
        return 1
    # Рекурсивный шаг: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

# Проверка
test_number = 5
result_factorial = factorial(test_number)
print(f"--- Задание 1: Факториал ---")
print(f"Факториал числа {test_number} равен: {result_factorial}") # Ожидаемый результат: 120
print("-" * 30)

# ------------------------------------------------------------------

# Задание 2. Рекурсивный бинарный поиск
def binary_search(arr, left, right, x):
    # Базовое условие 1: Границы поиска сошлись (элемент не найден)
    if right < left:
        return -1  # Возвращаем -1, если элемент не найден

    # Вычисляем средний индекс
    # Используем формулу для избежания переполнения: left + (right - left) // 2
    mid = left + (right - left) // 2

    # Базовое условие 2: Элемент найден в середине
    if arr[mid] == x:
        return mid # Возвращаем индекс

    # Рекурсивный шаг 1: Искомый элемент меньше среднего
    # Ищем в левой половине списка
    elif arr[mid] > x:
        # Уменьшение задачи: правая граница становится mid - 1
        return binary_search(arr, left, mid - 1, x)

    # Рекурсивный шаг 2: Искомый элемент больше среднего
    # Ищем в правой половине списка
    else:
        # Уменьшение задачи: левая граница становится mid + 1
        return binary_search(arr, mid + 1, right, x)

# Проверка
arr = [1, 3, 5, 7, 9, 11]
x = 7
result_index = binary_search(arr, 0, len(arr) - 1, x)

print(f"--- Задание 2: Рекурсивный бинарный поиск ---")
if result_index != -1:
    print(f"Элемент {x} найден на позиции: {result_index}") # Ожидаемый результат: 3
else:
    print(f"Элемент {x} не найден в списке.")
print("-" * 30)

# ------------------------------------------------------------------

# Задание 3. Рекурсивная сортировка QuickSort
def quicksort(arr):
    # Базовое условие: Список из 0 или 1 элемента уже отсортирован
    if len(arr) <= 1:
        return arr

    # Выбор опорного элемента (pivot) - берем элемент из середины для простоты
    pivot = arr[len(arr) // 2]

    # Создание трех подсписков
    # left: элементы меньше pivot
    left = [x for x in arr if x < pivot]
    # middle: элементы равные pivot (включая сам pivot)
    middle = [x for x in arr if x == pivot]
    # right: элементы больше pivot
    right = [x for x in arr if x > pivot]

    # Рекурсивный шаг: Сортируем левую и правую части и объединяем
    return quicksort(left) + middle + quicksort(right)

# Проверка
unsorted_list = [5, 2, 9, 1, 5, 6]
sorted_list = quicksort(unsorted_list)

print(f"--- Задание 3: QuickSort ---")
print(f"Исходный список: {unsorted_list}")
print(f"Отсортированный список: {sorted_list}") # Ожидаемый результат: [1, 2, 5, 5, 6, 9]
print("-" * 30)