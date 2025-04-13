from tracker import add_expense, get_expenses, get_total, get_by_category

def main():
    """
    Основная функция, реализующая пользовательский интерфейс.
    """
    print("Калькулятор расходов.")
    
    while True:
        print("\nМеню:")
        print("1. Добавить расход")
        print("2. Показать все расходы")
        print("3. Показать общую сумму расходов")
        print("4. Показать расходы по категории")
        print("5. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            try:
                amount = float(input("Введите сумму: "))
                category = input("Введите категорию: ")
                description = input("Введите описание (необязательно): ")
                add_expense(amount, category, description)
                print("Расход успешно добавлен!")
            except ValueError:
                print("Ошибка: сумма должна быть числом!")
                
        elif choice == "2":
            all_expenses = get_expenses()
            if not all_expenses:
                print("Нет добавленных расходов.")
            else:
                print("\nВсе расходы:")
                for idx, expense in enumerate(all_expenses, 1):
                    print(f"{idx}. {expense['category']}: {expense['amount']} руб. - {expense['description']}")
                    
        elif choice == "3":
            total = get_total()
            print(f"\nОбщая сумма расходов: {total} руб.")
            
        elif choice == "4":
            category = input("Введите категорию для фильтрации: ")
            filtered = get_by_category(category)
            if not filtered:
                print(f"Нет расходов в категории '{category}'.")
            else:
                print(f"\nРасходы в категории '{category}':")
                for idx, expense in enumerate(filtered, 1):
                    print(f"{idx}. {expense['amount']} руб. - {expense['description']}")
                    
        elif choice == "5":
            print("До свидания!")
            break
            
        else:
            print("Неверный ввод. Пожалуйста, выберите цифру от 1 до 5.")

if __name__ == "__main__":
    main()
