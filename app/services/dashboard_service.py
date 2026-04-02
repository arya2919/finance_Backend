from fastapi import Depends
from sqlalchemy import func
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.financial_record import FinancialRecord
from app.utils.enums import RecordType

def get_summary_of_financial_records(db: Session):
    total_income = db.query(func.sum(FinancialRecord.amount))\
        .filter(FinancialRecord.type == RecordType.INCOME).scalar() or 0

    total_expense = db.query(func.sum(FinancialRecord.amount))\
        .filter(FinancialRecord.type == RecordType.EXPENSE).scalar() or 0

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "net_balance": total_income - total_expense
    }


def category_breakdown_of_financial_records(
    db: Session
):
    results = db.query(
        FinancialRecord.category,
        func.sum(FinancialRecord.amount)
    ).group_by(FinancialRecord.category).all()

    return [
        {"category": r[0], "total": r[1]}
        for r in results
    ]