from tabulate import tabulate

from app.database.db import Database


class ExpenseService:

    @staticmethod
    def add_expense(expense):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO expenses
        (
            title,
            category,
            amount,
            expense_date,
            notes
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            expense.title,
            expense.category,
            expense.amount,
            expense.expense_date,
            expense.notes
        ))

        conn.commit()
        conn.close()

    @staticmethod
    def get_all_expenses():

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT *
        FROM expenses
        ORDER BY expense_date DESC
        """)

        rows = cursor.fetchall()

        conn.close()

        return rows

    @staticmethod
    def delete_expense(expense_id):

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM expenses WHERE id=?",
            (expense_id,)
        )

        conn.commit()
        conn.close()

    @staticmethod
    def total_expense():

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT SUM(amount) FROM expenses"
        )

        total = cursor.fetchone()[0]

        conn.close()

        return total or 0

    @staticmethod
    def category_report():

        conn = Database.connect()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT
            category,
            SUM(amount)
        FROM expenses
        GROUP BY category
        """)

        rows = cursor.fetchall()

        conn.close()

        return rows

    @staticmethod
    def display_table(data, headers):

        print(
            tabulate(
                data,
                headers=headers,
                tablefmt="grid"
            )
        )