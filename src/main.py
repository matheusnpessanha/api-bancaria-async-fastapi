from src.core.database import engine
from src.models.base import BaseModel
from src.models import users_models, accounts_models, transactions_models
from fastapi import FastAPI

app = FastAPI(title='Project-bank-api-async')

@app.on_event("startup")
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)