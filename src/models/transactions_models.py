from src.models.base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Numeric, Enum
from uuid import UUID
from decimal import Decimal
from typing import TYPE_CHECKING
from src.models.enum_type import TransactionType

if TYPE_CHECKING:
    from models.accounts_models import AccountModel


class TransactionModel(BaseModel):
    __tablename__ = 'transactions'

    type: Mapped[TransactionType] = mapped_column(Enum(TransactionType), nullable=False)
    account_id: Mapped[UUID] = mapped_column(ForeignKey("accounts.id"), nullable=False)
    amount: Mapped[Decimal] = mapped_column(Numeric(10, 2), default=0 ,nullable=False)
    account: Mapped["AccountModel"] = relationship(back_populates="transactions") 


