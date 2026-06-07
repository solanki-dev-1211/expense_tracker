from app.database.db import Database
from app.models.expense import Expense
from app.services.expense_service import ExpenseService
from app.utils.validators import (
    validate_amount,
    validate_date
)


def add_expense():

    title = input("Title: ")
    category = input("Category: ")

    amount = validate_amount(
        input("Amount: ")
    )

    if amount is None:
        print("Invalid Amount")
        return

    date = input(
        "Date (YYYY-MM-DD): "
    )

    if not validate_date(date):
        print("Invalid Date")
        return

    notes = input("Notes: ")

    expense = Expense(
        title=title,
        category=category,
        amount=amount,
        expense_date=date,
        notes=notes
    )

    ExpenseService.add_expense(expense)

    print("\nExpense Added Successfully")


def view_expenses():

    expenses = ExpenseService.get_all_expenses()

    if not expenses:
        print("\nNo Expenses Found")
        return

    headers = [
        "ID",
        "Title",
        "Category",
        "Amount",
        "Date",
        "Notes"
    ]

    ExpenseService.display_table(
        expenses,
        headers
    )


def delete_expense():

    expense_id = input(
        "Expense ID: "
    )

    ExpenseService.delete_expense(
        expense_id
    )

    print("Expense Deleted")


def total_expense():

    total = ExpenseService.total_expense()

    print(
        f"\nTotal Expenses: ₹{total:.2f}"
    )


def category_report():

    report = ExpenseService.category_report()

    ExpenseService.display_table(
        report,
        ["Category", "Total"]
    )


def main():

    Database.initialize()

    while True:

        print("\n")
        print("=" * 40)
        print("      EXPENSE TRACKER")
        print("=" * 40)

        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Total Expense")
        print("5. Category Report")
        print("6. Exit")

        choice = input(
            "\nEnter Choice: "
        )

        match choice:

            case "1":
                add_expense()

            case "2":
                view_expenses()

            case "3":
                delete_expense()

            case "4":
                total_expense()

            case "5":
                category_report()

            case "6":
                print("Goodbye!")
                break

            case _:
                print("Invalid Choice")


if __name__ == "__main__":
    main()