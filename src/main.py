from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from src.core.database import engine
from src.models.base import BaseModel
from src.controllers import auth_controller, account_controller, transaction_controller



# 🔄 Lifecycle (startup/shutdown)
@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)

    yield

    # shutdown (se quiser fechar conexões futuramente)


# 🏷️ Tags (Swagger organizado)
tags_metadata = [
    {"name": "Auth", "description": "Authentication"},
    {"name": "Users", "description": "User management"},
    {"name": "Accounts", "description": "Bank accounts"},
    {"name": "Transactions", "description": "Financial operations"},
]


app = FastAPI(
    title="Bank API",
    version="1.0.0",
    description="API bancária assíncrona com FastAPI",
    openapi_tags=tags_metadata,
    lifespan=lifespan,
)


# 🌍 CORS (liberar acesso externo)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 🔗 Registrar rotas
app.include_router(auth_controller.router)
app.include_router(account_controller.router)
app.include_router(transaction_controller.router)


# ❌ Tratamento genérico de erro (opcional)
@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": str(exc)},
    )