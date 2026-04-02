from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.financial_record import FinancialRecord
from app.schemas.financial_record import RecordCreate
from app.dependencies.auth import get_current_user, require_role
from app.services.financial_record_service import create_financial_record, get_filtered_records
from app.utils.enums import Role

router = APIRouter(prefix="/records", tags=["Records"])


# 🔥 CREATE (ADMIN only)
@router.post("/")
def create_record(
    record: RecordCreate,
    db: Session = Depends(get_db),
    user = Depends(require_role([Role.ADMIN]))
):
    new_record = create_financial_record(record_data=record, db=db, user=user)

    return {"message": "Record created"}


# 🔥 READ (ALL roles)
@router.get("/")
def get_records(
    type: str | None = None,
    category: str | None = None,
    start_date: str | None = None,
    end_date: str | None = None,
    limit: int = 10,
    offset: int = 0,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    records = get_filtered_records(
        type=type,
        category=category,
        start_date=start_date,
        end_date=end_date,
        limit=limit,
        offset=offset,
        db=db,
        user=user
    )

    return records