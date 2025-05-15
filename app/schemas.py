from pydantic import BaseModel

# Shared properties for Task
class TaskBase(BaseModel):
    title: str
    description: str

# Schema for creating a Task
class TaskCreate(TaskBase):
    pass

# Schema for returning a Task (with ID)
class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True