from fastapi import APIRouter, Depends, HTTPException
from datetime import datetime
from ..models import Todo, TodoCreate
from .auth import get_current_user

router = APIRouter()
todos = []
id_seq = 1

@router.get("/", response_model=list[Todo])
async def list_todos(user=Depends(get_current_user)):
    return [t for t in todos if t.owner == user and t.due_date > datetime.utcnow()]

@router.post("/", response_model=Todo)
async def create_todo(todo: TodoCreate, user=Depends(get_current_user)):
    global id_seq
    new_todo = Todo(**todo.model_dump(), id=id_seq, owner=user)
    todos.append(new_todo)
    id_seq += 1
    return new_todo

@router.delete("/{todo_id}")
async def delete_todo(todo_id: int, user=Depends(get_current_user)):
    global todos
    todos = [t for t in todos if not (t.id == todo_id and t.owner == user)]
    return {"detail": "Deleted"}