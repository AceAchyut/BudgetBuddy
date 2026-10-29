
from datetime import datetime, date
from decimal import Decimal
from app.database import Base
from sqlalchemy import Column

from sqlalchemy import (
    Boolean,
    CheckConstraint,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    Numeric,
    String,
    Text,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = __import__("sqlalchemy").Column(Integer, primary_key=True, index=True)
    username = __import__("sqlalchemy").Column(String(50), unique=True, nullable=False)
    email = __import__("sqlalchemy").Column(String(255), unique=True, nullable=False, index=True)
    hashed_password = __import__("sqlalchemy").Column(String(255), nullable=False)
    role = __import__("sqlalchemy").Column(String(20), default="student", nullable=False)
    is_active = __import__("sqlalchemy").Column(Boolean, default=True, nullable=False)
    created_at = __import__("sqlalchemy").Column(DateTime, default=datetime.utcnow)

    profile = relationship(
        "Profile", back_populates="user", uselist=False,
        cascade="all, delete-orphan"
    )
    incomes = relationship("Income", back_populates="user", cascade="all, delete-orphan")
    expenses = relationship("Expense", back_populates="user", cascade="all, delete-orphan")
    budgets = relationship("Budget", back_populates="user", cascade="all, delete-orphan")
    savings_goals = relationship("SavingsGoal", back_populates="user", cascade="all, delete-orphan")
    notifications = relationship("Notification", back_populates="user", cascade="all, delete-orphan")


class Profile(Base):
    __tablename__ = "profiles"

    id = __import__("sqlalchemy").Column(Integer, primary_key=True, index=True)
    user_id = __import__("sqlalchemy").Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"),
        unique=True, nullable=False
    )
    full_name = __import__("sqlalchemy").Column(String(100), nullable=True)
    monthly_income = __import__("sqlalchemy").Column(Numeric(12, 2), default=Decimal("0.00"))
    currency = __import__("sqlalchemy").Column(String(3), default="INR")
    preferences = __import__("sqlalchemy").Column(Text, nullable=True)

    user = relationship("User", back_populates="profile")


class Income(Base):
    __tablename__ = "incomes"
    __table_args__ = (
        CheckConstraint("amount > 0", name="ck_income_amount_positive"),
    )

    id = __import__("sqlalchemy").Column(Integer, primary_key=True, index=True)
    user_id = __import__("sqlalchemy").Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    source = __import__("sqlalchemy").Column(String(50), nullable=False)
    amount = __import__("sqlalchemy").Column(Numeric(12, 2), nullable=False)
    date = __import__("sqlalchemy").Column(Date, default=date.today, nullable=False)
    description = __import__("sqlalchemy").Column(Text, nullable=True)

    user = relationship("User", back_populates="incomes")


class Expense(Base):
    __tablename__ = "expenses"
    __table_args__ = (
        CheckConstraint("amount > 0", name="ck_expense_amount_positive"),
    )

    id = __import__("sqlalchemy").Column(Integer, primary_key=True, index=True)
    user_id = __import__("sqlalchemy").Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    category = __import__("sqlalchemy").Column(String(50), nullable=False)
    amount = __import__("sqlalchemy").Column(Numeric(12, 2), nullable=False)
    date = __import__("sqlalchemy").Column(Date, default=date.today, nullable=False)
    description = __import__("sqlalchemy").Column(Text, nullable=True)
    payment_method = __import__("sqlalchemy").Column(String(30), nullable=True)

    user = relationship("User", back_populates="expenses")


class Budget(Base):
    __tablename__ = "budgets"
    __table_args__ = (
        CheckConstraint("amount > 0", name="ck_budget_amount_positive"),
        UniqueConstraint("user_id", "month", "category", name="uq_budget_user_month_category"),
    )

    id = __import__("sqlalchemy").Column(Integer, primary_key=True, index=True)
    user_id = __import__("sqlalchemy").Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    month = __import__("sqlalchemy").Column(String(7), nullable=False)  # YYYY-MM
    category = __import__("sqlalchemy").Column(String(50), nullable=False)
    amount = __import__("sqlalchemy").Column(Numeric(12, 2), nullable=False)

    user = relationship("User", back_populates="budgets")


class SavingsGoal(Base):
    __tablename__ = "savings_goals"
    __table_args__ = (
        CheckConstraint("target_amount > 0", name="ck_goal_target_positive"),
        CheckConstraint("current_amount >= 0", name="ck_goal_current_nonnegative"),
    )

    id = __import__("sqlalchemy").Column(Integer, primary_key=True, index=True)
    user_id = __import__("sqlalchemy").Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title = __import__("sqlalchemy").Column(String(100), nullable=False)
    target_amount = __import__("sqlalchemy").Column(Numeric(12, 2), nullable=False)
    current_amount = __import__("sqlalchemy").Column(Numeric(12, 2), default=Decimal("0.00"), nullable=False)
    deadline = __import__("sqlalchemy").Column(Date, nullable=True)
    is_completed = __import__("sqlalchemy").Column(Boolean, default=False, nullable=False)

    user = relationship("User", back_populates="savings_goals")


class Notification(Base):
    __tablename__ = "notifications"

    id = __import__("sqlalchemy").Column(Integer, primary_key=True, index=True)
    user_id = __import__("sqlalchemy").Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title = __import__("sqlalchemy").Column(String(150), nullable=False)
    message = __import__("sqlalchemy").Column(Text, nullable=False)
    notification_type = __import__("sqlalchemy").Column(String(30), default="general")
    is_read = __import__("sqlalchemy").Column(Boolean, default=False, nullable=False)
    created_at = __import__("sqlalchemy").Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="notifications")
