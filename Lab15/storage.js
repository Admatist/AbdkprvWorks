// storage.js
export function saveExpenses(expenses) {
  // Сохранение массива объектов в LocalStorage
  localStorage.setItem('expenses', JSON.stringify(expenses));
}

export function loadExpenses() {
  // Загрузка и парсинг, возвращает пустой массив, если данных нет
  const data = localStorage.getItem('expenses');
  return data ? JSON.parse(data) : [];
}