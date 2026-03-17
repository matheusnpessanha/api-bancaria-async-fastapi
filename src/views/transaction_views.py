from pydantic import AwareDatetime, BaseModel, NaiveDatetime
from uuid import UUID   
from decimal import Decimal 


class TransactionOut(BaseModel):
    id: UUID
    account_id: UUID
    type: str
    amount: Decimal
    timestamp: AwareDatetime | NaiveDatetime