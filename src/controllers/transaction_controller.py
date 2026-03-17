from fastapi import APIRouter, Depends, status
from src.schemas.transaction_schemas import TransactionCreate
from src.core.security import login_required
from src.services.transactions_service import TransactionsService
from src.views.transaction_views import TransactionOut

router = APIRouter(prefix="/transactions", tags=["Transactions"])

service = TransactionsService()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=TransactionOut)
async def create_transaction(
    transaction: TransactionCreate,
    current_user = Depends(login_required)
):
    return await service.create(
        user_id=current_user["user_id"],
        transaction=transaction
    )