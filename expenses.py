expenses = []


def add_expense(description, amount):
    expenses.append({
        "description": description,
        "amount": amount
    })


def show_expenses():
    for expense in expenses:
        print(f"{expense['description']}: ${expense['amount']:.2f}")


add_expense("Coffee", 4.50)
add_expense("Lunch", 12.00)

show_expenses()
