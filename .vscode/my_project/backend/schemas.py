from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional


class UserBase(BaseModel):
    name: str
    mail: str
    full_name: str
    age: int
    date_of_birth: date


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


class EntryBase(BaseModel):
    title: str
    content_hash: str
    is_public: bool
    categories_id: int
    tags: str


class EntryCreate(EntryBase):
    pass


class Entry(EntryBase):
    entry_id: int
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


class CategoryBase(BaseModel):
    name: str
    id: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    categories_id: int

    class Config:
        orm_mode = True


class LoginHistoryBase(BaseModel):
    login_time: datetime
    ip_address: str
    device_info: str
    login_status: str


class LoginHistoryCreate(LoginHistoryBase):
    pass


class LoginHistory(LoginHistoryBase):
    login_id: int
    user_id: int
    logout_time: Optional[datetime]

    class Config:
        orm_mode = True
