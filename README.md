# Zorvyn Finance Dashboard Backend

## 📌 Overview

This is a backend system for managing financial records with role-based access control (RBAC) and analytics.

The system supports:

* User authentication (JWT-based)
* Role-based authorization (ADMIN, ANALYST, VIEWER)
* Financial record management (CRUD)
* Filtering & pagination
* Dashboard analytics (income, expenses, balance)
* Automated testing

---

## 🚀 Tech Stack

* **Python**
* **FastAPI** 
* **SQLAlchemy**
* **SQLite (default)**
* **Pytest**
* **JWT Authentication**

---

## 📁 Project Structure

```
app/
 ├── api/             # Route handlers
 ├── core/            # Security & config
 ├── db/              # Database setup
 ├── models/          # ORM models
 ├── schemas/         # Pydantic validation schemas
 ├── services/        # Business logic layer
 ├── dependencies/    # Auth & RBAC
 └── utils/           # Enums & helpers

tests/                # Test suite
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/arya2919/zorvyn-assignment.git
cd zorvyn-assignment
```


### 2. Create virtual environment

```
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```
pip3 install -r requirements.txt
```

### 4. Run the server

```
uvicorn app.main:app --reload
```

---

## 📖 API Documentation

Once the server is running:

👉 http://127.0.0.1:8000/docs

---

## 🔐 Authentication

* Uses JWT tokens
* Obtain token via `/auth/login`
* Use token in requests:

```
Authorization: Bearer <token>
```

NOTE: Bearer is already provided in the token place, no need to put it again.

---

## 👥 Roles & Permissions

| Role    | Permissions      |
| ------- | ---------------- |
| VIEWER  | Read-only access |
| ANALYST | Read + analytics |
| ADMIN   | Full access      |

---

## 🔐 Role Management Note

- By default, all newly registered users are assigned the `VIEWER` role.
- Elevated roles (`ADMIN`, `ANALYST`) are not user-configurable via API.
- Roles can be updated manually in the database for testing purposes.

This ensures proper role-based access control and prevents privilege escalation.



## 💰 Financial Records

Each record contains:

* amount
* type (INCOME / EXPENSE)
* category
* date
* description

Supports:

* Create
* Read
* Update
* Delete
* Filtering (type, category, date)
* Pagination

---

## 📊 Dashboard APIs

* Total income
* Total expenses
* Net balance
* Category-wise breakdown

---

## 🧪 Running Tests

```
pytest -v
```

* Uses a separate test database (`test.db`)
* Automatically created and destroyed during test runs

---

## ⚠️ Assumptions

* Single-tenant system (all users see shared data)
* Role assignment is controlled internally (not user-defined)
* SQLite used for simplicity (can switch to PostgreSQL via config)

---

## 🔥 Improvements (Future Scope)

* Add refresh tokens
* Add user management endpoints
* Add caching (Redis)
* Add pagination metadata
* Add Docker support

---

## 👨‍💻 Author

Arya Pandey
