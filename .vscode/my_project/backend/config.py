import os
from dotenv import load_dotenv

# Load biến môi trường từ file .env
load_dotenv()

class Config:
    DB_USER = os.getenv("DB_USER")
    DB_PASS = os.getenv("DB_PASS")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT", "3306")
    DB_NAME = os.getenv("DB_NAME")
    SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:cuncon123@localhost:3306/diary_app"
    API_URL = os.getenv("API_URL", "http://localhost:8000")  # Thêm nếu cần
