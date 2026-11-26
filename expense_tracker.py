
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

def main():
    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add an expense")
        print("2. View expenses")
        print("3. Show total")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()