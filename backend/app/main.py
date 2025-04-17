from fastapi import FastAPI
from .routers import todos, auth

app = FastAPI()
app.include_router(auth.router, prefix="/auth")
app.include_router(todos.router, prefix="/todos")