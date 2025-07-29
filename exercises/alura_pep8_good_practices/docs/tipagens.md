## 1. Tipagem em Variáveis
```python
nome: str = "Lorenzo"
idade: int = 30
altura: float = 1.75
ativo: bool = True
```

## 2. Tipagem em Listas
```python
from typing import List

nomes: List[str] = ["Ana", "Bruno", "Carlos"]
idades: List[int] = [25, 30, 40]
```

## 3. Tipagem em Tuplas
```python
from typing import Tuple

coordenadas: Tuple[float, float] = (23.5, 45.1)
pessoa: Tuple[str, int] = ("Lorenzo", 30)
```

## 4. Tipagem em Dicionários
```python
from typing import Dict

usuario: Dict[str, str] = {
    "nome": "Lorenzo",
    "email": "lorenzo@example.com"
}

estoque: Dict[str, int] = {
    "maçã": 10,
    "banana": 5
}
```

## 5. Tipagem em Funções
```python
def somar(a: int, b: int) -> int:
    return a + b

def saudacao(nome: str) -> str:
    return f"Olá, {nome}!"

def media(notas: List[float]) -> float:
    return sum(notas) / len(notas)
```

## 6. Tipagem em Classes
```python
from typing import Optional

class Pessoa:
    def __init__(self, nome: str, idade: int, email: Optional[str] = None):
        self.nome: str = nome
        self.idade: int = idade
        self.email: Optional[str] = email

    def aniversario(self) -> None:
        self.idade += 1
```

## Observações
* `Optional[str]` significa que o valor pode ser do tipo `str` ou `None`.
* Tipos como `List`, `Dict`, `Tuple` são importados de `typing` (no Python 3.9+, você pode usar `list`, `dict`, `tuple` com tipagem entre colchetes, ex: `list[str]`, `dict[str, int]`).
* Usar tipagem ajuda com **autocompletar**, **verificação estática** (com ferramentas como `mypy`) e **documentação**.