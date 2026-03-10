from sqlalchemy import ForeignKey, Numeric
from decimal import Decimal
from sqlalchemy.orm import Mapped,mapped_column, relationship
from src.models.base import BaseModel
from typing import List, TYPE_CHECKING
from uuid import UUID

if TYPE_CHECKING:
    from models.users_models import UserModel
    from models.transactions_models import TransactionModel

class AccountModel(BaseModel):
    __tablename__ = 'accounts'

    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    balance: Mapped[Decimal] = mapped_column(Numeric(10, 2), default=0, nullable=False)
    user: Mapped["UserModel"] = relationship(back_populates="accounts")
    transactions: Mapped[List["TransactionModel"]] = relationship(back_populates="account")



