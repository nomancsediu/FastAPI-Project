from pydantic import BaseModel

# DTOs for Task
class TaskSchema(BaseModel):
    title: str
    description: str
    is_completed: bool = False

# Response DTO for Task
class TaskResponseSchema(TaskSchema):
    id: int