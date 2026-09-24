from pathlib import Path

from app.database import ExpenseRepository


def test_create_and_get_expense(tmp_path: Path):
    repo = ExpenseRepository(tmp_path / "test.db")

    created = repo.create_expense("Groceries", 48.75, "Food")
    fetched = repo.get_expense(created["id"])

    assert fetched is not None
    assert fetched["description"] == "Groceries"
    assert fetched["amount"] == 48.75
    assert fetched["category"] == "Food"


def test_list_and_total_expenses(tmp_path: Path):
    repo = ExpenseRepository(tmp_path / "test.db")

    repo.create_expense("Groceries", 40.00, "Food")
    repo.create_expense("Gas", 35.50, "Transport")

    expenses = repo.list_expenses()

    assert len(expenses) == 2
    assert repo.total_spending() == 75.50


def test_delete_expense(tmp_path: Path):
    repo = ExpenseRepository(tmp_path / "test.db")

    created = repo.create_expense("Coffee", 5.25, "Food")
    deleted = repo.delete_expense(created["id"])

    assert deleted is True
    assert repo.get_expense(created["id"]) is None
