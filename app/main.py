from fastapi import FastAPI, HTTPException, status

from app.database import ExpenseRepository
from app.models import Expense, ExpenseCreate

app = FastAPI(
    title="Expense Tracker API",
    description="A simple FastAPI + SQLite expense tracking backend.",
    version="1.0.0",
)

repository = ExpenseRepository()


@app.get("/")
def home():
    return {"message": "Expense Tracker API is running"}


@app.post("/expenses", response_model=Expense, status_code=status.HTTP_201_CREATED)
def create_expense(expense: ExpenseCreate):
    return repository.create_expense(
        description=expense.description,
        amount=expense.amount,
        category=expense.category,
    )


@app.get("/expenses", response_model=list[Expense])
def list_expenses():
    return repository.list_expenses()


@app.get("/expenses/{expense_id}", response_model=Expense)
def get_expense(expense_id: int):
    expense = repository.get_expense(expense_id)
    if expense is None:
        raise HTTPException(status_code=404, detail="Expense not found")
    return expense


@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):
    deleted = repository.delete_expense(expense_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Expense not found")
    return {"message": "Expense deleted successfully"}


@app.get("/summary")
def spending_summary():
    return {"total_spending": repository.total_spending()}
