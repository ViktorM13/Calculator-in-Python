import pytest
from tracker import add_expense, get_expenses, get_total, get_by_category

def test_add_expense():
    """Тестирование добавления расходов."""
    add_expense(100, "Еда", "Обед")
    add_expense(200, "Транспорт")
    assert len(get_expenses()) == 2

def test_get_total():
    """Тестирование расчета общей суммы."""
    add_expense(300, "Развлечения", "Кино")
    assert get_total() == 600 

def test_get_by_category():
    """Тестирование фильтрации по категории."""
    result = get_by_category("Еда")
    assert len(result) == 1
    assert result[0]['amount'] == 100
    assert result[0]['description'] == "Обед"

def test_empty_expenses():
    """Тестирование пустого списка расходов."""
    from tracker import expenses
    expenses.clear() 
    assert len(get_expenses()) == 0
    assert get_total() == 0
    assert len(get_by_category("Любая")) == 0

def test_invalid_expense():
    """Тестирование обработки некорректных данных."""
    with pytest.raises(TypeError):
        add_expense("Не число", "Категория", "Описание")
