
expenses = []

def add_expense():
    name = input("Expense name: ")
    amount = float(input("Amount: "))
    expenses.append((name, amount))
    print("Expense added!")

def show_expenses():
    if not expenses:
        print("No expenses yet.")
    else:
        for i, (name, amount) in enumerate(expenses, 1):
            print(f"{i}. {name}: {amount:.2f}")

def show_total():
    total = sum(amount for _, amount in expenses)
    print(f"Total: {total:.2f}")

def delete_expense():
    show_expenses()
    if not expenses:
        return
    try:
        num = int(input("Enter expense number to delete: "))
        if 1 <= num <= len(expenses):
            removed = expenses.pop(num - 1)
            print(f"Deleted: {removed[0]}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a number.")

def main():
    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add an expense")
        print("2. View expenses")
        print("3. Show total")
        print("4. Delete an expense")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            delete_expense()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()