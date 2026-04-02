from pydantic import BaseModel
from datetime import date
from app.utils.enums import RecordType

class RecordCreate(BaseModel):
    amount: float
    type: RecordType
    category: str
    date: date
    description: str | None = None