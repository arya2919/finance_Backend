from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.dependencies.auth import get_current_user, require_role
from app.models.financial_record import FinancialRecord
from app.schemas.financial_record import RecordCreate
from app.utils.enums import Role

def create_financial_record(
    record_data: RecordCreate,
    db: Session = Depends(get_db),
    user = Depends(require_role([Role.ADMIN]))
):
    record = FinancialRecord(
        amount=record_data.amount,
        type=record_data.type,
        category=record_data.category,
        date=record_data.date,
        description=record_data.description,
        created_by=user.id
    )

    db.add(record)
    db.commit()
    db.refresh(record)

    return record


def get_filtered_records(
    type: str | None = None,
    category: str | None = None,
    start_date: str | None = None,
    end_date: str | None = None,
    limit: int = 10,
    offset: int = 0,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):    
    query = db.query(FinancialRecord)

    if type:
        query = query.filter(FinancialRecord.type == type)

    if category:
        query = query.filter(FinancialRecord.category == category)

    if start_date and end_date:
        query = query.filter(
            FinancialRecord.date >= start_date,
            FinancialRecord.date <= end_date
        )

    return query.offset(offset).limit(limit).all()