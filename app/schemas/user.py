from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=4, max_length=100)

class UserLogin(BaseModel):
    email: EmailStr
    password: str