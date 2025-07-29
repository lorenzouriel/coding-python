# Testes com FastAPI
* Criação de endpoints com FastAPI
* Testes com `TestClient` (fornecido pela FastAPI via Starlette)
* Estrutura de projeto ideal


## Estrutura de Projeto
```bash
meu_projeto/
├── app/
│   ├── main.py           # FastAPI app
│   └── routes.py         # Endpoints separados
├── tests/
│   └── test_routes.py    # Testes com pytest
├── requirements.txt
└── pytest.ini
```

## 1. Código da API (`app/main.py`)
```python
from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="API de Teste")

app.include_router(router)
```

## 2. Rotas da API (`app/routes.py`)
```python
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Item(BaseModel):
    nome: str
    preco: float

@router.get("/")
def home():
    return {"mensagem": "Bem-vindo à API!"}

@router.post("/item/")
def criar_item(item: Item):
    return {"nome": item.nome, "preco": item.preco}
```

## 3. Testes com Pytest (`tests/test_routes.py`)
```python
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"mensagem": "Bem-vindo à API!"}

def test_criar_item():
    payload = {"nome": "Camiseta", "preco": 49.90}
    response = client.post("/item/", json=payload)
    assert response.status_code == 200
    assert response.json() == payload
```

## 4. Arquivo `pytest.ini` (opcional)
```ini
[pytest]
testpaths = tests
addopts = -ra -q
```

## 5. Arquivo `requirements.txt`
```txt
fastapi
uvicorn
pytest
httpx
```
> `httpx` é usado internamente por `TestClient`.

## Como executar os testes
```bash
pytest
```

## Dica: Testando exceções e validações
Você pode testar também cenários negativos (ex: erro 422):
```python
def test_criar_item_dados_invalidos():
    response = client.post("/item/", json={"nome": "Caneca"})  # Faltando "preco"
    assert response.status_code == 422
```