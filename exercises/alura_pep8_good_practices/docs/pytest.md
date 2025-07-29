## O que é o `pytest`?
O `pytest` é uma das bibliotecas mais populares e poderosas para testes automatizados em Python. Ele é simples de começar, mas muito robusto para projetos grandes.

É um framework de **testes automatizados** para Python que permite escrever testes de forma clara, escalável e com relatórios detalhados. Funciona bem com `unittest`, `doctest` e outras ferramentas.

## Instalação
```bash
pip install pytest
```

## Estrutura de Projeto (boa prática)
```bash
meu_projeto/
├── src/
│   └── app.py
├── tests/
│   └── test_app.py
├── requirements.txt
└── pytest.ini  # (opcional)
```

## Exemplo simples
### Arquivo: `src/app.py`
```python
def soma(a, b):
    return a + b
```

### Arquivo: `tests/test_app.py`
```python
from src.app import soma

def test_soma():
    assert soma(2, 3) == 5
```

### Rodar o teste:
```bash
pytest
```

Saída esperada:

```
collected 1 item
tests/test_app.py .                                               [100%]
```

## Testes parametrizados
```python
import pytest
from src.app import soma

@pytest.mark.parametrize("a, b, resultado", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, -1, -2),
])
def test_soma_parametrizado(a, b, resultado):
    assert soma(a, b) == resultado
```

## Testes com exceção
```python
import pytest

def dividir(a, b):
    if b == 0:
        raise ValueError("Divisão por zero!")
    return a / b

def test_divisao_zero():
    with pytest.raises(ValueError, match="Divisão por zero!"):
        dividir(10, 0)
```

## Boas práticas com `pytest`

| Boas práticas                               | Descrição                                                   |
| ------------------------------------------- | ----------------------------------------------------------- |
| Usar prefixo `test_` nos arquivos e funções | Para que o `pytest` consiga identificá-los automaticamente. |
| Escrever testes pequenos e objetivos        | Cada teste deve validar um único comportamento.             |
| Usar `pytest.mark.parametrize`              | Para testar múltiplos cenários com menos código.            |
| Separar código da aplicação e dos testes    | Mantenha testes em uma pasta `tests/`.                      |
| Usar fixtures para preparação de dados      | Ideal para setups reutilizáveis (ex: conexões, objetos).    |

## `pytest.ini` — Configurações opcionais
```ini
# pytest.ini
[pytest]
minversion = 6.0
addopts = -ra -q
testpaths = 
    tests
```

## Plugins úteis
| Plugin         | Função                                       |
| -------------- | -------------------------------------------- |
| `pytest-cov`   | Geração de relatório de cobertura de testes. |
| `pytest-mock`  | Facilita o uso de mocks e spies.             |
| `pytest-xdist` | Executa testes em paralelo.                  |

Instalação de plugin:
```bash
pip install pytest-cov
```

## Cobertura de testes
```bash
pytest --cov=src tests/
```