from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional

class UserBase(BaseModel):
    name: str
    mail: str
    full_name: str
    age: int
    date_of_birth: str  # Đổi thành kiểu chuỗi

class UserCreate(UserBase):
    password: str

class User(UserBase):
    user_id: int
    created_at: datetime
    last_login: Optional[datetime]
    login_count: int
    updated_at: Optional[datetime]
    is_active: bool
    role: str

    class Config:
        orm_mode = True

# Các schema khác...
