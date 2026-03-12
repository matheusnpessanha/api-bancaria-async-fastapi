from uuid import UUID
from decimal import Decimal
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.models.accounts_models import AccountModel
from src.models.users_models import UserModel


class AccountService:

    @staticmethod
    async def create_account(
        db: AsyncSession,
        user_id: UUID,
        initial_balance: Decimal = Decimal("0")
    ):
        # Check if the user exists
        user = await db.get(UserModel, user_id)
        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        # Create the account
        account = AccountModel(
            user_id=user_id,
            balance=initial_balance
        )

        db.add(account)
        await db.commit()
        await db.refresh(account)
        return account


    @staticmethod
    async def get_account_by_id(
        db: AsyncSession,
        account_id: UUID
    ):
        account = await db.get(AccountModel, account_id)

        if not account:
            raise HTTPException(
                status_code=404,
                detail="Account not found"
            )

        return account


    @staticmethod
    async def list_accounts(
        db: AsyncSession,
        limit: int = 10,
        skip: int = 0
    ):
        query = select(AccountModel).limit(limit).offset(skip)

        result = await db.execute(query)

        return result.scalars().all()