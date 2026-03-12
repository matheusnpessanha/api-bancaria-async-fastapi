@router.post("/transactions")
async def create_transaction(
    data: TransactionCreate,
    db: AsyncSession = Depends(get_db)
):

    account = await get_account(db, data.account_id)

    transaction = await TransactionService.create_transaction(
        db=db,
        account=account,
        amount=data.amount,
        type=data.type
    )

    return transaction