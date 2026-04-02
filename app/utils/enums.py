from enum import Enum

class Role(str, Enum):
    ADMIN = "ADMIN"
    ANALYST = "ANALYST"
    VIEWER = "VIEWER"

class RecordType(str, Enum):
    INCOME = "INCOME"
    EXPENSE = "EXPENSE"

class UserStatus(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"