from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models.base import BaseModel
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from models.accounts_models import AccountModel

class UserModel(BaseModel):
    __tablename__ = 'users'

    name: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), unique=True, nullable=False, index=True)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    accounts: Mapped[List["AccountModel"]] = relationship(back_populates="user")