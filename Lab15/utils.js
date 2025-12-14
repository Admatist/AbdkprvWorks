// utils.js
// Использование Array.prototype.filter для реализации поиска
export function filterExpenses(expenses, query) {
    const lowerCaseQuery = query.toLowerCase();
    return expenses.filter(expense =>
        expense.description.toLowerCase().includes(lowerCaseQuery) ||
        expense.category.toLowerCase().includes(lowerCaseQuery)
    );
}

// Дополнительная функция (не обязательно, но полезно для закрепления структур данных)
export function getExpensesByCategory(expenses) {
    // Использование Map для подсчёта сумм по категориям
    const categoryMap = new Map();
    expenses.forEach(expense => {
        const currentTotal = categoryMap.get(expense.category) || 0;
        categoryMap.set(expense.category, currentTotal + parseFloat(expense.amount));
    });
    return categoryMap; // Возвращает Map: {'Food' => 1200, 'Transport' => 500}
}