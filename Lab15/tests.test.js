// tests.test.js

// ** 1. ИМИТАЦИЯ LocalStorage (должна быть в начале) **
const localStorageMock = (function() {
    let store = {};
    return {
        getItem: function(key) {
            return store[key] || null;
        },
        setItem: function(key, value) {
            store[key] = value.toString();
        },
        clear: function() {
            store = {};
        }
    };
})();

// Прикрепляем имитацию LocalStorage к глобальному объекту
Object.defineProperty(global, 'localStorage', { value: localStorageMock });

// ** 2. Импорты функций **
import { saveExpenses, loadExpenses } from './storage.js';

// ** 3. Сам тест **
test("Тест: Сохранение и загрузка расходов из LocalStorage", () => {
  // 1. Создаем тестовые данные (объекты)
  const sample = [
      { description: "Кофе", amount: 1200, category: "Food" },
      { description: "Бензин", amount: 3000, category: "Transport" }
  ];

  // 2. Вызываем функции сохранения и загрузки
  saveExpenses(sample);
  const loaded = loadExpenses();

  // 3. Проверяем, что загруженный массив идентичен исходному
  expect(loaded).toEqual(sample);
});