import sqlite3
from pathlib import Path


class ExpenseRepository:
    def __init__(self, db_path: str | Path = "expenses.db"):
        self.db_path = str(db_path)
        self.initialize()

    def connect(self):
        connection = sqlite3.connect(self.db_path)
        connection.row_factory = sqlite3.Row
        return connection

    def initialize(self):
        with self.connect() as connection:
            connection.execute(
                '''
                CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    description TEXT NOT NULL,
                    amount REAL NOT NULL CHECK (amount > 0),
                    category TEXT NOT NULL
                )
                '''
            )
            connection.commit()

    def create_expense(self, description: str, amount: float, category: str):
        with self.connect() as connection:
            cursor = connection.execute(
                '''
                INSERT INTO expenses (description, amount, category)
                VALUES (?, ?, ?)
                ''',
                (description, amount, category),
            )
            connection.commit()
            return self.get_expense(cursor.lastrowid)

    def list_expenses(self):
        with self.connect() as connection:
            rows = connection.execute(
                '''
                SELECT id, description, amount, category
                FROM expenses
                ORDER BY id DESC
                '''
            ).fetchall()
            return [dict(row) for row in rows]

    def get_expense(self, expense_id: int):
        with self.connect() as connection:
            row = connection.execute(
                '''
                SELECT id, description, amount, category
                FROM expenses
                WHERE id = ?
                ''',
                (expense_id,),
            ).fetchone()
            return dict(row) if row else None

    def delete_expense(self, expense_id: int):
        with self.connect() as connection:
            cursor = connection.execute(
                "DELETE FROM expenses WHERE id = ?",
                (expense_id,),
            )
            connection.commit()
            return cursor.rowcount > 0

    def total_spending(self):
        with self.connect() as connection:
            row = connection.execute(
                "SELECT COALESCE(SUM(amount), 0) AS total FROM expenses"
            ).fetchone()
            return float(row["total"])
