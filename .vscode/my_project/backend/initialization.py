# backend/initialization.py

from backend.database import engine, Base

def init_db():
    """Tạo tất cả các bảng trong cơ sở dữ liệu."""
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()

