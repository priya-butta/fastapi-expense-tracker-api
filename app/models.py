from pydantic import BaseModel, Field


class ExpenseCreate(BaseModel):
    description: str = Field(min_length=1, max_length=120)
    amount: float = Field(gt=0)
    category: str = Field(min_length=1, max_length=60)


class Expense(ExpenseCreate):
    id: int
