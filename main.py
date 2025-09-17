from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Todo(BaseModel):
    id: int
    task: str
    done: bool = False

todos = []

@app.get("/")
def root():
    return {"message": "Todo API"}

@app.get("/todos")
def get_todos():
    return todos

@app.post("/todos")
def add_todo(todo: Todo):
    todos.append(todo.dict())
    return {"message": "Todo ditambahkan"}

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: Todo):
    for t in todos:
        if t["id"] == todo_id:
            t.update(todo.dict())
            return {"message": "Todo diperbarui"}
    return {"error": "Todo tidak ditemukan"}

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    global todos
    todos = [t for t in todos if t["id"] != todo_id]
    return {"message": "Todo dihapus"}
