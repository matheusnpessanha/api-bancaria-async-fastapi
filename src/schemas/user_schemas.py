from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime

class UserCreate(BaseModel):
    name: str = Field(..., max_length=50)
    cpf: str = Field(..., min_length=11, max_length=11)
    age: int = Field(..., gt=0)

class UserResponse(BaseModel):
    id: UUID
    name: str
    cpf: str
    age: int
    created_at: datetime


    class Config:
        from_attributes = True

