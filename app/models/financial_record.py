import uuid
from sqlalchemy import Column, String, Float, Date, Enum
from app.db.base import Base
from app.utils.enums import RecordType

class FinancialRecord(Base):
    __tablename__ = "records"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    amount = Column(Float)
    type = Column(Enum(RecordType))
    category = Column(String)
    date = Column(Date)
    description = Column(String, nullable=True)
    created_by = Column(String)