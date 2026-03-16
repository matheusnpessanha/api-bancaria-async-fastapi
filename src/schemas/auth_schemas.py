from pydantic import BaseModel 
from uuid import UUID

class LoginIn(BaseModel):
    user_id: UUID  

class TokenResponse(BaseModel):
    access_token: str