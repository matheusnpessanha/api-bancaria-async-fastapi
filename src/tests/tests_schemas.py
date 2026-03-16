from uuid import uuid4

from src.schemas.auth_schemas import LoginIn
from src.schemas.user_schemas import UserCreate
from src.schemas.transaction_schemas import TransactionCreate
from src.models.enum_type import TransactionType


def test_signin():
    data = {"user_id": str(uuid4())}
    schema = LoginIn(**data)
    print("SignIn OK ->", schema)


def test_user():
    data = {
        "name": "Matheus",
        "cpf": "12345678901",
        "age": 25
    }

    schema = UserCreate(**data)
    print("UserCreate OK ->", schema)


def test_transaction():
    data = {
        "account_id": str(uuid4()),
        "type": TransactionType.deposit,
        "amount": 100.50
    }

    schema = TransactionCreate(**data)
    print("TransactionCreate OK ->", schema)


if __name__ == "__main__":
    test_signin()
    test_user()
    test_transaction()