from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import database, models, schemas

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/feedback", response_model=schemas.FeedbackOut)
def create_feedback(feedback: schemas.FeedbackCreate, db: Session = Depends(get_db)):
    fb = models.Feedback(**feedback.dict())
    db.add(fb)
    db.commit()
    db.refresh(fb)
    return fb

@router.get("/feedback/{employee_id}")
def get_feedback(employee_id: int, db: Session = Depends(get_db)):
    return db.query(models.Feedback).filter(models.Feedback.employee_id == employee_id).all()
