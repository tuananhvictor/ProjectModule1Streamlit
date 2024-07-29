from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base

class User(Base):
    __tablename__ = "User"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    age = Column(Integer)
    password_hash = Column(String(100))
    mail = Column(String(100), unique=True, index=True)
    full_name = Column(String(100))
    date_of_birth = Column(Date)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    last_login = Column(DateTime(timezone=True))
    login_count = Column(Integer, default=0)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    is_active = Column(Boolean, default=True)
    role = Column(String(50))

    entries = relationship("Entries", back_populates="user")
    login_history = relationship("LoginHistory", back_populates="user")

class Entries(Base):
    __tablename__ = "Entries"

    entry_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("User.user_id"))
    title = Column(String(200))
    content_hash = Column(String(100))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    is_public = Column(Boolean, default=False)
    categories_id = Column(Integer, ForeignKey("Categories.categories_id"))
    tags = Column(String(200))

    user = relationship("User", back_populates="entries")
    category = relationship("Categories", back_populates="entries")

class Categories(Base):
    __tablename__ = "Categories"

    categories_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    id = Column(String(50), unique=True)

    entries = relationship("Entries", back_populates="category")

class LoginHistory(Base):
    __tablename__ = "Login_History"

    login_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("User.user_id"))
    login_time = Column(DateTime(timezone=True))
    ip_address = Column(String(50))
    device_info = Column(String(200))
    logout_time = Column(DateTime(timezone=True))
    login_status = Column(String(50))

    user = relationship("User", back_populates="login_history")
