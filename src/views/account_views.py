from pydantic import AwareDatetime, BaseModel, NaiveDatetime
from uuid import UUID
from decimal import Decimal


class AccountOut(BaseModel):
    id: UUID
    user_id: UUID
    balance: Decimal
    created_at: AwareDatetime | NaiveDatetime


class TransactionOut(BaseModel):
    id: UUID
    account_id: UUID
    type: str
    amount: Decimal
    timestamp: AwareDatetime | NaiveDatetime