# 💸 BudgetBuddy

<p align="center">
  <strong>Personal Finance Management Web Application</strong>
  <br />
  Track your expenses, manage your budget, and make smarter financial decisions.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-FastAPI-009688?logo=fastapi" alt="FastAPI" />
  <img src="https://img.shields.io/badge/React-Vite-646CFF?logo=vite" alt="React and Vite" />
  <img src="https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite" alt="SQLite" />
</p>

---

## 📖 About

BudgetBuddy is a personal finance management application designed to help students and individuals track their income and expenses, organize their finances, and manage their money more effectively.

## ✨ Features

- 🔐 User registration and authentication
- 💰 Income tracking and management
- 💸 Expense tracking and categorization
- 📊 Monthly budget management
- 🎯 Savings goal tracking
- 📈 Financial summaries and spending insights

## 🛠️ Tech Stack

- **Frontend:** React.js, Vite
- **Backend:** Python, FastAPI
- **Database:** SQLite
- **ORM:** SQLAlchemy
- **Authentication:** JWT
- **Password Hashing:** Argon2

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10+
- Node.js and npm
- Git

### 1. Clone the repository

```bash
git clone https://github.com/AceAchyut/BudgetBuddy.git
cd BudgetBuddy
```

### 2. Start the backend

```bash
cd backend
python -m venv venv
```

Activate the virtual environment.

**Windows**
```bash
venv\Scripts\activate
```

**macOS/Linux**
```bash
source venv/bin/activate
```

Install dependencies and run the server:

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 3. Start the frontend

Open another terminal from the project root:

```bash
cd frontend
npm install
npm run dev
```

## 📚 API Documentation

FastAPI provides interactive API documentation when the backend is running.

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 👨‍💻 Author

**Achyut Natekar**

- GitHub: [@AceAchyut](https://github.com/AceAchyut)
- LinkedIn: [Achyut Natekar](https://www.linkedin.com/in/achyut-natekar-8bb40634b/)

---

<p align="center">
  Made with 💚 by Achyut
</p>
