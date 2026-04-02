import uuid
from sqlalchemy import Column, String, Enum
from app.db.base import Base
from app.utils.enums import Role, UserStatus

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(Enum(Role), default=Role.VIEWER)
    status = Column(Enum(UserStatus), default=UserStatus.ACTIVE)