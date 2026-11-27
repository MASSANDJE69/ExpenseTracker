expenses = []

def add_expense(amount, category):
    expenses.append({"amount": amount, "category": category})
    print("Expense added!")

def view_expenses():
    if not expenses:
        print("No expenses yet.")
    else:
        for i, e in enumerate(expenses):
            print(f"{i}: {e['category']} - {e['amount']}")

def delete_expense(index):
    if 0 <= index < len(expenses):
        removed = expenses.pop(index)
        print(f"Deleted: {removed}")
    else:
        print("Invalid index!")

def average_expense():
    if not expenses:
        print("No expenses to calculate average.")
    else:
        total = sum(e["amount"] for e in expenses)
        avg = total / len(expenses)
        print(f"Average expense: {avg}")

# Test
add_expense(100, "Food")
add_expense(200, "Transport")
view_expenses()
average_expense()
delete_expense(0)
view_expenses()