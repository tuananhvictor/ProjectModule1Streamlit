from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas
from .database import get_db
from .utils import get_password_hash  # Giả sử bạn có một tệp utils.py chứa hàm này
from datetime import datetime

app = FastAPI()


@app.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        db_user = db.query(models.User).filter(models.User.mail == user.mail).first()
        if db_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        
        hashed_password = get_password_hash(user.password, shift=3, mode='e')
        db_user = models.User(
            name=user.name,
            mail=user.mail,
            full_name=user.full_name,
            age=user.age,
            date_of_birth=datetime.strptime(user.date_of_birth, '%Y-%m-%d').date(),
            password_hash=hashed_password
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
def read_root():
    return {"Hello": "World"}
