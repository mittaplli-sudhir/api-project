from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a task
@app.post("/tasks/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)

# Read a task by ID
@app.get("/tasks/{task_id}", response_model=schemas.Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    return crud.get_task(db, task_id)

# Update a task by ID
@app.put("/tasks/{task_id}", response_model=schemas.Task)
def update_task(task_id: int, task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.update_task(db, task_id, task)

# Delete a task by ID
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    return crud.delete_task(db, task_id)