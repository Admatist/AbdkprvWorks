// ui.js
export function renderList(listElem, expenses, deleteFn) {
  listElem.innerHTML = ''; // Очистка списка

  expenses.forEach((expense, index) => {
    const li = document.createElement('li');
    li.className = 'expense-item';
    li.innerHTML =
      `<span><strong>${expense.description}</strong> (${expense.category}): ${expense.amount} KZT</span>
      <button onclick="deleteFn(${index})">Удалить</button>
    `;

    listElem.appendChild(li);
  });
}