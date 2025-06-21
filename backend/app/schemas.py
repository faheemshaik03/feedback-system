from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class FeedbackBase(BaseModel):
    strengths: str
    improvements: str
    sentiment: str

class FeedbackCreate(FeedbackBase):
    employee_id: int
    manager_id: int

class FeedbackOut(FeedbackBase):
    id: int
    acknowledged: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
