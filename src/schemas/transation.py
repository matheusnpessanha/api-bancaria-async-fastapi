from enum import Enum
from pydantic import BaseModel, PositiveFloat

class TransitionType(Enum):
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"

class TransitionIn(BaseModel):
    account_id: int
    type: TransitionType
    amount: PositiveFloat

    class Config:
        use_enum_values = True

