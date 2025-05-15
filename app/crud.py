from sqlalchemy.orm import Session
from . import models, schemas
from fastapi import HTTPException

# Get a task by ID
def get_task(db: Session, task_id: int):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# Create a new task
def create_task(db: Session, task: schemas.TaskCreate):
    try:
        db_task = models.Task(**task.dict())
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        return db_task
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

# Update an existing task
def update_task(db: Session, task_id: int, task_update: schemas.TaskCreate):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    try:
        task.title = task_update.title
        task.description = task_update.description
        db.commit()
        db.refresh(task)
        return task
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

# Delete a task
def delete_task(db: Session, task_id: int):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    try:
        db.delete(task)
        db.commit()
        return {"message": "Task deleted"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))