from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.dependencies.auth import require_role
from app.services.dashboard_service import category_breakdown_of_financial_records, get_summary_of_financial_records
from app.utils.enums import Role

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


@router.get("/summary")
def get_summary(
    db: Session = Depends(get_db),
    user = Depends(require_role([Role.ADMIN, Role.ANALYST]))
):
    result = get_summary_of_financial_records(db)
    return result


@router.get("/categories")
def category_breakdown(
    db: Session = Depends(get_db),
    user = Depends(require_role([Role.ADMIN, Role.ANALYST]))
):
    results = category_breakdown_of_financial_records(db)
    return results