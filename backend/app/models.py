from pydantic import BaseModel, EmailStr
from datetime import datetime

class TodoBase(BaseModel):
    title: str
    description: str
    due_date: datetime

class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    id: int
    owner: EmailStr