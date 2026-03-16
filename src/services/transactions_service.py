from decimal import Decimal
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.transactions_models import TransactionModel
from src.models.accounts_models import AccountModel
from src.models.enum_type import TransactionType
from uuid import UUID

class TransactionsService:
    @staticmethod
    async def create_transaction(db: AsyncSession, account_id: UUID, amount: Decimal, type: TransactionType):
        # Fetch the account
        account = await db.get(AccountModel, account_id)
        if not account:
            raise HTTPException(status_code=404, detail="Account not found")

        # Update the account balance based on the transaction type
        if type == TransactionType.deposit:
            account.balance += amount
        elif type == TransactionType.withdrawal:
            if account.balance < amount:
                raise HTTPException(status_code=400, detail="Insufficient funds")
            account.balance -= amount

        # Create a new transaction record
        transaction = TransactionModel(
            account_id=account_id,
            amount=amount,
            type=type
        )
        db.add(transaction)
        await db.commit()
        await db.refresh(transaction)

        return transaction