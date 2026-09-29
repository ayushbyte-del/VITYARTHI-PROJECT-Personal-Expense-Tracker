"""Personal Expense Tracker - Python Essentials Project"""

CATEGORIES = ("food", "travel", "shopping", "bills", "health", "fun", "other")

TIPS = (
    "Track small expenses because they add up quickly.",
    "Set a monthly budget before spending.",
    "Avoid unnecessary online purchases.",
    "Compare prices before buying something.",
    "Keep some money aside for emergencies."
)

SAMPLE = (
    (1, "food", 120.0, "Lunch"),
    (2, "travel", 80.0, "Bus"),
    (3, "shopping", 450.0, "T-shirt"),
    (4, "bills", 300.0, "Mobile recharge"),
    (5, "health", 200.0, "Medicine"),
    (6, "fun", 150.0, "Movie"),
    (7, "food", 90.0, "Snacks"),
    (8, "travel", 60.0, "Auto")
)


def summation(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def to_base(number, base=36):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if number == 0:
        return "0"
    result = ""
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result


def find_max(items):
    maximum = items[0]
    for item in items[1:]:
        if item > maximum:
            maximum = item
    return maximum


def find_min(items):
    minimum = items[0]
    for item in items[1:]:
        if item < minimum:
            minimum = item
    return minimum


def sort_list(items):
    values = list(items)
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if values[j] < values[i]:
                values[i], values[j] = values[j], values[i]
    return values


def median(items):
    values = sort_list(items)
    middle = len(values) // 2
    if len(values) % 2 == 1:
        return values[middle]
    return (values[middle - 1] + values[middle]) / 2


def parse_whole(text, name, low=0, high=None):
    text = text.strip()
    if text == "" or not text.isdigit():
        raise ValueError(name + " must be a whole number.")
    value = 0
    for ch in text:
        value = value * 10 + (ord(ch) - ord("0"))
    if value < low:
        raise ValueError(name + " is too small.")
    if high is not None and value > high:
        raise ValueError(name + " is too large.")
    return value


def parse_amount(text):
    text = text.strip()
    if text == "":
        raise ValueError("Amount cannot be empty.")
    if text.count(".") > 1:
        raise ValueError("Invalid amount.")
    for ch in text.replace(".", ""):
        if ch < "0" or ch > "9":
            raise ValueError("Amount must contain only numbers.")
    amount = float(text)
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")
    return amount


def parse_category(text):
    value = text.strip().lower()
    if value not in CATEGORIES:
        raise ValueError("Invalid category.")
    return value


def parse_text(text):
    value = text.strip()
    if value == "":
        raise ValueError("Text cannot be empty.")
    return value


def ask(prompt, parser, *args):
    while True:
        try:
            return parser(input(prompt), *args)
        except ValueError as error:
            print("Error:", error)


# EXPENSE MANAGEMENT

def add_expense(expenses, expense_id, category, amount, note):
    expenses.append((expense_id, category, amount, note))


def find_by_id(expenses, expense_id):
    for expense in expenses:
        if expense[0] == expense_id:
            return expense
    return None


def show(expenses):
    if not expenses:
        print("\nNo expenses found.")
        return
    print("\nID   Category      Amount       Note")
    print("-" * 45)
    for expense_id, category, amount, note in expenses:
        print(f"{expense_id:<4} {category:<13} ₹{amount:<10.2f} {note}")


def receipt_code(expense_id):
    return "EXP-" + to_base(expense_id, 36)


def add_flow(expenses):
    print("\n--- Add Expense ---")
    if expenses:
        new_id = find_max([expense[0] for expense in expenses]) + 1
    else:
        new_id = 1
    category = ask("Category: ", parse_category)
    amount = ask("Amount: ", parse_amount)
    note = ask("Note: ", parse_text)
    add_expense(expenses, new_id, category, amount, note)
    print("Expense added.")
    print("Receipt code:", receipt_code(new_id))


def view_flow(expenses):
    print("\n--- All Expenses ---")
    show(expenses)


def update_flow(expenses):
    print("\n--- Update Expense ---")
    if not expenses:
        print("No expenses available.")
        return
    show(expenses)
    expense_id = ask("Enter expense ID: ", parse_whole, "ID", 1)
    old = find_by_id(expenses, expense_id)
    if old is None:
        print("Expense not found.")
        return
    category = ask("New category: ", parse_category)
    amount = ask("New amount: ", parse_amount)
    note = ask("New note: ", parse_text)
    expenses[expenses.index(old)] = (expense_id, category, amount, note)
    print("Expense updated.")


def delete_flow(expenses):
    print("\n--- Delete Expense ---")
    if not expenses:
        print("No expenses available.")
        return
    show(expenses)
    expense_id = ask("Enter expense ID: ", parse_whole, "ID", 1)
    expense = find_by_id(expenses, expense_id)
    if expense is None:
        print("Expense not found.")
        return
    expenses.remove(expense)
    print("Expense deleted.")


def amounts_of(expenses):
    return [expense[2] for expense in expenses]


def category_totals(expenses):
    totals = {}
    for category in CATEGORIES:
        total = 0
        for expense in expenses:
            if expense[1] == category:
                total += expense[2]
        if total > 0:
            totals[category] = total
    return totals


def top_k(expenses, k):
    values = list(expenses)
    result = []
    for _ in range(min(k, len(values))):
        largest = find_max(amounts_of(values))
        for expense in values:
            if expense[2] == largest:
                result.append(expense)
                values.remove(expense)
                break
    return result


def summary_flow(expenses):
    print("\n--- Expense Summary ---")
    if not expenses:
        print("No expenses available.")
        return
    amounts = amounts_of(expenses)
    total = summation(amounts)
    print("Total expenses:", f"₹{total:.2f}")
    print("Number of expenses:", len(expenses))
    print("Average expense:", f"₹{total / len(amounts):.2f}")
    print("Maximum expense:", f"₹{find_max(amounts):.2f}")
    print("Minimum expense:", f"₹{find_min(amounts):.2f}")
    print("Median expense:", f"₹{median(amounts):.2f}")
    print("\nTop 3 expenses:")
    for expense in top_k(expenses, 3):
        print(expense[0], expense[1], f"₹{expense[2]:.2f}", expense[3])


def breakdown_flow(expenses):
    print("\n--- Category Breakdown ---")
    totals = category_totals(expenses)
    if not totals:
        print("No expenses available.")
        return
    for category, total in totals.items():
        print(f"{category:<12} ₹{total:.2f}")


# BUDGET & SAVINGS

def budget_status(expenses, budget):
    total = summation(amounts_of(expenses))
    remaining = budget - total
    print("\nBudget:", f"₹{budget:.2f}")
    print("Spent:", f"₹{total:.2f}")
    print("Remaining:", f"₹{remaining:.2f}")
    if remaining < 0:
        print("Budget exceeded by:", f"₹{-remaining:.2f}")
    else:
        print("You are within your budget.")


def budget_flow(expenses):
    print("\n--- Budget Check ---")
    budget = ask("Enter monthly budget: ", parse_amount)
    budget_status(expenses, budget)


def savings_flow():
    print("\n--- Saving Tips ---")
    index = 0
    while index < len(TIPS):
        print(f"{index + 1}. {TIPS[index]}")
        index += 1


def sample_flow(expenses):
    if expenses:
        print("Expenses already contain data.")
        return
    for expense in SAMPLE:
        expenses.append(expense)
    print("Sample expenses loaded.")


# MAIN MENU

MENU = """
=============================
     PERSONAL EXPENSE TRACKER
=============================
1. Add Expense
2. View Expenses
3. Update Expense
4. Delete Expense
5. Expense Summary
6. Category Breakdown
7. Check Budget
8. Saving Tips
9. Load Sample Data
0. Exit
"""


def main():
    expenses = []
    while True:
        print(MENU)
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_flow(expenses)
        elif choice == "2":
            view_flow(expenses)
        elif choice == "3":
            update_flow(expenses)
        elif choice == "4":
            delete_flow(expenses)
        elif choice == "5":
            summary_flow(expenses)
        elif choice == "6":
            breakdown_flow(expenses)
        elif choice == "7":
            budget_flow(expenses)
        elif choice == "8":
            savings_flow()
        elif choice == "9":
            sample_flow(expenses)
        elif choice == "0":
            print("Thank you for using the Expense Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()