# 🚀 FastAPI Async API (DIO Project)

Projeto desenvolvido como parte do desafio da DIO para criação de uma **API bancária assíncrona com FastAPI**.

---

## 🧱 Tecnologias utilizadas

- FastAPI
- SQLAlchemy (async)
- Alembic (migrations)

---

## ⚙️ Configuração do ambiente

### 1. Criar ambiente virtual

python -m venv venv

### 2. Ativar ambiente virtual

#### Windows:
venv\Scripts\activate

#### Linux / Mac:
source venv/bin/activate

### 3. Instalar dependências
pip install -r requirements.txt

### 4. 🔑 Variáveis de ambiente

Crie um arquivo .env na raiz do projeto:
DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/app_db

🗄️ Migrations (Alembic)

Criar migration
alembic revision --autogenerate -m "initial"

Aplicar migrations

alembic upgrade head

▶️ Rodando a aplicação

uvicorn main:app --reload





👨‍💻 Autor

Projeto desenvolvido por Matheus Pessanha.
