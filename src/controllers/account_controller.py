from fastapi import APIRouter, Depends, status
from src.schemas.account_schemas import AccountCreate
from src.core.security import login_required
from src.services.accounts_service import AccountService
from src.services.transactions_service import TransactionsService
from src.views.account_views import AccountOut, TransactionOut
from uuid import UUID

router = APIRouter(prefix="/accounts", tags=["Accounts"])

account_service = AccountService()
tx_service = TransactionsService()


@router.get("/", response_model=list[AccountOut])
async def read_accounts(
    limit: int = 10,
    skip: int = 0,
    current_user = Depends(login_required)
):
    return await account_service.read_all(
        user_id=current_user["user_id"],
        limit=limit,
        skip=skip
    )


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=AccountOut)
async def create_account(
    account: AccountCreate,
    current_user = Depends(login_required)
):
    return await account_service.create(
        user_id=current_user["user_id"],
        account=account
    )


@router.get("/{id}/transactions", response_model=list[TransactionOut])
async def read_account_transactions(
    id: UUID,
    limit: int,
    skip: int = 0,
    current_user = Depends(login_required)
):
    return await tx_service.read_all(
        user_id=current_user["user_id"],
        account_id=id,
        limit=limit,
        skip=skip
    )