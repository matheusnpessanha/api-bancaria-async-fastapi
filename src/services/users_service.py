from fastapi import HTTPException
from src.utils.cpf_validator import validate_cpf

class UserService:

    @staticmethod
    def validate_user(name: str, cpf: str, age: int):

        if not name:
            raise HTTPException(
                status_code=400,
                detail="Name is required"
            )

        if not validate_cpf(cpf):
            raise HTTPException(
                status_code=400,
                detail="Invalid CPF"
            )

        if age < 18:
            raise HTTPException(
                status_code=400,
                detail="User must be at least 18 years old"
            )