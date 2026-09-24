# FastAPI Expense Tracker API

A beginner-friendly backend API built with Python, FastAPI, and SQLite.

## What it demonstrates

- REST API design
- FastAPI request validation
- SQLite database operations
- CRUD-style backend logic
- Error handling
- Automated tests
- Interactive Swagger documentation

## Features

- Create an expense
- List all expenses
- Get one expense by ID
- Delete an expense
- Calculate total spending

## Project structure

```text
fastapi-expense-tracker-api/
├── app/
│   ├── __init__.py
│   ├── database.py
│   ├── main.py
│   └── models.py
├── tests/
│   └── test_database.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Install

```bash
pip install -r requirements.txt
```

## Run the API

```bash
uvicorn app.main:app --reload
```

Then open:

```text
http://127.0.0.1:8000/docs
```

## Run tests

```bash
pytest -q
```

## Example expense

```json
{
  "description": "Groceries",
  "amount": 48.75,
  "category": "Food"
}
```

## Technologies

Python, FastAPI, SQLite, Pydantic, Pytest, REST APIs.

## Cost

This project runs locally and uses free/open-source tools only. No cloud account or paid service is required.
