from sqlalchemy import Enum
import enum

class TransactionType(enum.Enum):
    deposit = "deposit"
    withdrawal = "withdrawal"