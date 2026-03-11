from datetime import datetime  
from pydantic import BaseModel
from uuid import UUID
from decimal import Decimal
from src.models.enum_type import TransactionType

class TransactionCreate(BaseModel):
    account_id: UUID
    type: TransactionType
    amount: Decimal

class TransactionResponse(BaseModel):
    id: UUID
    type: TransactionType
    account_id: UUID
    amount: Decimal
    created_at: datetime

    class Config:
        from_attributes = True

