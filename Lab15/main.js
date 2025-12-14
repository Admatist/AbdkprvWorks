// main.js
import { saveExpenses, loadExpenses } from './storage.js';
import { renderList } from './ui.js';
import { filterExpenses } from './utils.js';

// Загрузка данных при старте
let expenses = loadExpenses();

// Получение DOM-элементов
const form = document.getElementById('expenseForm');
const listElem = document.getElementById('expenseList');
const filterInput = document.getElementById('filterInput');

// Функция для удаления (операция над данными: удаление)
window.deleteExpense = (index) => { // Доступна глобально для onclick в ui.js
  expenses.splice(index, 1); // Удаление элемента из массива
  saveExpenses(expenses);
  renderList(listElem, expenses, deleteExpense);
};

// Обработчик добавления (операция над данными: добавление)
form.addEventListener('submit', (e) => {
  e.preventDefault();

  const description = document.getElementById('descriptionInput').value.trim();
  const amount = parseFloat(document.getElementById('amountInput').value);
  const category = document.getElementById('categoryInput').value;

  if (description && !isNaN(amount)) {
    // Добавление нового расхода
    const newExpense = { description, amount, category, id: Date.now() };
    expenses.push(newExpense);
    saveExpenses(expenses);

    // Очистка формы
    form.reset();

    // Перерисовка списка
    renderList(listElem, expenses, deleteExpense);
  }
});

// Обработчик фильтрации (операция над данными: поиск/фильтрация)
filterInput.addEventListener('input', () => {
  const query = filterInput.value.trim();
  const filteredExpenses = filterExpenses(expenses, query);
  renderList(listElem, filteredExpenses, deleteExpense);
});

// Инициализация: первоначальная отрисовка списка
renderList(listElem, expenses, deleteExpense);