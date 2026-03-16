from validate_docbr import CPF

def validate_cpf(cpf: str) -> bool:
    cpf_validator = CPF()
    if not cpf_validator.validate(cpf):
        raise ValueError("Invalid CPF")