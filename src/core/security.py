from uuid import uuid4
import time
from datetime import datetime, timedelta
import jwt
from typing import Annotated
from pydantic import BaseModel
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPBearer
from src.core.config import settings

SECRET = settings.JWT_SECRET
ALGORITHM = settings.JWT_ALGORITHM


class AccessToken(BaseModel):
    iss: str
    sub: int
    aud: str
    exp: float
    iat: float
    nbf: float
    jti: str


class JWTToken(BaseModel):
    access_token: AccessToken


def sign_jwt(user_id):
    payload = {
        "sub": str(user_id),  
        "exp": datetime.utcnow() + timedelta(hours=1)  
    }

    token = jwt.encode(payload, SECRET, algorithm=ALGORITHM)

    return {"access_token": token}


async def decode_jwt(token: str) -> JWTToken | None:
    try:
        decoded_token = jwt.decode(
            token,
            SECRET,
            audience="desafio-bank",
            algorithms=[ALGORITHM],
        )

        token_data = JWTToken.model_validate(
            {"access_token": decoded_token}
        )

        return token_data if token_data.access_token.exp >= time.time() else None

    except Exception:
        return None


class JWTBearer(HTTPBearer):

    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> JWTToken:

        authorization = request.headers.get("Authorization", "")

        scheme, _, credentials = authorization.partition(" ")

        if credentials:

            if scheme != "Bearer":
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid authentication scheme.",
                )

            payload = await decode_jwt(credentials)

            if not payload:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid or expired token.",
                )

            return payload

        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authorization code.",
            )


async def get_current_user(
    token: Annotated[JWTToken, Depends(JWTBearer())],
) -> dict[str, int]:

    return {"user_id": token.access_token.sub}


def login_required(
    current_user: Annotated[dict[str, int], Depends(get_current_user)]
):

    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied",
        )

    return current_user