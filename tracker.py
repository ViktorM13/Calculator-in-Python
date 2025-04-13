expenses = []

def add_expense(amount: float, category: str, description: str = ""):
    """
    Добавляет новый расход в список расходов.

    Args:
        amount (float): Сумма расхода;
        category (str): Категория расхода;
        description (str, optional): Описание расхода. По умолчанию не заполнено.
    """
    expense = {
        'amount': amount,
        'category': category,
        'description': description
    }
    expenses.append(expense)

def get_expenses():
    """
    Возвращает список всех расходов.

    Returns:
        list: Список словарей с расходами.
    """
    return expenses

def get_total():
    """
    Рассчитывает общую сумму всех расходов.

    Returns:
        float: Общая сумма расходов.
    """
    return sum(expense['amount'] for expense in expenses)

def get_by_category(category: str):
    """
    Возвращает расходы только по указанной категории.

    Args:
        category (str): Категория для фильтрации.

    Returns:
        list: Отфильтрованный список расходов
    """
    return [expense for expense in expenses if expense['category'].lower() == category.lower()]