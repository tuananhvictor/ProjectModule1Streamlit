from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas
from .database import get_db
from .utils import get_password_hash  # Giả sử bạn có một tệp utils.py chứa hàm này

app = FastAPI()

@app.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.mail == user.mail).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(user.password, shift=3, mode='e')
    db_user = models.User(
        name=user.name,
        mail=user.mail,
        full_name=user.full_name,
        age=user.age,
        date_of_birth=user.date_of_birth,
        password_hash=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
